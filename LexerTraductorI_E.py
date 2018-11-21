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

    'VERBO',
    'VERBO_PRESENTE',
    'VERBO_PRESENTE_TERCERA_PERSONA',
    'VERBO_PASADO',
    'AUXILIAR_FUTURO',
    'OBJETO',
    'OBJETO_PRONOMBRE',

    'VERBO_PRESENTE_BE_1',
    'VERBO_PRESENTE_BE_2',
    'VERBO_PRESENTE_BE_3',

    'INTERROGACION'

)

t_INTERROGACION = r'\?'


def t_SUJETO_PRIMERA_PERSONA(t):
    r'I|We'
    return t


def t_SUJETO_SEGUNDA_PERSONA(t):
    r'You'
    return t


def t_SUJETO_TERCERA_PERSONA(t):
    r'He|She|It'
    return t


def t_VERBO_PASADO(t):
    r'sang|danced|ran|cried|woke|waked'
    return t


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


def t_VERBO_PRESENTE_TERCERA_PERSONA(t):
    r'dances|sings|runs|cries|wakes'
    return t


def t_VERBO_PRESENTE(t):
    r'dance|sing|run|cry|wake'
    return t


def t_AUXILIAR_FUTURO(t):
    r'will'
    return t


def t_OBJETO(t):
    r'salsa|opera|soccer|alone|good'
    return t


def t_PRONOMBRE_OBJETO(t):
    r'me|you|him|her|it|them'
    return t


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
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok, '1')


lexer = lex.lex()

# Test
if __name__ == '__main__':

    # Test
    data = '''
        I sang good?
        She is good
        He sings good
    '''

    # Build lexer and try on
    lexer.input(data)
    test(data, lexer)
