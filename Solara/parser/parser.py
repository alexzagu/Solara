# -*- coding: utf-8 -*-
#-------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  05/03/17
#-------------------------------------------------------------
import ply.yacc as yacc
import sys
from scanner.scanner import tokens
from scanner.scanner import t_INT_CONT
from scanner.scanner import t_FLOAT_CONT
from scanner.scanner import t_STRING_CONT
from scanner.scanner import t_CHAR_CONT
from structures.function_directory import functionDirectory
from structures.symbol_table import symbolTable
from structures.semantic_cube import semanticCube
from structures.quad_queue import quadQueue
import re
#-------------------------------------------------------------
funDir = functionDirectory()
semCube = semanticCube()
currentType = None # Code signing of the type
currentSymTab = None # Actual object of the symbol table
currentVar = None # Variable that's being processed at the moment
currentSol = None # Solution that's being processed at the moment
programID = None # Name of the main solution (program's name)
POperators = [] # Stack of pending operators to process
POperands = [] # Stack of pending operands to process
PTypes = [] # Stack of pending operand types to process
quadQueue = quadQueue()
#-------------------------------------------------------------

def p_program(p):
    '''
    program : PROGRAM ID create_global_fun COLON VAR_BLOCK print_currentSymTab SOLS COLON SOL_DEFINITIONS MAIN_DEFINITION
    '''

def p_create_global_fun(p):
    '''
    create_global_fun :
    '''
    global currentSymTab
    global programID
    currentSymTab = symbolTable()
    funDir.add(p[-1], 6, (), currentSymTab)
    programID = p[-1]

def p_print_currentSymTab(p):
    '''
    print_currentSymTab :
    '''
    #print(funDir)
    #print(currentSymTab)

#-------------------------------------------------------------

def p_var_block(p):
    '''
    VAR_BLOCK : VARS COLON AA
    '''

def p_aa(p):
    '''
    AA : VAR_DEFINITIONS AA
    | empty
    '''

#-------------------------------------------------------------

def p_var_definitions(p):
    '''
    VAR_DEFINITIONS : TYPE store_type A TICK
    '''

def p_store_type(p):
    '''
    store_type :
    '''
    global currentType
    if p[-1] == 'int':
        currentType = 0
    elif p[-1] == 'float':
        currentType = 1
    elif p[-1] == 'string':
        currentType = 2
    elif p[-1] == 'char':
        currentType = 3
    elif p[-1] == 'bool':
        currentType = 4
    elif p[-1] == 'list':
        currentType = 5
    else:
        currentType = 6

def p_a(p):
    '''
    A : ID check_var_duplicates B D
    '''

def p_check_var_duplicates(p):
    '''
    check_var_duplicates :
    '''
    global currentSymTab
    global currentType
    global currentVar
    if currentSymTab.search(p[-1]) is None:
        currentSymTab.add(p[-1], currentType, None)
        currentVar = p[-1]
    else:
        p_error_duplicate_var(p[-1])

def p_b(p):
    '''
    B : EQUALS C assign_var_value
    | empty
    '''

def p_assign_var_value(p):
    '''
    assign_var_value :
    '''
    global currentSymTab
    global currentVar
    global currentType
    currentSymTab.add(currentVar, currentType, p[-1])

def p_c(p):
    '''
    C : EXPRESSION
    | LIST_EXP
    '''

def p_d(p):
    '''
    D : COMMA A
    | empty
    '''

#-------------------------------------------------------------

def p_s_block(p):
    '''
    S_BLOCK : L_BRACE F R_BRACE
    '''

def p_f(p):
    '''
    F : S_STATUTE F
    | empty
    '''

#-------------------------------------------------------------

def p_s_statute(p):
    '''
    S_STATUTE : VAR_DEFINITIONS
    | STATUTE
    '''

#-------------------------------------------------------------

def p_solution_def(p):
    '''
    SOLUTION_DEF : SOL S_TYPE store_type ID check_sol_duplicates L_PAREN PARAMS R_PAREN COLON S_BLOCK TICK print_currentSymTab
    '''

def p_check_sol_duplicates(p):
    '''
    check_sol_duplicates :
    '''
    if funDir.search(p[-1]) is None:
        global currentSymTab
        global currentType
        global currentSol
        currentSymTab = symbolTable()
        funDir.add(p[-1], currentType, (), currentSymTab)
        currentSol = p[-1]
    else:
        p_error_duplicate_sol(p[-1])

#-------------------------------------------------------------

def p_statute(p):
    '''
    STATUTE : CONDITION
    | CYCLE
    | ASSIGNATION
    '''

#-------------------------------------------------------------

def p_s_type(p):
    '''
    S_TYPE : VOID
    | TYPE
    '''
    if p[1] == 'void':
        p[0] = 'void'
    else:
        p[0] = p[1]

#-------------------------------------------------------------

def p_type(p):
    '''
    TYPE : INT
    | FLOAT
    | CHAR
    | STRING
    | BOOL
    | LIST
    '''
    if p[1] == 'int':
        p[0] = 'int'
    elif p[1] == 'float':
        p[0] = 'float'
    elif p[1] == 'char':
        p[0] = 'char'
    elif p[1] == 'string':
        p[0] = 'string'
    elif p[1] == 'bool':
        p[0] = 'bool'
    else:
        p[0] = 'list'

#-------------------------------------------------------------

def p_expression(p):
    '''
    EXPRESSION : EXP G
    '''

def p_g(p):
    '''
    G : H EXP process_possible_relop_operation
    | empty
    '''

def p_process_possible_relop_operation(p):
    '''
    process_possible_relop_operation :
    '''
    operator = POperators[len(POperators) - 1]
    if operator == '<' or operator == '>' or operator == '>=' or operator == '<=' or operator == '==' or \
                    operator == 'is' or operator == '&&' or operator == 'and' or operator == '||' or \
                    operator == 'or' or operator == '%' or operator == 'mod':
        right_operand = POperands.pop()
        right_type = PTypes.pop()
        left_operand = POperands.pop()
        left_type = PTypes.pop()
        operator = POperators.pop()
        result_type = semCube.search((left_type, operator, right_type))

        if not result_type is None:
            result = quadQueue.avail()
            quadQueue.add(operator, left_operand, right_operand, result)
            POperands.append(result)
            PTypes.append(result_type)
        else:
            print(str(left_type) + ', ' + operator + ', ' + str(right_type))
            p_error_type_mismatch(p)

def p_h(p):
    '''
    H : LESS_T
    | GREATER_T
    | GREATER_T_EQUALS
    | LESS_T_EQUALS
    | IS
    | AND
    | OR
    | PERCENTAGE
    '''
    if p[1] == '<':
        POperators.append('<')
    elif p[1] == '>':
        POperators.append('>')
    elif p[1] == '>=':
        POperators.append('>=')
    elif p[1] == '<=':
        POperators.append('<=')
    elif p[1] == '==' or p[1] == 'is':
        POperators.append('==')
    elif p[1] == '&&' or p[1] == 'and':
        POperators.append('&&')
    elif p[1] == '||' or p[1] == 'or':
        POperators.append('||')
    else:
        POperators.append('%')

#-------------------------------------------------------------

def p_exp(p):
    '''
    EXP : TERM process_possible_plus_minus_operation I
    '''

def p_process_possible_plus_minus_operation(p):
    '''
    process_possible_plus_minus_operation :
    '''
    if len(POperators) > 0:
        operator = POperators[len(POperators) - 1]
        if operator == '+' or operator == '-':
            right_operand = POperands.pop()
            right_type = PTypes.pop()
            left_operand = POperands.pop()
            left_type = PTypes.pop()
            operator = POperators.pop()
            result_type = semCube.search((left_type, operator, right_type))

            if not result_type is None:
                result = quadQueue.avail()
                quadQueue.add(operator, left_operand, right_operand, result)
                POperands.append(result)
                PTypes.append(result_type)
            else:
                print(str(left_type) + ', ' + operator + ', ' + str(right_type))
                p_error_type_mismatch(p)

def p_i(p):
    '''
    I : J EXP
    | empty
    '''

def p_j(p):
    '''
    J : PLUS
    | MINUS
    '''
    if p[1] == '+':
        POperators.append('+')
    else:
        POperators.append('-')

#-------------------------------------------------------------

def p_term(p):
    '''
    TERM : FACTOR process_possible_multiply_divide_operation K
    '''

def p_process_possible_multiply_divide_operation(p):
    '''
    process_possible_multiply_divide_operation :
    '''
    if len(POperators) > 0:
        operator = POperators[len(POperators) - 1]
        if operator == '*' or operator == '/':
            right_operand = POperands.pop()
            right_type = PTypes.pop()
            left_operand = POperands.pop()
            left_type = PTypes.pop()
            operator = POperators.pop()
            result_type = semCube.search((left_type, operator, right_type))

            if not result_type is None:
                result = quadQueue.avail()
                quadQueue.add(operator, left_operand, right_operand, result)
                POperands.append(result)
                PTypes.append(result_type)
            else:
                print(str(left_type) + ', ' + operator + ', ' + str(right_type))
                p_error_type_mismatch(p)

def p_k(p):
    '''
    K : L TERM
    | empty
    '''

def p_l(p):
    '''
    L : MULTIPLY
    | DIVIDE
    '''
    if p[1] == '*':
        POperators.append('*')
    else:
        POperators.append('/')

#-------------------------------------------------------------

def p_factor(p):
    '''
    FACTOR : L_PAREN push_false_bottom EXPRESSION R_PAREN pop_false_bottom
    | M CON_VAR check_sign_type_correspondence
    '''

def p_push_false_bottom(p):
    '''
    push_false_bottom :
    '''
    POperators.append('(')

def p_pop_false_bottom(p):
    '''
    pop_false_bottom :
    '''
    POperators.pop()

def p_check_sign_type_correspondence(p):
    '''
    check_sign_type_correspondence :
    '''
    if p[-2] == '+' or p[-2] == '-':
        var_type = PTypes[len(PTypes) - 1]
        if not (var_type == 0 or var_type == 1):
            p_error_sign_type_mismatch(p)

def p_m(p):
    '''
    M : PLUS
    | MINUS
    | empty
    '''
    if p[1] == '+':
        POperators.append('+')
        p[0] = '+'
    elif p[-1] == '-':
        POperators.append('-')
        p[0] = '-'

#-------------------------------------------------------------

def p_con_var(p):
    '''
    CON_VAR : ID_REF
    | CON_VAR_TERMINAL
    | SOLUTION_CALL
    | PREDEFINED_SOLS
    '''

def p_con_var_terminal(p):
    '''
    CON_VAR_TERMINAL : INT_CONT
    | STRING_CONT
    | CHAR_CONT
    | FLOAT_CONT
    | BOOL_CONT
    '''
    int_r = re.compile(t_INT_CONT)
    string_r = re.compile(t_STRING_CONT)
    char_r = re.compile(t_CHAR_CONT)
    float_r = re.compile(t_FLOAT_CONT)
    if p[1] == 'true' or p[1] == 'false':
        POperands.append(p[1] == 'true')
        PTypes.append(4)
    elif float_r.match(p[1]):
        POperands.append(float(p[1]))
        PTypes.append(1)
    elif int_r.match(p[1]):
        POperands.append(int(p[1]))
        PTypes.append(0)
    elif string_r.match(p[1]):
        POperands.append(p[1])
        PTypes.append(2)
    elif char_r.match(p[1]):
        POperands.append(p[1])
        PTypes.append(3)
    else:
        p_error_unidentified_constant(p)

#-------------------------------------------------------------

def p_negation(p):
    '''
    NEGATION : N EXPRESSION
    '''

def p_n(p):
    '''
    N : NOT
    '''

#-------------------------------------------------------------

def p_ID_ref(p):
    '''
    ID_REF : ID check_var_existence get_var_type O
    '''
    POperands.append(p[1])
    PTypes.append(p[3])

def p_check_var_existence(p):
    '''
    check_var_existence :
    '''
    if currentSymTab.search(p[-1]) is None and funDir.search(programID)[2].search(p[-1]) is None:
        p_error_undefined_var(p[-1])

def p_get_var_type(p):
    '''
    get_var_type :
    '''
    if currentSymTab.search(p[-2]) is None:
        p[0] = funDir.search(programID)[2].search(p[-2])[0]
    else:
        p[0] = currentSymTab.search(p[-2])[0]

def p_o(p):
    '''
    O : L_BRACK EXPRESSION check_int_type R_BRACK
    | empty
    '''

def p_check_int_type(p):
    '''
    check_int_type :
    '''
    if p[-1] != 0:
        p_error_noninteger_indexing(p[-1])

#-------------------------------------------------------------

def p_list_exp(p):
    '''
    LIST_EXP : L_BRACK EXPRESSION P R_BRACK
    '''

def p_p(p):
    '''
    P : COMMA EXPRESSION P
    | empty
    '''

#-------------------------------------------------------------

def p_assignation(p):
    '''
    ASSIGNATION : ID_REF EQUALS EXPRESSION TICK
    '''

#-------------------------------------------------------------

def p_block(p):
    '''
    BLOCK : L_BRACE Q R_BRACE
    '''

def p_q(p):
    '''
    Q : STATUTE Q
    | empty
    '''

#-------------------------------------------------------------

def p_s_assignation(p):
    '''
    S_ASSIGNATION : ID_REF EQUALS EXPRESSION
    '''

#-------------------------------------------------------------

def p_while(p):
    '''
    WHILE : WHILE_CYCLE EXPRESSION COLON BLOCK TICK
    '''

#-------------------------------------------------------------

def p_for(p):
    '''
    FOR : FOR_CYCLE S_ASSIGNATION TICK EXPRESSION TICK S_ASSIGNATION COLON BLOCK TICK
    '''

#-------------------------------------------------------------

def p_cycle(p):
    '''
    CYCLE : FOR
    | WHILE
    '''

#-------------------------------------------------------------

def p_condition(p):
    '''
    CONDITION : IF EXPRESSION COLON BLOCK R TICK
    '''

def p_r(p):
    '''
    R : S
    | T
    '''

def p_s(p):
    '''
    S : ELIF EXPRESSION COLON BLOCK U
    '''

def p_u(p):
    '''
    U : S
    | T
    | empty
    '''

def p_t(p):
    '''
    T : ELSE COLON BLOCK
    '''

#-------------------------------------------------------------

def p_solution_call(p):
    '''
    SOLUTION_CALL : ID check_sol_existence L_PAREN V R_PAREN
    '''
    POperands.append(p[1])
    PTypes.append(p[2])

def p_check_sol_existence(p):
    '''
    check_sol_existence :
    '''
    if funDir.search(p[-1]) is None:
        p_error_undefined_sol(p)
    elif p[-1] == 'main':
        p_error_main_not_callable(p)
    else:
        p[0] = funDir.search(p[-1])[0]

def p_v(p):
    '''
    V : W X
    '''

def p_w(p):
    '''
    W : EXPRESSION
    | NEGATION
    '''

def p_x(p):
    '''
    X : COMMA V
    | empty
    '''

#-------------------------------------------------------------

def p_params(p):
    '''
    PARAMS : TYPE store_type ID check_param_duplicates Y
    '''

def p_check_param_duplicates(p):
    '''
    check_param_duplicates :
    '''
    global currentSymTab
    global currentType
    global currentSol
    if currentSymTab.search(p[-1]) is None:
        currentSymTab.add(p[-1], currentType, None)
        funDir.append_parameter(currentSol, currentType)
    else:
        p_error_duplicate_param(p[-1])

def p_y(p):
    '''
    Y : COMMA PARAMS
    | empty
    '''

#-------------------------------------------------------------

def p_sol_definitions(p):
    '''
    SOL_DEFINITIONS : Z
    '''

def p_z(p):
    '''
    Z : SOLUTION_DEF Z
    | empty
    '''

#-------------------------------------------------------------

def p_main_definition(p):
    '''
    MAIN_DEFINITION : INT store_type MAIN_R check_sol_duplicates L_PAREN R_PAREN COLON S_BLOCK TICK print_currentSymTab
    '''
    print(quadQueue)

#-------------------------------------------------------------

def p_draw_circle(p):
    '''
    DRAW_CIRCLE : DRAW_CIRCLE_R L_PAREN EXPRESSION COMMA EXPRESSION COMMA EXPRESSION R_PAREN
    '''
    p[0] = 'drawCircle'

#-------------------------------------------------------------

def p_draw_line(p):
    '''
    DRAW_LINE : DRAW_LINE_R L_PAREN EXPRESSION COMMA EXPRESSION COMMA EXPRESSION COMMA EXPRESSION R_PAREN
    '''
    p[0] = 'drawLine'

#-------------------------------------------------------------

def p_draw_rectangle(p):
    '''
    DRAW_RECTANGLE : DRAW_RECTANGLE_R L_PAREN EXPRESSION COMMA EXPRESSION COMMA EXPRESSION R_PAREN
    '''
    p[0] = 'drawRectangle'

#-------------------------------------------------------------

def p_move_up(p):
    '''
    MOVE_UP : MOVE_UP_R L_PAREN EXPRESSION R_PAREN
    '''
    p[0] = 'moveUp'

#-------------------------------------------------------------

def p_move_right(p):
    '''
    MOVE_RIGHT : MOVE_RIGHT_R L_PAREN EXPRESSION R_PAREN
    '''
    p[0] = 'moveRight'

#-------------------------------------------------------------

def p_move_down(p):
    '''
    MOVE_DOWN : MOVE_DOWN_R L_PAREN EXPRESSION R_PAREN
    '''
    p[0] = 'moveDown'

#-------------------------------------------------------------

def p_move_left(p):
    '''
    MOVE_LEFT : MOVE_LEFT_R L_PAREN EXPRESSION R_PAREN
    '''
    p[0] = 'moveLeft'

#-------------------------------------------------------------

def p_print(p):
    '''
    PRINT : PRINT_R L_PAREN EXPRESSION R_PAREN
    '''
    p[0] = 'print'

#-------------------------------------------------------------

def p_predefined_sols(p):
    '''
    PREDEFINED_SOLS : DRAW_LINE
    | DRAW_CIRCLE
    | DRAW_RECTANGLE
    | MOVE_UP
    | MOVE_RIGHT
    | MOVE_DOWN
    | MOVE_LEFT
    | PRINT
    '''
    POperands.append(p[1])
    PTypes.append(6)

#-------------------------------------------------------------

# funcion para manejar errores
def p_empty(p):
  'empty :'
  pass

# funcion para manejar errores
def p_error(p):
    print("Error de sintaxis!")
    print(p.value)
    print(p.type)
    print(p.lineno)

# Error-handling function for duplicate variables
def p_error_duplicate_var(p):
    '''
    '''
    print('Error!')
    print('Variable ' + p + ' already defined.')

# Error-handling function for duplicate parameters
def p_error_duplicate_param(p):
    '''
    '''
    print('Error!')
    print('Parameter ' + p + ' already defined.')

# Error-handling function for duplicate solutions
def p_error_duplicate_sol(p):
    '''
    '''
    print('Error!')
    print('Solution ' + p + ' already defined.')

# Error-handling function for undefined variables
def p_error_undefined_var(p):
    '''
    '''
    print('Error!')
    print('Variable ' + p + ' is not defined.')

# Error-handling function for noninteger indexing
def p_error_noninteger_indexing(p):
    '''
    '''
    print('Error!')
    print('Trying to index a list using a non-integer value.')

# Error-handling function for undefined solutions
def p_error_undefined_sol(p):
    '''
    '''
    print('Error!')
    print('Solution ' + p + ' is not defined.')

# Error-handling function for when main solution is called
def p_error_main_not_callable(p):
    '''
    '''
    print('Error!')
    print('Main solution is not a callable solution.')

# Error-handling function for unidentified constants
def p_error_unidentified_constant(p):
    '''
    '''
    print('Error!')
    print('Constant ' + p + ' is not identified.')

# Error-handling function for sign type mismatch
def p_error_sign_type_mismatch(p):
    '''
    '''
    print('Error!')
    print('Trying to enforce a sign to a non-number value.')

# Error-handling function for type mismatch
def p_error_type_mismatch(p):
    '''
    '''
    print('Error!')
    print('Type mismatch!')

# se contruye el parser
parser = yacc.yacc()

'''
# lista para guardar la lineas de la entrada
lines = []

# se lee linea por linea el contenIDo de un archivo
# especificado como argumento al momento de correr el programa
for line in sys.stdin:
  print('hola')
  stripped = line.strip()
  if not stripped: break
  lines.append(stripped)
# se crea un solo string con los strings en la lista
input = ' '.join(lines)
# se parsea la entrada
print input
'''

with open('../testing/success_test.txt', 'r') as myfile:
    data = myfile.read()

#with open('../testing/failure_test.txt', 'r') as myfile:
#    data = myfile.read()

result = parser.parse(data)
print(result)