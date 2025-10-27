import ply.lex as lex

tokens = ('NUM', 'PA', 'PF', 'SOMA', 'DIV', 'MULT', 'SUB')
          

t_NUM = r'\d+'
t_PA = r'\('
t_PF = r'\)'
t_SOMA = r'\+'
t_DIV = r'/'
t_MULT = r'\*'
t_SUB = r'-'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
t_ignore = '\t '

def t_error(t):
    print('Carácter desconhecido: ', t.value[0], 'Linha: ', t.lexer.lineno)
    t.lexer.skip(1)

lexer = lex.lex()

