# -*- enconding: utf-8 -*-

# Referencia: http://www.juanjoconti.com.ar/2007/11/02/minilisp-un-ejemplo-de-ply/

import ply.yacc as yacc
from LexerTraducctor import tokens
import LexerTraducctor
import sys

VERBOSE = 1


def p_parrafo(p):
    'parrafo : frases'
    pass


def p_frases_1(p):
    'frases : frases oracion'
  
    pass


def p_frases_2(p):
    'frases : oracion'
    pass

def p_oracion(p):
    '''oracion : SUJETO    VERBOPRESENTE
                         | VERBOPASADO
                         | VERBOFUTURO OBJETO 
                         '''
    pass

"""
    def p_empty(p):
    'empty :'
    pass
"""

def p_error(p):
   
    if VERBOSE:
        if p is not None:
            print("Syntax error at line " + str(p.lexer.lineno) +
                  " Unexpected token  " + str(p.value))
        else:
            print("Syntax error at line: " + str(cminus_lexer.lexer.lineno))
    else:
        raise Exception('syntax', 'error')


parser = yacc.yacc()

if __name__ == '__main__':

    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'Ejemplos/oraciones.c'

    f = open(fin, 'r')
    data = f.read()
    print(data)
    parser.parse(data, tracking=True)
