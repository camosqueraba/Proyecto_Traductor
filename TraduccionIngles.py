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
              'VERBO_PASADO':VERBO_PASADO,
              'OBJETO':OBJETO
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
        frase_traducida = ' ' + traducir(tipo,valor)
    return frase_traducida

ultimo_sujeto = ''

def traducir(tipo,valor):
	global ultimo_sujeto
	palabra = ''
	token_clase = tipo_token[tipo]
	palabra = token_clase[valor]
	if((palabra == 'I') or (palabra == 'You') or (palabra == 'He') or (palabra == 'She') or (palabra == 'It') or (palabra == 'We') or (palabra == 'They')):
		print(palabra)
		ultimo_sujeto = palabra
		return palabra
	if ((palabra == VERBO_PRESENTE) or (palabra == VERBO_PRESENTE_TERCERA_PERSONA) or (palabra == VERBO_PASADO) ): 
		conjugacion = palabra[ultimo_sujeto]
		print (conjugacion)
		return conjugacion
	
	#return palabra


def traducirAEspaniol(data):

    tokens = test(data, lexer)
    #print (tokens)
    traduccion = ''
    ParserTraductorI_E.VERBOSE = 0

    try:
        ParserTraductorI_E.parser.parse(data, tracking=True)
        #print(data)
        #tokens = test(data)
        #print(tokens)
        #traduccion = traducirFrase(tokens)
        print('[ok]')
    except:
        print('[Error de syntaxis]')
    
    traduccion = traducirFrase(tokens)    
    return traduccion

