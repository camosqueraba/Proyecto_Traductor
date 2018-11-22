# -*- enconding: utf-8 -*-

import ply.yacc as yacc
from LexerTraductorI_E import tokens
import LexerTraductorI_E
import sys
import codecs

VERBOSE = 1


def p_parrafo(p):
    'parrafo : frase'
    pass


def p_frase(p):
    'frase : frase oracion'

    pass


def p_frase_(p):
    '''frase :  palabra
             | oracion'''
    pass


def p_oracion(p):
    '''oracion :    oracion_presente
                |   oracion_pasado
                |   oracion_futuro
                |   oracion_pregunta'''
    pass

def p_oracion_1(p):
    'oracion : sujeto VERBO_PASADO'
    pass


def p_oracion_presente(p):
    '''oracion_presente :   sujeto VERBO_PRESENTE OBJETO
                          | SUJETO_TERCERA_PERSONA VERBO_PRESENTE_TERCERA_PERSONA OBJETO'''
    pass

def p_oracion_presente_1(p):
    '''oracion_presente :   sujeto VERBO_PRESENTE 
                          | SUJETO_TERCERA_PERSONA VERBO_PRESENTE_TERCERA_PERSONA'''
    pass



def p_oracion_pasado(p):
    'oracion_pasado : sujeto VERBO_PASADO OBJETO'
    pass

def p_oracion_pasado_1(p):
    'oracion_pasado : SUJETO_TERCERA_PERSONA VERBO_PASADO'



def p_oracion_futuro(p):
    'oracion_futuro : sujeto AUXILIAR_FUTURO VERBO OBJETO'
    pass

def p_oracion_pregunta(p):
    '''oracion_pregunta :   AUXILIAR_PREGUNTA AUXILIAR_DO sujeto VERBO_PRESENTE INTERROGACION
                         | AUXILIAR_PREGUNTA DO_TERCERA_PERSONA SUJETO_TERCERA_PERSONA VERBO_PRESENTE INTERROGACION
                         | AUXILIAR_DO sujeto VERBO_PRESENTE INTERROGACION '''

def p_palabra(p):
    '''palabra :  SUJETO
                | VERBO_PRESENTE
                | OBJETO '''
    pass

#def p_verbo(p):
#    '''verbo :    VERBO_PRESENTE
#                | VERBO_PASADO
#                | VERBO   '''


def p_sujeto(p):
    '''sujeto :     SUJETO_PRIMERA_PERSONA
                 |  SUJETO_SEGUNDA_PERSONA'''
    pass


def p_sujeto_1(p):
    'sujeto_tercera_persona : SUJETO_TERCERA_PERSONA'
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
            print("Syntax error at line: " +
                  str(LexerTraductorI_E.lexer.lineno))
    else:
        raise Exception('syntax', 'error')


parser = yacc.yacc()

if __name__ == '__main__':

    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'Ejemplos/oraciones.txt'

    f = codecs.open(fin, 'r', "utf-8")
    data = f.read()
    print(data)
    parser.parse(data, tracking=True)
