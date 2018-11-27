# -*- encondig: utf-8 -*-

# --------------------------------------
# Lexer Para traducion de ingles a español
# --------------------------------------

import ply.lex as lex

# list of tokens
tokens = (

    # Pronombres Personales

    'SUJETO_PRIMERA_PERSONA',
    'SUJETO_SEGUNDA_PERSONA',
    'SUJETO_TERCERA_PERSONA',
    'SUJETO',
    'VERBO',
    'OBJETO',
    'VERBO_PRESENTE',
    'VERBO_PRESENTE_TERCERA_PERSONA',
    'VERBO_PASADO',
    'AUXILIAR_FUTURO',
    'AUXILIAR_DO',
    'AUXILIAR_DO_PASADO',
    'DO_TERCERA_PERSONA',
    'AUXILIAR_PREGUNTA',
    'AUXILIAR_NEGACION',
    'OBJETO_PRONOMBRE',
    'VERBO_PRESENTE_BE_1',
    'VERBO_PRESENTE_BE_2',
    'VERBO_PRESENTE_BE_3',
    'INTERROGACION',
    'CONECTOR',
    'ARTICULO'

)

t_INTERROGACION = r'\?'


def t_DO_TERCERA_PERSONA(t):
    r'does'
    return t


def t_AUXILIAR_DO(t):
    r'do'
    return t

def t_AUXILIAR_DO_PASADO(t):
    r'did'
    return t

def t_SUJETO_PRIMERA_PERSONA(t):
    r'I|we'
    return t


def t_SUJETO_SEGUNDA_PERSONA(t):
    r'you|they'
    return t


def t_SUJETO_TERCERA_PERSONA(t):
    r'^he$|she|it'
    return t


def t_SUJETO(t):
    r'I|You|She|He|It|We|They'


def t_VERBO_PASADO(t):
    r'sang|danced|ran|cried|woke|waked|had'
    return t

'''
def t_VERBO_PASADO_BE_1(t):
    r'was'
    return t


def t_VERBO_PASADO_BE_2(t):
    r'were'
    return t


def t_VERBO_PRESENTE_BE_1(t):
    r'am'
    return t


def t_VERBO_PRESENTE_BE_2(t):
    r'are'
    return t


def t_VERBO_PRESENTE_BE_3(t):
    r'is'
    return t
'''

def t_VERBO_PRESENTE_TERCERA_PERSONA(t):
    r'dances|sings|runs|cries|wakes|is'
    return t


def t_VERBO_PRESENTE(t):
    r'dance|sing|run|cry|wake|have|am|are'
    return t


def t_VERBO(t):
    r'dance|sing|run|cry|wake'
    return t


def t_AUXILIAR_FUTURO(t):
    r'will'
    return t


def t_AUXILIAR_NEGACION(t):
    r'not'
    return t

def t_PRESENTE_CONTINUO(t):
    r'going'
    return t

def t_OBJETO(t):
    r'salsa|opera|soccer|alone|good|car'
    return t


def t_OBJETO_PRONOMBRE(t):
    r'me|you|him|her|it|them'
    return t


def t_CONECTOR(t):
    r'a|with|and'
    return t


def t_AUXILIAR_PREGUNTA(t):
    r'why|how|when|where'
    return t

'''
def t_ARTICULO(t):
    r'a|an|the'
    return t
'''
# def t_INTERROGACION():


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)


def test(data, lexer):
    lexer.input(data)
    palabras = []

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok, '1')
        palabras.append(tok)
        #print(tok.value, tok.type)
        # print(tok.type)
    # print(palabras)
    return palabras


lexer = lex.lex()

# Test
if __name__ == '__main__':

    # Test
    data = '''
       I did not have a car
    '''

    # Build lexer and try on
    lexer.input(data)
    test(data, lexer)
