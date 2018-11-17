# -*- encondig: utf-8 -*-

# --------------------------------------
# Lexer Para traducion de ingles a español
# --------------------------------------

import ply.lex as lex

# list of tokens
tokens = (

    #Pronombres Personales
    'SUJETO',
    'VERBOPRESENTE',
    'VERBOPASADO',
    'VERBOFUTURO',
    'OBJETO'
    )

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



def t_SUJETO(t):
    r'Yo|Tu|Ella|El|Nosotros|Ustedes|Ellos'
    return t

def t_VERBOPASADO(t):
    r'bailé|canté|jugué|reí|lloré'
    return t

def t_VERBOPRESENTE(t):
    r'bailo|canto|canta|juego|rio|lloro'
    return t

def t_VERBOFUTURO(t):
    r'bailaré|cantaré|jugaré|reiré|lloraré'
    return t
    
def t_OBJETO(t):
    r'salsa|opera|futbol|mucho|solo|bien'
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)

lexer = lex.lex()

# Test 
if __name__ == '__main__':

    # Test
    data = '''
        Yo canto bien
        Ella canta bien
    '''

    # Build lexer and try on
    lexer.input(data)
    test(data, lexer)
