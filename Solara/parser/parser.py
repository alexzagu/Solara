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
from structures.virtual_machine import virtualMachine
from structures.main_memory import mainMemory
from structures.execution_block import executionBlock
from structures.list_information import listInformation
from structures.id_ref_information import idRefInformation
import re
from tkinter import *
#-------------------------------------------------------------
funDir = functionDirectory()
semCube = semanticCube()
currentType = None # Code signing of the type of the current variable (currentVar)
currentListType = None # Code signing of the type of the current list
currentSymTab = None # Actual object of the current symbol table
currentVar = None # Variable that's being processed at the moment
currentSol = None # Solution that's being processed at the moment
solHasReturn = False # Boolean that specifies if solution has at least one return statement
programID = None # Name of the main solution (program's name)
POperators = [] # Stack of pending operators to process
POperands = [] # Stack of pending operands to process
PTypes = [] # Stack of pending operand types to process
quadQueue = quadQueue() # Queue of generated quadruples
PJumps = [] # Stack of pending quads to assign a jump to
numParamDefined = [0, 0, 0, 0, 0] # List of number of parameters defined of each data type for the currentSol
numConstUsed = [0, 0, 0, 0, 0] # List of number of constants used of each data type for the entire program
numLocalVarsDefined = [0, 0, 0, 0, 0] # List of number of local variables defined of each data type for the currentSol
numGlobalVarsDefined = [0, 0, 0, 0, 0] # List of number of global variables defined of each data type for the program
numTempVarsDefined = [0, 0, 0, 0, 0] # List of number of temporal variables defined of each data type for the currentSol
param_counter = -1 # Parameter counter for solution call semantic analysis
solution_name = None # Solution name for solution call semantic analysis
virMachine = None
mainMemory = mainMemory()
executionBlock = executionBlock()
currentListInformation = None # Object that holds the information of the list being processed, if any.
currentListLength = 0 # Length of the list that's currently being processed.
currentListBaseVirtualAddress = None # Base virtual address of the list that's currently being processed.
listVirtualAddressToModify = None # The list element that needs to be modified in order to link the list elements.
potentialNextListVirtualAddress = None # Potential next virtual address from a list.
id_references = [] # Stack of id refs that are being processed
current_id_ref = None # Id ref that's being processed at the moment
terminal = None
top_frame_terminal = None
bottom_frame_terminal = None
#-------------------------------------------------------------

def ide_setup():
    global terminal
    global top_frame_terminal
    global bottom_frame_terminal
    terminal = Tk()
    top_frame_terminal = Frame(terminal)
    bottom_frame_terminal = Frame(terminal)
    screen_width = terminal.winfo_screenwidth()
    screen_height = terminal.winfo_screenheight()
    terminal.configure(bg="#363835")
    terminal.geometry(
        '%dx%d+%d+%d' % (screen_width / 2, screen_height / 2 - 80, screen_width / 2, screen_height / 2))

    top_frame_terminal.pack()
    bottom_frame_terminal.pack(side=BOTTOM)
    bottom_frame_terminal.configure(bg="#363835")

def terminal_print(strprint):
    label = Label(bottom_frame_terminal, text=strprint, anchor='w')
    label.grid(sticky=E)
    label.configure(bg="#363835")
    label.configure(fg="white")
    label.pack()

def p_program(p):
    '''
    program : PROGRAM ID create_global_fun COLON VAR_BLOCK update_global_fun generate_go_to_main_quad print_currentSymTab SOLS COLON SOL_DEFINITIONS MAIN_DEFINITION update_constant_number free_symbol_table print_funDir
    '''

def p_generate_go_to_main_quad(p):
    '''
    generate_go_to_main_quad :
    '''
    PJumps.append(quadQueue.count())
    quadQueue.add('GOSUB', 'main', None, None)

def p_update_go_to_main_quad(p):
    '''
    update_go_to_main_quad :
    '''
    quad_to_modify = PJumps.pop()
    quadQueue.append_jump(quad_to_modify, funDir.search('main')[6])

def p_print_funDir(p):
    '''
    print_funDir :
    '''
    print(funDir)

def p_free_symbol_table(p):
    '''
    free_symbol_table :
    '''
    global currentSol
    funDir.search(currentSol)[2].clear()

def p_update_constant_number(p):
    '''
    update_constant_number :
    '''
    global numConstUsed
    global programID
    funDir.update_number_of_constants(programID, numConstUsed)
    numConstUsed = [0, 0, 0, 0, 0]

def p_create_global_fun(p):
    '''
    create_global_fun :
    '''
    global currentSymTab
    global currentSol
    global programID
    currentSymTab = symbolTable()
    funDir.add(p[-1], 6, (), currentSymTab, None, None, None, None)
    programID = p[-1]
    currentSol = p[-1]

def p_update_global_fun(p):
    '''
    update_global_fun :
    '''
    global numGlobalVarsDefined
    global numTempVarsDefined
    global numLocalVarsDefined
    global programID
    funDir.update_number_of_global_variables(programID, numGlobalVarsDefined)
    funDir.update_number_of_temp_variables(programID, numTempVarsDefined)
    numGlobalVarsDefined = [0, 0, 0, 0, 0]
    numTempVarsDefined = [0, 0, 0, 0, 0]
    numLocalVarsDefined = [0, 0, 0, 0, 0]

def p_print_currentSymTab(p):
    '''
    print_currentSymTab :
    '''
    print(currentSymTab)

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
    A : LIST_TYPE_SPECIFICATION ID check_var_duplicates update_local_count B D
    '''

def p_list_type_specification(p):
    '''
    LIST_TYPE_SPECIFICATION : LESS_T LIST_TYPE GREATER_T
    | empty check_for_list_type_specification
    '''

def p_check_for_list_type_specification(p):
    '''
    check_for_list_type_specification :
    '''
    global currentType
    if currentType == 5:
        p_error_missing_list_type_specification(p)

def p_list_type(p):
    '''
    LIST_TYPE : INT
    | FLOAT
    | CHAR
    | STRING
    | BOOL
    '''
    global currentListType
    global currentType
    if currentType == 5:
        if p[1] == 'int':
            currentListType = 0
        elif p[1] == 'float':
            currentListType = 1
        elif p[1] == 'char':
            currentListType = 3
        elif p[1] == 'string':
            currentListType = 2
        elif p[1] == 'bool':
            currentListType = 4
    else:
        p_error_type_mismatch(p)

def p_check_var_duplicates(p):
    '''
    check_var_duplicates :
    '''
    global currentSymTab
    global currentType
    global currentVar
    global currentSol
    global programID
    if currentSymTab.search(p[-1]) is None:
        if currentType != 5:
            if programID == currentSol:
                virtual_address = mainMemory.availGlobals(currentType)
            else:
                virtual_address = executionBlock.availLocal(currentType)
            if virtual_address is None:
                p_error_exceeded_memory_capability(p)
            currentSymTab.add(p[-1], currentType, virtual_address)
        else:
            currentSymTab.add(p[-1], currentType, None)
        currentVar = p[-1]
    else:
        p_error_duplicate_var(p[-1])

def p_update_local_count(p):
    '''
    update_local_count :
    '''
    global currentType
    if currentType != 5:
        numLocalVarsDefined[currentType] = numLocalVarsDefined[currentType] + 1
        numGlobalVarsDefined[currentType] = numGlobalVarsDefined[currentType] + 1

def p_b(p):
    '''
    B : EQUALS C
    | empty check_for_list_assignation
    '''

def p_check_for_list_assignation(p):
    '''
    check_for_list_assignation :
    '''
    global currentType
    if currentType == 5:
        p_error_missing_list_assignation(p)

def p_append_left_operand(p):
    '''
    append_left_operand :
    '''
    global currentSymTab
    global currentType
    global currentVar
    POperands.append(currentSymTab.search(currentVar)[1])
    PTypes.append(currentType)

def p_c(p):
    '''
    C : S_EXPRESSION check_for_list_definition append_equals append_left_operand process_definition_assignation_operation
    | LIST_EXP
    '''

def p_check_for_list_definition(p):
    '''
    check_for_list_definition :
    '''
    global currentType
    if currentType == 5:
        p_error_incorrect_list_definition(p)

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
    SOLUTION_DEF : SOL S_TYPE store_type ID check_sol_duplicates upload_global_return_var L_PAREN PARAMS R_PAREN COLON S_BLOCK check_for_return_statement TICK update_fun print_currentSymTab free_symbol_table reset_execution_block
    '''

def p_upload_global_return_var(p):
    '''
    upload_global_return_var :
    '''
    global currentType
    if currentType != 6:
        global currentSol
        global programID
        global_return_var = ('$' + currentSol + '$')
        virtual_address = mainMemory.availGlobals(currentType)
        if virtual_address is None:
            p_error_exceeded_memory_capability(p)
        funDir.search(programID)[2].add(global_return_var, currentType, virtual_address)
        funDir.add_global_return_var(programID, currentType)

def p_check_for_return_statement(p):
    '''
    check_for_return_statement :
    '''
    global solHasReturn
    if not solHasReturn:
        p_error_no_return_statement_found(p)
    else:
        solHasReturn = False

def p_reset_execution_block(p):
    '''
    reset_execution_block :
    '''
    executionBlock.clear()

def p_check_sol_duplicates(p):
    '''
    check_sol_duplicates :
    '''
    if funDir.search(p[-1]) is None:
        global currentSymTab
        global currentType
        global currentSol
        currentSymTab = symbolTable()
        funDir.add(p[-1], currentType, (), currentSymTab, None, None, None, quadQueue.count())
        currentSol = p[-1]
    else:
        p_error_duplicate_sol(p[-1])

def p_update_fun(p):
    '''
    update_fun :
    '''
    global numParamDefined
    global numLocalVarsDefined
    global numTempVarsDefined
    global currentSol
    funDir.update_number_of_param_variables(currentSol, numParamDefined)
    funDir.update_number_of_local_variables(currentSol, numLocalVarsDefined)
    funDir.update_number_of_temp_variables(currentSol, numTempVarsDefined)
    numParamDefined = [0, 0, 0, 0, 0]
    numLocalVarsDefined = [0, 0, 0, 0, 0]
    numTempVarsDefined = [0, 0, 0, 0, 0]

#-------------------------------------------------------------

def p_statute(p):
    '''
    STATUTE : CONDITION
    | CYCLE
    | ASSIGNATION
    | CON_VAR TICK
    | RETURN_STATEMENT
    '''

#-------------------------------------------------------------

def p_return(p):
    '''
    RETURN_STATEMENT : RETURN S_EXPRESSION TICK check_return_type_correspondence process_return_operation_with_return_value
    | RETURN TICK process_return_operation_without_return_value
    '''

def p_check_return_type_correspondence(p):
    '''
    check_return_type_correspondence :
    '''
    global currentSol
    exp_type = PTypes[len(PTypes) - 1]
    sol_return_type = funDir.search(currentSol)[0]
    if exp_type != sol_return_type:
        p_error_return_type_mismatch(p)

def p_process_return_operation_with_return_value(p):
    '''
    process_return_operation_with_return_value :
    '''
    global solHasReturn
    global currentSol
    global programID
    global_return_var = ('$' + currentSol + '$')
    solHasReturn = True
    PTypes.pop()
    operand = POperands.pop()
    global_return_virtual_address = funDir.search(programID)[2].search(global_return_var)[1]

    quadQueue.add('RETURN', operand, None, global_return_virtual_address)
    quadQueue.add('ENDPROC', None, None, None)

def p_process_return_operation_without_return_value(p):
    '''
    process_return_operation_without_return_value :
    '''
    sol_return_type = funDir.search(currentSol)[0]
    if sol_return_type != 6:
        p_error_return_type_mismatch(p)
    else:
        global solHasReturn
        solHasReturn = True
        quadQueue.add('RETURN', None, None, None)
        quadQueue.add('ENDPROC', None, None, None)

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
            global programID
            global currentSol
            if programID == currentSol:
                virtual_address = mainMemory.availTemporal(result_type)
            else:
                virtual_address = executionBlock.availTemporal(result_type)
            if virtual_address is None:
                p_error_exceeded_memory_capability(p)

            quadQueue.add(operator, left_operand, right_operand, virtual_address)
            POperands.append(virtual_address)
            PTypes.append(result_type)
            numTempVarsDefined[result_type] = numTempVarsDefined[result_type] + 1
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
    EXP : TERM I
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
                global programID
                global currentSol
                if programID == currentSol:
                    virtual_address = mainMemory.availTemporal(result_type)
                else:
                    virtual_address = executionBlock.availTemporal(result_type)
                if virtual_address is None:
                    p_error_exceeded_memory_capability(p)

                quadQueue.add(operator, left_operand, right_operand, virtual_address)
                POperands.append(virtual_address)
                PTypes.append(result_type)
                numTempVarsDefined[result_type] = numTempVarsDefined[result_type] + 1
            else:
                print(str(left_type) + ', ' + operator + ', ' + str(right_type))
                p_error_type_mismatch(p)

def p_i(p):
    '''
    I : J EXP process_possible_plus_minus_operation
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
    TERM : FACTOR K
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
                global programID
                global currentSol
                if programID == currentSol:
                    virtual_address = mainMemory.availTemporal(result_type)
                else:
                    virtual_address = executionBlock.availTemporal(result_type)
                if virtual_address is None:
                    p_error_exceeded_memory_capability(p)

                quadQueue.add(operator, left_operand, right_operand, virtual_address)
                POperands.append(virtual_address)
                PTypes.append(result_type)
                numTempVarsDefined[result_type] = numTempVarsDefined[result_type] + 1
            else:
                print(str(left_type) + ', ' + operator + ', ' + str(right_type))
                p_error_type_mismatch(p)

def p_k(p):
    '''
    K : L TERM process_possible_multiply_divide_operation
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
    FACTOR : L_PAREN push_false_bottom S_EXPRESSION R_PAREN pop_false_bottom
    | CON_VAR
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
    global numConstUsed
    int_r = re.compile(t_INT_CONT)
    string_r = re.compile(t_STRING_CONT)
    char_r = re.compile(t_CHAR_CONT)
    float_r = re.compile(t_FLOAT_CONT)
    value = None
    type = None
    if p[1] == 'true' or p[1] == 'false':
        value = (p[1] == 'true')
        type = 4
        numConstUsed[4] = numConstUsed[4] + 1
    elif float_r.match(p[1]):
        value = float(p[1])
        type = 1
        numConstUsed[1] = numConstUsed[1] + 1
    elif int_r.match(p[1]):
        value = int(p[1])
        type = 0
        numConstUsed[0] = numConstUsed[0] + 1
    elif string_r.match(p[1]):
        value = p[1]
        type = 2
        numConstUsed[2] = numConstUsed[2] + 1
    elif char_r.match(p[1]):
        value = p[1]
        type = 3
        numConstUsed[3] = numConstUsed[3] + 1
    else:
        p_error_unidentified_constant(p)

    if mainMemory.searchConstants(value, type) is None:
        virtual_address = mainMemory.saveConstant(value, type)

        if virtual_address is None:
            p_error_exceeded_memory_capability(p)

        POperands.append(virtual_address)
        PTypes.append(type)
    else:
        POperands.append(mainMemory.searchConstants(value, type))
        PTypes.append(type)

#-------------------------------------------------------------

def p_negation(p):
    '''
    NEGATION : N S_EXPRESSION process_negation_operation
    '''

def p_process_negation_operation(p):
    '''
    process_negation_operation :
    '''
    if len(POperators) > 0:
        operator = POperators[len(POperators) - 1]
        if operator == '!' or operator == 'not':
            operand = POperands.pop()
            type = PTypes.pop()
            operator = POperators.pop()
            result_type = semCube.search((operator, type))

            if not result_type is None:
                global programID
                global currentSol
                if programID == currentSol:
                    virtual_address = mainMemory.availTemporal(result_type)
                else:
                    virtual_address = executionBlock.availTemporal(result_type)
                if virtual_address is None:
                    p_error_exceeded_memory_capability(p)

                quadQueue.add(operator, operand, None, virtual_address)
                POperands.append(virtual_address)
                PTypes.append(result_type)
                numTempVarsDefined[result_type] = numTempVarsDefined[result_type] + 1
            else:
                print(operator + ', ' + str(type))
                p_error_type_mismatch(p)

def p_n(p):
    '''
    N : NOT
    '''
    POperators.append('!')

#-------------------------------------------------------------

def p_ID_ref(p):
    '''
    ID_REF : ID check_var_existence get_var_type O
    '''

def p_check_var_existence(p):
    '''
    check_var_existence :
    '''
    global current_id_ref
    if currentSymTab.search(p[-1]) is None and funDir.search(programID)[2].search(p[-1]) is None:
        p_error_undefined_var(p[-1])
    current_id_ref = idRefInformation()
    current_id_ref.set_name(p[-1])
    id_references.append(current_id_ref)

def p_get_var_type(p):
    '''
    get_var_type :
    '''
    global current_id_ref
    if currentSymTab.search(p[-2]) is None:
        current_id_ref.set_type(funDir.search(programID)[2].search(p[-2])[0])
        current_id_ref.set_is_global(True)
    else:
        current_id_ref.set_type(currentSymTab.search(p[-2])[0])
        current_id_ref.set_is_global(False)

def p_o(p):
    '''
    O : L_BRACK id_ref_check_type_correspondence S_EXPRESSION check_int_type R_BRACK process_list_reference
    | POINT id_ref_check_type_correspondence LENGTH L_PAREN R_PAREN process_list_length_reference
    | POINT id_ref_check_type_correspondence APPEND L_PAREN S_EXPRESSION check_list_append_exp_type R_PAREN process_list_append_reference process_append_assignation_operation
    | POINT id_ref_check_type_correspondence POP L_PAREN R_PAREN process_list_pop_reference
    | empty check_for_list_reference process_var_reference
    '''
    global id_references
    global current_id_ref
    id_references.pop()
    if len(id_references) > 0:
        current_id_ref = id_references[len(id_references) - 1]

def p_process_append_assignation_operation(p):
    '''
    process_append_assignation_operation :
    '''
    if len(POperators) > 0:
        operator = POperators[len(POperators) - 1]
        if operator == '=':
            left_operand = POperands.pop()
            left_type = PTypes.pop()
            right_operand = POperands.pop()
            right_type = PTypes.pop()
            operator = POperators.pop()
            result_type = semCube.search((left_type, operator, right_type))

            if not result_type is None:
                quadQueue.add(operator, right_operand, None, left_operand)
            else:
                print(str(left_type) + ', ' + operator + ', ' + str(right_type))
                p_error_type_mismatch(p)

def p_check_list_append_exp_type(p):
    '''
    check_list_append_exp_type :
    '''
    global current_id_ref
    global currentSol
    global programID

    exp_type = PTypes[len(PTypes) - 1]
    if current_id_ref.get_is_global():
        list_type = funDir.search(programID)[2].search(current_id_ref.get_name())[1].get_type()
    else:
        list_type = funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].get_type()
    if exp_type != list_type:
        p_error_type_mismatch(p)

def p_process_list_append_reference(p):
    '''
    process_list_append_reference :
    '''
    global current_id_ref
    global currentSol
    global programID

    if current_id_ref.get_is_global():
        list_length = funDir.search(programID)[2].search(current_id_ref.get_name())[1].get_length()
        funDir.search(programID)[2].search(current_id_ref.get_name())[1].set_length(list_length + 1)
        list_base_virtual_address = funDir.search(programID)[2].search(current_id_ref.get_name())[1].get_base_virtual_address()
        list_type = funDir.search(programID)[2].search(current_id_ref.get_name())[1].get_type()
        virtual_address = mainMemory.availGlobals(list_type)
        funDir.update_number_of_global_type(programID, list_type)
        if list_length == 0:
            funDir.search(programID)[2].search(current_id_ref.get_name())[1].set_base_virtual_address(virtual_address)
    else:
        list_length = funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].get_length()
        funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].set_length(list_length + 1)
        list_base_virtual_address = funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].get_base_virtual_address()
        list_type = funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].get_type()
        virtual_address = executionBlock.availLocal(list_type)
        numLocalVarsDefined[list_type] = numLocalVarsDefined[list_type] + 1
        if list_length == 0:
            funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].set_base_virtual_address(virtual_address)

    if virtual_address is None:
        p_error_exceeded_memory_capability(p)

    quadQueue.add('APPEND', list_base_virtual_address, list_length, virtual_address)
    POperators.append('=')
    POperands.append(virtual_address)
    PTypes.append(list_type)

def p_process_list_pop_reference(p):
    '''
    process_list_pop_reference :
    '''
    global current_id_ref
    global currentSol
    global programID

    if current_id_ref.get_is_global():
        list_length = funDir.search(programID)[2].search(current_id_ref.get_name())[1].get_length()
        funDir.search(programID)[2].search(current_id_ref.get_name())[1].set_length(list_length - 1)
        list_base_virtual_address = funDir.search(programID)[2].search(current_id_ref.get_name())[1].get_base_virtual_address()
        if list_length == 1:
            funDir.search(programID)[2].search(current_id_ref.get_name())[1].set_base_virtual_address(None)
        list_type = funDir.search(programID)[2].search(current_id_ref.get_name())[1].get_type()
    else:
        list_length = funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].get_length()
        funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].set_length(list_length - 1)
        list_base_virtual_address = funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].get_base_virtual_address()
        if list_length == 1:
            funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].set_base_virtual_address(None)
        list_type = funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].get_type()

    if list_length == 0:
        p_error_nothing_to_pop(p)

    if currentSol == programID:
        virtual_address = mainMemory.availTemporal(list_type)
    else:
        virtual_address = executionBlock.availTemporal(list_type)
    if virtual_address is None:
        p_error_exceeded_memory_capability(p)

    quadQueue.add('POP', list_base_virtual_address, list_length, virtual_address)

    POperands.append(virtual_address)
    PTypes.append(list_type)
    numTempVarsDefined[list_type] = numTempVarsDefined[list_type] + 1

def p_process_list_length_reference(p):
    '''
     process_list_length_reference :
    '''
    global current_id_ref
    global currentSol
    global programID

    if current_id_ref.get_is_global():
        list_length = funDir.search(programID)[2].search(current_id_ref.get_name())[1].get_length()
    else:
        list_length = funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].get_length()

    if currentSol == programID:
        virtual_address = mainMemory.availTemporal(0)
    else:
        virtual_address = executionBlock.availTemporal(0)
    if virtual_address is None:
        p_error_exceeded_memory_capability(p)

    quadQueue.add('LENGTH', list_length, None, virtual_address)

    POperands.append(virtual_address)
    PTypes.append(0)
    numTempVarsDefined[0] = numTempVarsDefined[0] + 1

def p_process_var_reference(p):
    '''
    process_var_reference :
    '''
    global current_id_ref
    global currentSol
    global programID

    if current_id_ref.get_is_global():
        virtual_address = funDir.search(programID)[2].search(current_id_ref.get_name())[1]
    else:
        virtual_address = funDir.search(currentSol)[2].search(current_id_ref.get_name())[1]
    POperands.append(virtual_address)
    PTypes.append(current_id_ref.get_type())

def p_process_list_reference(p):
    '''
    process_list_reference :
    '''
    global current_id_ref
    global currentSol
    global programID

    indexer = POperands.pop()
    PTypes.pop()
    if current_id_ref.get_is_global():
        list_length = funDir.search(programID)[2].search(current_id_ref.get_name())[1].get_length()
        list_base_virtual_address = funDir.search(programID)[2].search(current_id_ref.get_name())[1].get_base_virtual_address()
        list_type = funDir.search(programID)[2].search(current_id_ref.get_name())[1].get_type()
    else:
        list_length = funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].get_length()
        list_base_virtual_address = funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].get_base_virtual_address()
        list_type = funDir.search(currentSol)[2].search(current_id_ref.get_name())[1].get_type()
    quadQueue.add('VERIFY', indexer, 0, list_length)

    if currentSol == programID:
        virtual_address = mainMemory.availTemporal(list_type)
    else:
        virtual_address = executionBlock.availTemporal(list_type)
    if virtual_address is None:
        p_error_exceeded_memory_capability(p)
    quadQueue.add('LOCATE', list_base_virtual_address, indexer, virtual_address)

    POperands.append([virtual_address])
    PTypes.append(list_type)
    numTempVarsDefined[list_type] = numTempVarsDefined[list_type] + 1

def p_check_for_list_reference(p):
    '''
    check_for_list_reference :
    '''
    global current_id_ref
    if current_id_ref.get_type() == 5:
        p_error_incorrect_list_reference(p)

def p_id_ref_check_type_correspondence(p):
    '''
    id_ref_check_type_correspondence :
    '''
    global current_id_ref
    if current_id_ref.get_type() != 5:
        p_error_type_mismatch(p)

def p_check_int_type(p):
    '''
    check_int_type :
    '''
    exp_type = PTypes[len(PTypes) - 1]
    if exp_type != 0:
        p_error_noninteger_indexing(p[-1])

#-------------------------------------------------------------

def p_list_exp(p):
    '''
    LIST_EXP : L_BRACK check_type_correspondence P R_BRACK end_list_processing
    '''

def p_end_list_processing(p):
    '''
    end_list_processing :
    '''
    global potentialNextListVirtualAddress
    global listVirtualAddressToModify
    global currentListBaseVirtualAddress
    global currentListLength
    global currentListInformation
    global currentSymTab
    global currentVar
    global currentListType
    currentListInformation = listInformation()
    currentListInformation.set_type(currentListType)
    currentListInformation.set_base_virtual_address(currentListBaseVirtualAddress)
    currentListInformation.set_length(currentListLength)
    currentSymTab.update_list_information(currentVar, currentListInformation)
    potentialNextListVirtualAddress = None
    listVirtualAddressToModify = None
    currentListBaseVirtualAddress = None
    currentListLength = 0

def p_check_type_correspondence(p):
    '''
    check_type_correspondence :
    '''
    global currentType
    if currentType != 5:
        p_error_type_mismatch(p)

def p_p(p):
    '''
    P : S_EXPRESSION check_list_exp_type_correspondence update_list_local_or_global_count append_equals ask_for_avail process_definition_assignation_operation PP
    | empty
    '''

def p_update_list_local_or_global_count(p):
    '''
    update_list_local_or_global_count :
    '''
    global currentListType
    numLocalVarsDefined[currentListType] = numLocalVarsDefined[currentListType] + 1
    numGlobalVarsDefined[currentListType] = numGlobalVarsDefined[currentListType] + 1

def p_check_list_exp_type_correspondence(p):
    '''
    check_list_exp_type_correspondence :
    '''
    global currentListType
    exp_type = PTypes[len(PTypes) - 1]
    if currentListType != exp_type:
        p_error_type_mismatch(p)

def p_process_definition_assignation_operation(p):
    '''
    process_definition_assignation_operation :
    '''
    global potentialNextListVirtualAddress
    if len(POperators) > 0:
        operator = POperators[len(POperators) - 1]
        if operator == '=':
            left_operand = POperands.pop()
            potentialNextListVirtualAddress = left_operand
            left_type = PTypes.pop()
            right_operand = POperands.pop()
            right_type = PTypes.pop()
            operator = POperators.pop()
            result_type = semCube.search((left_type, operator, right_type))

            if not result_type is None:
                quadQueue.add(operator, right_operand, None, left_operand)
            else:
                print(str(left_type) + ', ' + operator + ', ' + str(right_type))
                p_error_type_mismatch(p)

def p_ask_for_avail(p):
    '''
    ask_for_avail :
    '''
    global currentSol
    global programID
    global listVirtualAddressToModify
    global currentListBaseVirtualAddress
    global currentListLength
    exp_type = PTypes[len(PTypes) - 1]
    if currentSol == programID:
        virtual_address = mainMemory.availGlobals(exp_type)
    else:
        virtual_address = executionBlock.availLocal(exp_type)
    if virtual_address is None:
        p_error_exceeded_memory_capability(p)
    POperands.append(virtual_address)
    PTypes.append(exp_type)
    currentListLength = currentListLength + 1
    if listVirtualAddressToModify is None:
        listVirtualAddressToModify = virtual_address
    if currentListBaseVirtualAddress is None:
        currentListBaseVirtualAddress = virtual_address

def p_pp(p):
    '''
    PP : COMMA S_EXPRESSION check_list_exp_type_correspondence update_list_local_or_global_count append_equals ask_for_avail process_definition_assignation_operation process_next_element PP
    | empty
    '''

def p_process_next_element(p):
    '''
    process_next_element :
    '''
    global listVirtualAddressToModify
    global potentialNextListVirtualAddress
    quadQueue.add('SET_NEXT', potentialNextListVirtualAddress, None, listVirtualAddressToModify)
    listVirtualAddressToModify = potentialNextListVirtualAddress

#-------------------------------------------------------------

def p_assignation(p):
    '''
    ASSIGNATION : ID_REF EQUALS append_equals S_EXPRESSION process_assignation_operation TICK
    '''

def p_append_equals(p):
    '''
    append_equals :
    '''
    POperators.append('=')

def p_process_assignation_operation(p):
    '''
    process_assignation_operation :
    '''
    if len(POperators) > 0:
        operator = POperators[len(POperators) - 1]
        if operator == '=':
            right_operand = POperands.pop()
            right_type = PTypes.pop()
            left_operand = POperands.pop()
            left_type = PTypes.pop()
            operator = POperators.pop()
            result_type = semCube.search((left_type, operator, right_type))

            if not result_type is None:
                quadQueue.add(operator, right_operand, None, left_operand)
            else:
                print(str(left_type) + ', ' + operator + ', ' + str(right_type))
                p_error_type_mismatch(p)

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
    S_ASSIGNATION : ID_REF EQUALS append_equals S_EXPRESSION process_assignation_operation
    '''

#-------------------------------------------------------------

def p_while(p):
    '''
    WHILE : WHILE_CYCLE append_jump S_EXPRESSION process_condition_operation COLON BLOCK end_while_operation_processing TICK
    '''

def p_append_jump(p):
    '''
    append_jump :
    '''
    PJumps.append(quadQueue.count())

def p_end_while_operation_processing(p):
    '''
    end_while_operation_processing :
    '''
    quad_to_modify = PJumps.pop()
    quad_to_jump_to = PJumps.pop()
    quadQueue.add('GOTO', None, None, quad_to_jump_to)
    quadQueue.append_jump(quad_to_modify, quadQueue.count())

#-------------------------------------------------------------

def p_for(p):
    '''
    FOR : FOR_CYCLE S_ASSIGNATION TICK append_jump S_EXPRESSION process_for_condition_operation TICK S_ASSIGNATION process_for_assignation_operation COLON BLOCK end_for_operation_processing TICK
    '''

def p_process_for_condition_operation(p):
    '''
    process_for_condition_operation :
    '''
    exp_type = PTypes.pop()
    if exp_type == 4:
        operand = POperands.pop()
        PJumps.append(quadQueue.count())
        quadQueue.add('GOTOF', operand, None, None)
        PJumps.append(quadQueue.count())
        quadQueue.add('GOTO', None, None, None)
        PJumps.append(quadQueue.count())
    else:
        p_error_condition_type_mismatch(p)

def p_process_for_assignation_operation(p):
    '''
    process_for_assignation_operation :
    '''
    PJumps.append(quadQueue.count())
    quadQueue.add('GOTO', None, None, None)
    PJumps.append(quadQueue.count())

def p_end_for_operation_processing(p):
    '''
    end_for_operation_processing :
    '''
    jumps = []
    for x in range(0, 6):
        jumps.insert(0, PJumps.pop())

    quadQueue.add('GOTO', None, None, jumps[3])
    quadQueue.append_jump(jumps[4], jumps[0])
    quadQueue.append_jump(jumps[2], jumps[5])
    quadQueue.append_jump(jumps[1], quadQueue.count())

#-------------------------------------------------------------

def p_cycle(p):
    '''
    CYCLE : FOR
    | WHILE
    '''

#-------------------------------------------------------------

def p_condition(p):
    '''
    CONDITION : IF append_false_bottom S_EXPRESSION process_condition_operation COLON BLOCK R TICK end_condition_operation_processing
    '''

def p_end_condition_operation_processing(p):
    '''
    end_condition_operation_processing :
    '''
    while PJumps[len(PJumps) - 1] != 'false_bottom':
        quad_to_modify = PJumps.pop()
        quadQueue.append_jump(quad_to_modify, quadQueue.count())

    PJumps.pop()

def p_append_false_bottom(p):
    '''
    append_false_bottom :
    '''
    PJumps.append('false_bottom')

def p_process_condition_operation(p):
    '''
    process_condition_operation :
    '''
    exp_type = PTypes.pop()
    if exp_type == 4:
        operand = POperands.pop()
        PJumps.append(quadQueue.count())
        quadQueue.add('GOTOF', operand, None, None)
    else:
        p_error_condition_type_mismatch(p)

def p_r(p):
    '''
    R : S
    | T
    | empty
    '''

def p_s(p):
    '''
    S : ELIF process_elif_operation S_EXPRESSION process_condition_operation COLON BLOCK U
    '''

def p_process_elif_operation(p):
    '''
    process_elif_operation :
    '''
    quad_to_modify = PJumps.pop()
    PJumps.append(quadQueue.count())
    quadQueue.add('GOTO', None, None, None)
    quadQueue.append_jump(quad_to_modify, quadQueue.count())

def p_u(p):
    '''
    U : S
    | T
    | empty
    '''

def p_t(p):
    '''
    T : ELSE process_else_operation COLON BLOCK end_else_operation_processing
    '''

def p_process_else_operation(p):
    '''
    process_else_operation :
    '''
    quad_to_modify = PJumps.pop()
    PJumps.append(quadQueue.count())
    quadQueue.add('GOTO', None, None, None)
    quadQueue.append_jump(quad_to_modify, quadQueue.count())

def p_end_else_operation_processing(p):
    '''
    end_else_operation_processing :
    '''
    quad_to_modify = PJumps.pop()
    quadQueue.append_jump(quad_to_modify, quadQueue.count())

#-------------------------------------------------------------

def p_solution_call(p):
    '''
    SOLUTION_CALL : ID check_sol_existence L_PAREN generate_era_quad V R_PAREN end_argument_processing
    '''

def p_end_argument_processing(p):
    '''
    end_argument_processing :
    '''
    global param_counter
    global solution_name
    global executionBlock
    global programID
    if param_counter == (len(funDir.search(solution_name)[1])):
        quadQueue.add('GOSUB', solution_name, None, funDir.search(solution_name)[6])
        sol_return_type = funDir.search(solution_name)[0]
        if sol_return_type != 6:
            temporal_virtual_address = executionBlock.availTemporal(sol_return_type)
            if temporal_virtual_address is None:
                p_error_exceeded_memory_capability(p)
            POperands.append(temporal_virtual_address)
            PTypes.append(sol_return_type)
            global_return_var = ('$' + solution_name + '$')
            quadQueue.add('=', funDir.search(programID)[2].search(global_return_var)[1], None, temporal_virtual_address)
            numTempVarsDefined[funDir.search(solution_name)[0]] = numTempVarsDefined[funDir.search(solution_name)[0]]\
                                                                  + 1
        param_counter = -1
    else:
        p_error_less_parameters_than_expected(p)

def p_generate_era_quad(p):
    '''
    generate_era_quad :
    '''
    quadQueue.add('ERA', p[-3], None, None)
    global param_counter
    param_counter = param_counter + 1

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
        global solution_name
        solution_name = p[-1]

def p_v(p):
    '''
    V : S_EXPRESSION process_argument X
    | empty
    '''

def p_process_argument(p):
    '''
    process_argument :
    '''
    print('hey!')
    argument = POperands.pop()
    argument_type = PTypes.pop()
    global solution_name
    global param_counter
    if param_counter < len(funDir.search(solution_name)[1]):
        if argument_type == funDir.search(solution_name)[1][param_counter]:
            quadQueue.add('PARAMETER', argument, None, param_counter + 1)
            param_counter = param_counter + 1
        else:
            p_error_argument_type_mismatch(p)
    else:
        p_error_more_parameters_than_expected(p)


def p_x(p):
    '''
    X : COMMA V
    | empty
    '''

#-------------------------------------------------------------

def p_s_expression(p):
    '''
    S_EXPRESSION : EXPRESSION
    | NEGATION
    '''

#-------------------------------------------------------------

def p_params(p):
    '''
    PARAMS : TYPE store_type ID check_param_duplicates update_param_count Y
    | empty
    '''

def p_check_param_duplicates(p):
    '''
    check_param_duplicates :
    '''
    global currentSymTab
    global currentType
    global currentSol
    if currentSymTab.search(p[-1]) is None:
        virtual_address = executionBlock.availParameters(currentType)
        if virtual_address is None:
            p_error_exceeded_memory_capability(p)
        currentSymTab.add(p[-1], currentType, virtual_address)
        funDir.append_parameter(currentSol, currentType)
    else:
        p_error_duplicate_param(p[-1])

def p_update_param_count(p):
    '''
    update_param_count :
    '''
    global currentType
    numParamDefined[currentType] = numParamDefined[currentType] + 1

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
    MAIN_DEFINITION : INT store_type MAIN_R check_sol_duplicates upload_global_return_var L_PAREN R_PAREN COLON S_BLOCK check_for_return_statement TICK update_fun print_currentSymTab free_symbol_table reset_execution_block update_go_to_main_quad
    '''
    global programID
    print("******************************************************************")
    virMachine = virtualMachine(quadQueue, mainMemory, funDir, programID)
    print("******************************************************************")

#-------------------------------------------------------------

def p_draw_circle(p):
    '''
    DRAW_CIRCLE : DRAW_CIRCLE_R generate_predefined_sol_quad L_PAREN S_EXPRESSION process_draw_argument COMMA S_EXPRESSION process_draw_argument COMMA S_EXPRESSION process_draw_argument R_PAREN end_draw_argument_processing generate_exec_draw_circle_quad
    '''
    p[0] = 'drawCircle'

def p_generate_exec_draw_circle_quad(p):
    '''
    generate_exec_draw_circle_quad :
    '''
    quadQueue.add('EXEC', 'DRAW_CIRCLE', None, None)

#-------------------------------------------------------------

def p_draw_line(p):
    '''
    DRAW_LINE : DRAW_LINE_R generate_predefined_sol_quad L_PAREN S_EXPRESSION process_draw_argument COMMA S_EXPRESSION process_draw_argument COMMA S_EXPRESSION process_draw_argument COMMA S_EXPRESSION process_draw_argument R_PAREN end_draw_argument_processing generate_exec_draw_line_quad
    '''
    p[0] = 'drawLine'

def p_generate_exec_draw_line_quad(p):
    '''
    generate_exec_draw_line_quad :
    '''
    quadQueue.add('EXEC', 'DRAW_LINE', None, None)

#-------------------------------------------------------------

def p_draw_rectangle(p):
    '''
    DRAW_RECTANGLE : DRAW_RECTANGLE_R generate_predefined_sol_quad L_PAREN S_EXPRESSION process_draw_argument COMMA S_EXPRESSION process_draw_argument COMMA S_EXPRESSION process_draw_argument COMMA S_EXPRESSION process_draw_argument R_PAREN end_draw_argument_processing generate_exec_draw_rectangle_quad
    '''
    p[0] = 'drawRectangle'

def p_generate_exec_draw_rectangle_quad(p):
    '''
    generate_exec_draw_rectangle_quad :
    '''
    quadQueue.add('EXEC', 'DRAW_RECTANGLE', None, None)

def p_process_draw_argument(p):
    '''
    process_draw_argument :
    '''
    global param_counter
    param_counter = param_counter + 1
    argument = POperands.pop()
    argument_type = PTypes.pop()
    if argument_type in [0, 1]:
        quadQueue.add('PARAMETER', argument, None, param_counter)
    else:
        p_error_argument_type_mismatch(p)

def p_end_draw_argument_processing(p):
    '''
    end_draw_argument_processing :
    '''
    global param_counter
    param_counter = -1

#-------------------------------------------------------------

def p_move_up(p):
    '''
    MOVE_UP : MOVE_UP_R generate_predefined_sol_quad L_PAREN S_EXPRESSION process_move_argument R_PAREN generate_exec_move_up_quad
    '''
    p[0] = 'moveUp'

def p_generate_exec_move_up_quad(p):
    '''
    generate_exec_move_up_quad :
    '''
    quadQueue.add('EXEC', 'MOVE_UP', None, None)

#-------------------------------------------------------------

def p_move_right(p):
    '''
    MOVE_RIGHT : MOVE_RIGHT_R generate_predefined_sol_quad L_PAREN S_EXPRESSION process_move_argument R_PAREN generate_exec_move_right_quad
    '''
    p[0] = 'moveRight'

def p_generate_exec_move_right_quad(p):
    '''
    generate_exec_move_right_quad :
    '''
    quadQueue.add('EXEC', 'MOVE_RIGHT', None, None)

#-------------------------------------------------------------

def p_move_down(p):
    '''
    MOVE_DOWN : MOVE_DOWN_R generate_predefined_sol_quad L_PAREN S_EXPRESSION process_move_argument R_PAREN generate_exec_move_down_quad
    '''
    p[0] = 'moveDown'

def p_generate_exec_move_down_quad(p):
    '''
    generate_exec_move_down_quad :
    '''
    quadQueue.add('EXEC', 'MOVE_DOWN', None, None)

#-------------------------------------------------------------

def p_move_left(p):
    '''
    MOVE_LEFT : MOVE_LEFT_R generate_predefined_sol_quad L_PAREN S_EXPRESSION process_move_argument R_PAREN generate_exec_move_left_quad
    '''
    p[0] = 'moveLeft'

def p_generate_exec_move_left_quad(p):
    '''
    generate_exec_move_left_quad :
    '''
    quadQueue.add('EXEC', 'MOVE_LEFT', None, None)

def p_process_move_argument(p):
    '''
    process_move_argument :
    '''
    argument = POperands.pop()
    argument_type = PTypes.pop()
    if argument_type in [0, 1]:
        quadQueue.add('PARAMETER', argument, None, 0)
    else:
        p_error_argument_type_mismatch(p)

#-------------------------------------------------------------

def p_print(p):
    '''
    PRINT : PRINT_R generate_predefined_sol_quad L_PAREN S_EXPRESSION process_print_argument R_PAREN generate_exec_print_quad
    '''
    p[0] = 'print'

def p_generate_exec_print_quad(p):
    '''
    generate_exec_print_quad :
    '''
    quadQueue.add('EXEC', 'PRINT', None, None)

def p_process_print_argument(p):
    '''
    process_print_argument :
    '''
    argument = POperands.pop()
    argument_type = PTypes.pop()
    if argument_type in [0, 1, 2, 3, 4]:
        quadQueue.add('PARAMETER', argument, None, 0)
    else:
        p_error_argument_type_mismatch(p)

def p_generate_predefined_sol_quad(p):
    '''
    generate_predefined_sol_quad :
    '''
    if p[-1] == 'print':
        quadQueue.add('PRINT', None, None, None)
    elif p[-1] == 'moveLeft':
        quadQueue.add('MOVE_LEFT', None, None, None)
    elif p[-1] == 'moveRight':
        quadQueue.add('MOVE_RIGHT', None, None, None)
    elif p[-1] == 'moveDown':
        quadQueue.add('MOVE_DOWN', None, None, None)
    elif p[-1] == 'moveUp':
        quadQueue.add('MOVE_UP', None, None, None)
    elif p[-1] == 'drawRectangle':
        quadQueue.add('DRAW_RECTANGLE', None, None, None)
    elif p[-1] == 'drawLine':
        quadQueue.add('DRAW_LINE', None, None, None)
    else:
        quadQueue.add('DRAW_CIRCLE', None, None, None)

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
    ide_setup()
    terminal_print('Error de sintaxis!')
    terminal.mainloop()
    sys.exit()

# Error-handling function for duplicate variables
def p_error_duplicate_var(p):
    '''
    '''
    print('Error!')
    print('Variable ' + p + ' already defined.')
    ide_setup()
    terminal_print('Error!\n' + 'Variable ' + p + ' already defined.')
    terminal.mainloop()
    sys.exit()

# Error-handling function for duplicate parameters
def p_error_duplicate_param(p):
    '''
    '''
    print('Error!')
    print('Parameter ' + p + ' already defined.')
    ide_setup()
    terminal_print('Error!\n' + 'Parameter ' + p + ' already defined.')
    terminal.mainloop()
    sys.exit()

# Error-handling function for duplicate solutions
def p_error_duplicate_sol(p):
    '''
    '''
    print('Error!')
    print('Solution ' + p + ' already defined.')
    ide_setup()
    terminal_print('Error!\n' + 'Solution ' + p + ' already defined.')
    terminal.mainloop()
    sys.exit()

# Error-handling function for undefined variables
def p_error_undefined_var(p):
    '''
    '''
    print('Error!')
    print('Variable ' + p + ' is not defined.')
    ide_setup()
    terminal_print('Error!\n' + 'Variable ' + p + ' is not defined.')
    terminal.mainloop()
    sys.exit()

# Error-handling function for noninteger indexing
def p_error_noninteger_indexing(p):
    '''
    '''
    print('Error!')
    print('Trying to index a list using a non-integer value.')
    ide_setup()
    terminal_print('Error!\n' + 'Trying to index a list using a non-integer value.')
    terminal.mainloop()
    sys.exit()

# Error-handling function for undefined solutions
def p_error_undefined_sol(p):
    '''
    '''
    print('Error!')
    print('Solution ' + p + ' is not defined.')
    ide_setup()
    terminal_print('Error!\n' + 'Solution ' + p + ' is not defined.')
    terminal.mainloop()
    sys.exit()

# Error-handling function for when main solution is called
def p_error_main_not_callable(p):
    '''
    '''
    print('Error!')
    print('Main solution is not a callable solution.')
    ide_setup()
    terminal_print('Error!\n' + 'Main solution is not a callable solution.')
    terminal.mainloop()
    sys.exit()

# Error-handling function for unidentified constants
def p_error_unidentified_constant(p):
    '''
    '''
    print('Error!')
    print('Constant ' + p + ' is not identified.')
    ide_setup()
    terminal_print('Error!\n' + 'Constant ' + p + ' is not identified.')
    terminal.mainloop()
    sys.exit()

# Error-handling function for type mismatch
def p_error_type_mismatch(p):
    '''
    '''
    print('Error!')
    print('Type mismatch!')
    ide_setup()
    terminal_print('Error!\n' + 'Type mismatch!')
    terminal.mainloop()
    sys.exit()

# Error-handling function for condition type mismatch
def p_error_condition_type_mismatch(p):
    '''
    '''
    print('Error!')
    print('Condition type mismatch!')
    ide_setup()
    terminal_print('Error!\n' + 'Condition type mismatch!')
    terminal.mainloop()
    sys.exit()

# Error-handling function for return type mismatch
def p_error_return_type_mismatch(p):
    '''
    '''
    print('Error!')
    print('Return type mismatch!')
    ide_setup()
    terminal_print('Error!\n' + 'Return type mismatch!')
    terminal.mainloop()
    sys.exit()

# Error-handling function for argument type mismatch
def p_error_argument_type_mismatch(p):
    '''
    '''
    print('Error!')
    print('Argument type mismatch!')
    ide_setup()
    terminal_print('Error!\n' + 'Argument type mismatch!')
    terminal.mainloop()
    sys.exit()

# Error-handling function for more parameters than expected in solution call
def p_error_more_parameters_than_expected(p):
    '''
    '''
    print('Error!')
    print('More parameters than expected in solution call!')
    ide_setup()
    terminal_print('Error!\n' + 'More parameters than expected in solution call!')
    terminal.mainloop()
    sys.exit()

# Error-handling function for less parameters than expected in solution call
def p_error_less_parameters_than_expected(p):
    '''
    '''
    print('Error!')
    print('Less parameters than expected in solution call!')
    ide_setup()
    terminal_print('Error!\n' + 'Less parameters than expected in solution call!')
    terminal.mainloop()
    sys.exit()

# Error-handling function for exceeded memory capability
def p_error_exceeded_memory_capability(p):
    '''
    '''
    print('Error!')
    print('Exceeded memory capability!')
    ide_setup()
    terminal_print('Error!\n' + 'Exceeded memory capability!')
    terminal.mainloop()
    sys.exit()

# Error-handling function for no return statement in solution definition
def p_error_no_return_statement_found(p):
    '''
    '''
    print('Error!')
    print('No return statement found in solution definition!')
    ide_setup()
    terminal_print('Error!\n' + 'No return statement found in solution definition!')
    terminal.mainloop()
    sys.exit()

# Error-handling function for missing list type specification
def p_error_missing_list_type_specification(p):
    '''
    '''
    print('Error!')
    print('Missing list type specification!')
    ide_setup()
    terminal_print('Error!\n' + 'Missing list type specification!')
    terminal.mainloop()
    sys.exit()

# Error-handling function for missing list assignation
def p_error_missing_list_assignation(p):
    '''
    '''
    print('Error!')
    print('Missing list assignation!')
    ide_setup()
    terminal_print('Error!\n' + 'Missing list assignation!')
    terminal.mainloop()
    sys.exit()

# Error-handling function for incorrect list definition
def p_error_incorrect_list_definition(p):
    '''
    '''
    print('Error!')
    print('Incorrect list definition!')
    ide_setup()
    terminal_print('Error!\n' + 'Incorrect list definition!')
    terminal.mainloop()
    sys.exit()

# Error-handling function for incorrect list reference
def p_error_incorrect_list_reference(p):
    '''
    '''
    print('Error!')
    print('Incorrect list reference!')
    ide_setup()
    terminal_print('Error!\n' + 'Incorrect list reference!')
    terminal.mainloop()
    sys.exit()

# Error-handling function for attempting to pop an emtpy list
def p_error_nothing_to_pop(p):
    '''
    '''
    print('Error!')
    print('Nothing to pop! List is already empty.')
    ide_setup()
    terminal_print('Error!\n' + 'Nothing to pop! List is already empty.')
    terminal.mainloop()
    sys.exit()

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

with open('testing/code_to_compile_and_execute.txt', 'r') as myfile:
    data = myfile.read()

#with open('../testing/failure_test.txt', 'r') as myfile:
#    data = myfile.read()
result = parser.parse(data, tracking=True)
print(result)