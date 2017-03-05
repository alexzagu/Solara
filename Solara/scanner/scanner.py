# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  05/03/17
# ------------------------------------------------------------
import ply.lex as lex

tokens = (
    'IF',
    'ELSE',
    'ELIF',
    'WHILE',
    'FOR',
    'INT',
    'FLOAT',
    'CHAR',
    'STRING',
    'BOOL',
    'LIST',
    'L_BRACE',
    'R_BRACE',
    'L_PAREN',
    'R_PAREN',
    'L_BRACK',
    'R_BRACK',
    'COLON',
    'COMMA',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'GREATER_T',
    'LESS_T',
    'GREATER_T_EQUALS',
    'LESS_T_EQUALS',
    'EQUALS',
    'PERCENTAGE',
    'IS',
    'NOT',
    'AND',
    'OR',
    'SIMPLE_Q',
    'ID',
    'INT_CONT',
    'STRING_CONT',
    'CHAR_CONT',
    'FLOAT_CONT',
    'BOOL_CONT'
    'TICK',
    'AT',
    'LAT',
    'RAT',
    'EXP',
    'TERM',
    'CON_VAR',
    'S_TYPE',
    'NEGATION',
    'FACTOR',
    'ID_REF',
    'LIST_EXP',
    'EXPRESSION',
    'ASSIGNATION',
    'DECLARATION',
    'TYPE',
    'BLOCK',
    'ASSIGNATION_ESP',
    'S_BLOCK',
    'CONDITION',
    'CYCLE',
    'SOLUTION_DEF',
    'SOLUTION_CALL',
    'PARAM',
    'PROGRAM',
    'STATUTE',
    'S_STATUTE',
    'DRAW_CIRCLE',
    'DRAW_LINE',
    'DRAW_RECTANGLE',
    'MOVE_UP',
    'MOVE_DOWN',
    'MOVE_RIGHT',
    'MOVE_LEFT',
    'PRINT'
)

#expresiones regulares

t_INT               = r'[0-9]+'
t_FLOAT             = r'[0-9]+\.[0-9]+((E|e)(+|-)?[0-9]+)?'
t_STRING            = r' \’(\’\’|[^\’eo|]*\’'
t_BOOL              = r'true|false'
t_CHAR              = r''
t_AND               = r'and|&&'
t_IS                = r'is|\=='
t_NOT               = r'not|\!'
t_OR                = r'or|\||'
t_AT                = r'\@'
t_LAT               = r'\@*'
t_RAT               = r'\*@'
t_L_BRACE           = r'\{'
t_R_BRACE           = r'\}'
t_L_PAREN           = r'\('
t_R_PAREN           = r'\)'
t_L_BRACK           = r'\['
t_R_BRACK           = r'\]'
t_COLON             = r'\:'
t_COMMA             = r'\,'
t_PLUS              = r'\+'
t_MINUS             = r'\-'
t_MULTIPLY          = r'\*'
t_DIVIDE            = r'\/'
t_GREATER_T         = r'>'
t_LESS_T            = r'\<'
t_GREATER_T_EQUALS  = r'\>='
t_LESS_T_EQUALS     = r'\<='
t_EQUALS            = r'\='
t_PERCENTAGE        = r'\% | mod'
t_SIMPLE_Q          = r'\''


reserved = {
    'if'        :'IF',
    'else'      :'ELSE',
    'elif'      :'ELIF',
    'while'     :'WHILE',
    'for'       :'FOR',
    'program'   :'PROGRAM',
    'print'     :'PRINT',
    'int'       :'INT',
    'float'     :'FLOAT',
    'string'    :'STRING',
    'char'      :'CHAR',
    'bool'      :'BOOL',
    'core'      :'CORE',
    'sol'       :'SOL',
    'and'       :'AND',
    'not'       :'NOT',
    'or'        :'OR',
    'is'        :'IS'
}

t_ignore            = ' \t\r'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r'[a-z](_?[a-zA-Z0-9])*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_error(t):
    print("ERROR: '%s' en linea:'%s'" % (t.value[0], t.lineno))
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
nombre int if else program print int float 5, 5.4
< > <> () "hola muundo" * / = : + - ,{ } , ; ?
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break