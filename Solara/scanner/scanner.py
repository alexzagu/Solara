# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  05/03/17
# ------------------------------------------------------------
import ply.lex as lex
#-------------------------------------------------------------

# List of tokens.

tokens = (
    'IF',
    'ELSE',
    'ELIF',
    'WHILE_CYCLE',
    'FOR_CYCLE',
    'INT',
    'FLOAT',
    'CHAR',
    'STRING',
    'BOOL',
    'LIST',
    'VOID',
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
    'ID',
    'INT_CONT',
    'STRING_CONT',
    'CHAR_CONT',
    'FLOAT_CONT',
    'BOOL_CONT',
    'TICK',
    'SINGLE_COMMENT',
    'MULTI_COMMENT',
    'PROGRAM',
    'DRAW_CIRCLE_R',
    'DRAW_LINE_R',
    'DRAW_RECTANGLE_R',
    'MOVE_UP_R',
    'MOVE_DOWN_R',
    'MOVE_RIGHT_R',
    'MOVE_LEFT_R',
    'PRINT_R',
    'SOLS',
    'VARS',
    'SOL',
    'MAIN_R',
    'RETURN'
)

# Regular Expressions.

t_INT_CONT              = r'[0-9]+'
t_FLOAT_CONT            = r'[0-9]+\.[0-9]+'
t_STRING_CONT           = r'\"(\\.|[^"])*\"'
t_CHAR_CONT             = r'\'[a-zA-Z0-9]\''
t_AND                   = r'&&'
t_IS                    = r'\=\='
t_NOT                   = r'\!'
t_OR                    = r'\|\|'
t_ignore_SINGLE_COMMENT = r'\@.*'
t_ignore_MULTI_COMMENT  = r'\@\*'
t_L_BRACE               = r'\{'
t_R_BRACE               = r'\}'
t_L_PAREN               = r'\('
t_R_PAREN               = r'\)'
t_L_BRACK               = r'\['
t_R_BRACK               = r'\]'
t_COLON                 = r'\:'
t_COMMA                 = r'\,'
t_PLUS                  = r'\+'
t_MINUS                 = r'\-'
t_MULTIPLY              = r'\*'
t_DIVIDE                = r'\/'
t_GREATER_T             = r'>'
t_LESS_T                = r'\<'
t_GREATER_T_EQUALS      = r'\>\='
t_LESS_T_EQUALS         = r'\<\='
t_EQUALS                = r'\='
t_PERCENTAGE            = r'\%'
t_TICK                  = r'\~'

# Reserved words.

reserved = {
    'if'            :'IF',
    'else'          :'ELSE',
    'elif'          :'ELIF',
    'while'         :'WHILE_CYCLE',
    'for'           :'FOR_CYCLE',
    'program'       :'PROGRAM',
    'print'         :'PRINT_R',
    'int'           :'INT',
    'float'         :'FLOAT',
    'string'        :'STRING',
    'char'          :'CHAR',
    'bool'          :'BOOL',
    'list'          :'LIST',
    'void'          :'VOID',
    'SOLS'          :'SOLS',
    'VARS'          :'VARS',
    'sol'           :'SOL',
    'and'           :'AND',
    'not'           :'NOT',
    'or'            :'OR',
    'is'            :'IS',
    'mod'           :'PERCENTAGE',
    'true'          :'BOOL_CONT',
    'false'         :'BOOL_CONT',
    'drawCircle'    :'DRAW_CIRCLE_R',
    'drawLine'      :'DRAW_LINE_R',
    'drawRectangle' :'DRAW_RECTANGLE_R',
    'moveUp'        :'MOVE_UP_R',
    'moveDown'      :'MOVE_DOWN_R',
    'moveRight'     :'MOVE_RIGHT_R',
    'moveLeft'      :'MOVE_LEFT_R',
    'main'          :'MAIN_R',
    'return'        :'RETURN'
}

t_ignore            = ' \t\r'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r'[a-zA-Z](_?[a-zA-Z0-9])*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_error(t):
    print("ERROR: '%s' en linea:'%s'" % (t.value[0], t.lineno))
    t.lexer.skip(1)

lexer = lex.lex()

with open('../testing/TestSolutionCall.txt', 'r') as myfile:
    data = myfile.read()

#with open('../testing/failure_test.txt', 'r') as myfile:
#    data = myfile.read()

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    #print(tok)