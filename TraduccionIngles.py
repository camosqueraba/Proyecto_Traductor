import ParserTraductorI_E
import LexerTraductorI_E
import sys
from LexerTraductorI_E import *


SUJETO_PRIMERA_PERSONA = {'I': 'Yo', 'We': 'nosotro(a)s'}
SUJETO_SEGUNDA_PERSONA = {'You': 'tu'}
SUJETO_TERCERA_PERSONA = {'She': 'Ella', 'He': 'él'}

SUJETO = [SUJETO_PRIMERA_PERSONA,
          SUJETO_SEGUNDA_PERSONA, SUJETO_TERCERA_PERSONA]

VERBO = {'sing': 'cantar', 'cry': 'llorar'}


VERBO_PRESENTE = {'sing': {'I': 'canto', 'You': 'cantas', 'we': 'cantamos', 'they': 'cantan'},
                  'dance': {'I': 'bailo', 'You': 'bailas', 'we': 'bailamos', 'they': 'bailan'},
                  'cry': {'I': 'lloro', 'You': 'lloras', 'we': 'lloramos', 'they': 'lloran'},
                  'wake': {'I': 'despierto', 'You': 'despiertas', 'we': 'despertamos', 'they': 'despiertan'}

                  }

VERBO_PRESENTE_TERCERA_PERSONA = {
    'sing': 'canta', 'dances': 'baila', 'cries': 'llora', 'wakes': 'despierta'}

VERBO_PASADO = {'sang': {'I': 'canté', 'You': 'cantaste', 'she': 'cantó', 'he': 'cantó', 'we': 'cantamos', 'they': 'cantaron'},
                'danced': {'I': 'bailé', 'You': 'bailaste', 'she': 'bailó', 'he': 'bailó', 'we': 'bailamos', 'they': 'bailaron'},
                'cry': {'I': 'lloré', 'You': 'lloraste', 'she': 'lloró', 'he': 'lloró', 'we': 'lloramos', 'they': 'lloraron'},
                'wake': {'I': 'desperté', 'You': 'despertaste', 'she': 'despertó', 'he': 'despertó', 'we': 'despertamos', 'they': 'despertaron'}
                }

OBJETO = {'good': 'bien'}

tipo_token = {'SUJETO_PRIMERA_PERSONA': SUJETO_PRIMERA_PERSONA,
              'SUJETO_SEGUNDA_PERSONA': SUJETO_SEGUNDA_PERSONA,
              'SUJETO_TERCERA_PERSONA': SUJETO_TERCERA_PERSONA,
              'VERBO_PRESENTE': VERBO_PRESENTE,
              'VERBO_PRESENTE_TERCERA_PERSONA': VERBO_PRESENTE_TERCERA_PERSONA,
              'VERBO_PASADO': VERBO_PASADO,
              'OBJETO': OBJETO
              }


AUXILIAR_FUTURO = {}

OBJETO_PRONOMBRE = {}

VERBO_PRESENTE_BE_1 = {}
VERBO_PRESENTE_BE_2 = {}
VERBO_PRESENTE_BE_3 = {}

INTERROGACION = {}


def traducirFrase(frase):
    frase_traducida = ''
    for palabra in frase:
        tipo = palabra.type
        valor = palabra.value
        palabra_traducida = traducir(tipo, valor)
        print('funcion traducirFrase palabra traducida',palabra_traducida)
        frase_traducida = frase_traducida+' ' + palabra_traducida
    return frase_traducida


ultimo_sujeto = ''


def traducir(tipo, valor):
    print(tipo)
    print(valor)
    global tipo_token
    global ultimo_sujeto
    palabra = ''
    token_clase = tipo_token[tipo]
    palabra = token_clase[valor]
    print ('metodo traducir clase de token ',token_clase )
    print(isinstance(palabra,str))
    print('palabra antes del if',palabra)
    if((valor == 'I') or (valor == 'You') or (valor == 'He') or (valor == 'She') or (valor == 'It') or (valor == 'We') or (valor == 'They')):
        print('metodo traducir palabra if pronombres',palabra)
        ultimo_sujeto = valor
        return palabra
    elif(isinstance(palabra,dict)):
    #if ((palabra == VERBO_PRESENTE) or (palabra == VERBO_PRESENTE_TERCERA_PERSONA) or (palabra == VERBO_PASADO)):
        conjugacion = palabra[ultimo_sujeto]
        print('funcion traducir palabra if Verbos',palabra)
        return conjugacion
    else:
    	return palabra
    # return palabra


def traducirAEspaniol(data):

    tokens = test(data, lexer)
    #print (tokens)
    traduccion = ''
    ParserTraductorI_E.VERBOSE = 0

    try:
        ParserTraductorI_E.parser.parse(data, tracking=True)
        # print(data)
        #tokens = test(data)
        # print(tokens)
        traduccion = traducirFrase(tokens)
        print('[ok]')
    except:
        print('[Error de syntaxis]')
        traduccion = 'Error de syntaxis'
    #traduccion = traducirFrase(tokens)
    return traduccion
