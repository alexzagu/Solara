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
#-------------------------------------------------------------

def p_program(p):
  '''
    program : PROGRAM ID COLON VARS COLON DECLARATIONS CORE COLON S_BLOCK
  '''

#-------------------------------------------------------------

def p_declarations(p):
  '''
    DECLARATIONS : TYPE A TICK E
  '''

def p_a(p):
  '''
    A : ID B D
  '''

def p_b(p):
  '''
    B : EQUALS C
    | empty
  '''

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

def p_e(p):
  '''
    E : DECLARATIONS
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
    S_STATUTE : SOLUTION_DEF
    | STATUTE
  '''

#-------------------------------------------------------------

def p_solution_def(p):
  '''
    SOLUTION_DEF : SOL S_TYPE ID L_PAREN PARAMS R_PAREN COLON BLOCK TICK
  '''

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

#-------------------------------------------------------------

def p_expression(p):
  '''
    EXPRESSION : EXP G
  '''

def p_g(p):
  '''
    G : H EXP
    | empty
  '''

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

#-------------------------------------------------------------

def p_exp(p):
  '''
    EXP : TERM I
  '''

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

#-------------------------------------------------------------

def p_term(p):
  '''
    TERM : FACTOR K
  '''

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

#-------------------------------------------------------------

def p_factor(p):
  '''
    FACTOR : L_PAREN EXPRESSION R_PAREN
    | M CON_VAR
  '''

def p_m(p):
  '''
    M : PLUS
    | MINUS
    | empty
  '''

#-------------------------------------------------------------

def p_con_var(p):
  '''
    CON_VAR : ID_REF
    | INT_CONT
    | STRING_CONT
    | CHAR_CONT
    | FLOAT_CONT
    | BOOL_CONT
    | SOLUTION_CALL
  '''

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
    ID_REF : ID O
  '''

def p_o(p):
  '''
    O : L_BRACK EXPRESSION R_BRACK
    | empty
  '''

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
    T : ELSE BLOCK
  '''

#-------------------------------------------------------------

def p_solution_call(p):
  '''
    SOLUTION_CALL : ID L_PAREN V R_PAREN TICK
  '''

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
    PARAMS : TYPE ID Y
  '''

def p_y(p):
  '''
    Y : COMMA PARAMS
    | empty
  '''

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

#with open('../testing/success_test.txt', 'r') as myfile:
#    data = myfile.read()

with open('../testing/failure_test.txt', 'r') as myfile:
    data = myfile.read()

result = parser.parse(data)
print(result)