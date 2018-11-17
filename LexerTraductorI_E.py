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
"""
    'YO',
    'TU',
    'EL',
    'ELLA',
    'ESO',
    'ESA',
    'NOSOTROS',
    'USTEDES',
    'ELLOS',
    'ELLAS',
    
    # Verbos
    'BAILAR',
    'CANTAR',
    'JUGAR',
    'REIR',
    'LLORAR',

    # Verbos Conjugados presente
    'BAILO'
    'CANTO',
    'JUEGO',
    'RIO',
    'LLORO',
    
    'BAILAS',
    'CANTAS',
    'JUEGAS',
    'LLORAS',
    'RIES',
    
    'BAILA',
    'CANTA',
    'JUEGA',
    'RIE',
    'LLORA',
    
    'BAILAMOS',
    'CANTAMOS',
    'JUGAMOS',
    'REIMOS',
    'LLORAMOS',

    'BAILAN',
    'CANTAN',
    'JUEGAN',
    'RIEN',
    'LLORAN',

    # Verbos conjugados pasado
    'BAILÉ',
    'CANTÉ',
    'JUGUÉ',
    'REÍ',
    'LLORÉ',

    'BAILASTE',
    'CANTASTE',
    'JUGASTE',
    'REISTE',
    'LLORASTE',

    'BAILÓ',
    'CANTÓ',
    'JUGÓ',
    'RIÓ',
    'LLORÓ',
    
    # LA CONJUGACION DE ESTOS VERBOS EN PASADO ES IGUAL A LA FORMA PRESENTE
    # 'BAILAMOS',
    # 'CANTAMOS',
    # 'JUGAMOS',
    # 'REIMOS',
    # 'LLORAMOS',

    'BAILARON',
    'CANTARON',
    'JUGARON',
    'RIERON',
    'LLORARON',

    #Verbos Conjugados Futuro


    'BAILARÉ'
    'CANTARÉ',
    'JUGARÉ',
    'REIRÉ',
    'LLORARÉ',
    
    'BAILARÁS',
    'CANTARÁS',
    'JUGARÁS',
    'REIRÁS',
    'LLORARÁS',

    'BAILARÁ',
    'CANTARÁ',
    'JUGARÁ',
    'REIRÁ',
    'LLORARÁ',

    'BAILAREMOS',
    'CANTAREMOS',
    'JUGAREMOS',
    'REIREMOS',
    'LLORAREMOS',

    'BAILARÁN',
    'CANTARÁN',
    'JUGARÁN',
    'REIRÁN',
    'LLORARÁN',

    # LA CONJUGACION DE ESTOS VERVOS PARA EL PRONOMBRE USTEDES Y ELLOS ES IGUAL
    # 'BAILARÁN',
    # 'CANTARÁN',
    # 'JUGARÁN',
    # 'REIRÁN',
    # 'LLORARÁN',
"""


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


def t_VERBO_PRESENTE(t):
    r'dance|sing|run|cry|wake'
    return t


def t_VERBO_PRESENTE_TERCERA_PERSONA(t):
    r'dances|sings|runs|cries|wakes'
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


#def t_INTERROGACION():


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
        He sang good
    '''

    # Build lexer and try on
    lexer.input(data)
    test(data, lexer)
