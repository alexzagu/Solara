# -*- coding: utf-8 -*-
#------------------------------------------------------------
#
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  05/03/17
#------------------------------------------------------------
import ply.yacc as yacc
import sys
from scanner import tokens

#----------------------------------------------------------------

def p_program(p):
  '''
    program: program id COLON VARS COLON DECLARATIONS CORE COLON S_BLOCK
  '''

#----------------------------------------------------------------

def p_declarations(p):
  '''
    declarations: TYPE A TICK E
  '''

def p_a(p):
  '''
    a: id B D
  '''

def p_b(p):
  '''
    b: EQUALS C | empty
  '''

def p_c(p):
  '''
    c: EXPRESSION | LIST_EXP
  '''

def p_d(p):
  '''
    d: COMMA A | empty
  '''

def p_e(p):
  '''
    e: DECLARATIONS | empty
  '''

#----------------------------------------------------------------

def p_s_block(p):
  '''
    s_block: L_BRACE F R_BRACE
  '''

def p_f(p):
  '''
    f: S_STATUTE F | empty
  '''

#----------------------------------------------------------------

def p_s_statute(p):
  '''
    s_statute: SOLUTION_DEF | STATUTE
  '''

#----------------------------------------------------------------

def p_solution_def(p):
  '''
    solution_def: sol S_TYPE id L_PAREN PARAMS R_PAREN COLON BLOCK TICK
  '''

#----------------------------------------------------------------

def p_statute(p):
  '''
    statute: CONDITION | CYCLE | ASSIGNATION
  '''

#----------------------------------------------------------------

def p_s_type(p):
  '''
    s_type: void | TYPE
  '''

#----------------------------------------------------------------

def p_type(p):
  '''
    type: int | float | char | string | bool | list
  '''

#----------------------------------------------------------------

def p_expression(p):
  '''
    expression: EXP G
  '''

def p_g(p):
  '''
    g: H EXP | empty
  '''

def p_h(p):
  '''
    h: LESS_T | GREATER_T | GREATER_T_EQUALS | LESS_T_EQUALS | IS | AND | OR | PERCENTAGE
  '''

#----------------------------------------------------------------

def p_exp(p):
  '''
    exp: TERM I
  '''

def p_i(p):
  '''
    i: J EXP | empty
  '''

def p_j(p):
  '''
    j: PLUS | MINUS
  '''

#----------------------------------------------------------------

def p_term(p):
  '''
    term: FACTOR K
  '''

def p_k(p):
  '''
    k: L TERM | empty
  '''

def p_l(p):
  '''
    l: MULTIPLY | DIVIDE
  '''

#----------------------------------------------------------------

def p_factor(p):
  '''
    factor: L_PAREN EXPRESSION R_PAREN | M CON_VAR
  '''

def p_m(p):
  '''
    m: PLUS | MINUS | empty
  '''

#----------------------------------------------------------------

def p_con_var(p):
  '''
    con_var: ID_REF | INT_CONT | STRING_CONT | CHAR_CONT | FLOAT_CONT | BOOL_CONT | SOLUTION_CALL
  '''

#----------------------------------------------------------------

def p_negation(p):
  '''
    negation: N EXPRESSION
  '''

def p_n(p):
  '''
    n: NOT
  '''

#----------------------------------------------------------------

def p_id_ref(p):
  '''
    id_ref: id O
  '''

def p_o(p):
  '''
    o: L_BRACK EXPRESSION R_BRACK | empty
  '''

#----------------------------------------------------------------

def p_list_exp(p):
  '''
    list_exp: L_BRACK EXPRESSION R_BRACK
  '''

def p_p(p):
  '''
    p: COMMA EXPRESSION P | empty
  '''

#----------------------------------------------------------------

def p_assignation(p):
  '''
    assignation: ID_REF EQUALS EXPRESSION
  '''

#----------------------------------------------------------------

def p_block(p):
  '''
    block: L_BRACE Q R_BRACE
  '''

def p_q(p):
  '''
    q: STATUTE Q | empty
  '''

#----------------------------------------------------------------

def p_s_assignation(p):
  '''
    s_assignation: ID_REF EQUALS EXPRESSION
  '''

#----------------------------------------------------------------

def p_while(p):
  '''
    while: while EXPRESSION COLON BLOCK TICK
  '''

#----------------------------------------------------------------

def p_for(p):
  '''
    for: for S_ASSIGNATION TICK EXPRESSION TICK S_ASSIGNATION COLON BLOCK TICK
  '''

#----------------------------------------------------------------

def p_cycle(p):
  '''
    cycle: FOR | WHILE
  '''

#----------------------------------------------------------------

def p_condition(p):
  '''
    condition: if EXPRESSION COLON BLOCK R TICK
  '''

def p_r(p):
  '''
    r: S | T
  '''

def p_s(p):
  '''
    s: elif EXPRESSION COLON BLOCK U
  '''

def p_u(p):
  '''
    u: S | empty
  '''

def p_t(p):
  '''
    t: else BLOCK
  '''

#----------------------------------------------------------------

def p_solution_call(p):
  '''
    solution_call: id L_PAREN V R_PAREN TICK
  '''

def p_v(p):
  '''
    v: W X
  '''

def p_w(p):
  '''
    w: EXPRESSION | NEGATION
  '''

def p_x(p):
  '''
    x: COMMA V | empty
  '''

#----------------------------------------------------------------

def p_params(p):
  '''
    params: TYPE id Y
  '''

def p_y(p):
  '''
    y: COMMA PARAMS | empty
  '''

#----------------------------------------------------------------

# funcion para manejar errores
def p_error(p):
  print("Error de sintaxis!")

# se contruye el parser
parser = yacc.yacc()

# lista para guardar la lineas de la entrada
lines = []

# se lee linea por linea el contenido de un archivo
# especificado como argumento al momento de correr el programa
for line in sys.stdin:
  stripped = line.strip()
  if not stripped: break
  lines.append(stripped)
# se crea un solo string con los strings en la lista
input = ' '.join(lines)
# se parsea la entrada
print input
result = parser.parse(input)



