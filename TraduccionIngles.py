import ParserTraductorI_E
import LexerTraductorI_E
import sys
from LexerTraductorI_E import *


SUJETO_PRIMERA_PERSONA = {'I': 'Yo', 'we': 'nosotro(a)s'}
SUJETO_SEGUNDA_PERSONA = {'you': 'tu', 'they': 'ellos'}
SUJETO_TERCERA_PERSONA = {'she': 'ella', 'he': 'él', 'it': 'eso'}

SUJETO = [SUJETO_PRIMERA_PERSONA,
          SUJETO_SEGUNDA_PERSONA, SUJETO_TERCERA_PERSONA]

VERBO = {'sing': 'cantar', 'cry': 'llorar'}

EQUIVALENCIAS = {'have': 'had', 'sing': 'sang', 'dance': 'danced', 'cry':'cried', 'wake':'waked'}

VERBO_PRESENTE = {'sing': {'I': 'canto', 'you': 'cantas', 'she':'canta','he':'canta', 'it':'canta','we': 'cantamos', 'they': 'cantan'},
                  'dance': {'I': 'bailo', 'you': 'bailas', 'she':'baila','he':'baila', 'it':'baila', 'we': 'bailamos', 'they': 'bailan'},
                  'cry': {'I': 'lloro', 'you': 'lloras', 'she':'llora', 'he':'llora', 'it':'llora','we': 'lloramos', 'they': 'lloran'},
                  'wake': {'I': 'despierto', 'you': 'despiertas', 'she':'despierta', 'he':'despierta', 'it':'despierta','we': 'despertamos', 'they': 'despiertan'},
                  'have': {'I': 'tengo', 'you': 'tienes', 'she':'tiene', 'he':'tiene', 'it':'tiene','we': 'tenemos', 'they': 'tienen'}

                  }

AUXILIAR_DO = {'do': ''}

AUXILIAR_DO_PASADO = {'did':''}

DO_TERCERA_PERSONA = {'does': ''}

AUXILIAR_PREGUNTA = {'why': 'por qué', 'how': 'cómo',
    'when': 'cuando', 'where': 'donde'}

INTERROGACION = {'?': '?'}

AUXILIAR_NEGACION = {'not':'no'}

VERBO_PRESENTE_TERCERA_PERSONA = {
    'sings': 'canta', 'dances': 'baila', 'cries': 'llora', 'wakes': 'despierta'}

VERBO_PASADO = {'sang': {'I': 'canté', 'you': 'cantaste', 'she': 'cantó', 'he': 'cantó', 'it': 'cantó', 'we': 'cantamos', 'they': 'cantaron'},
                'danced': {'I': 'bailé', 'you': 'bailaste', 'she': 'bailó', 'he': 'bailó', 'it': 'bailó', 'we': 'bailamos', 'they': 'bailaron'},
                'cried': {'I': 'lloré', 'you': 'lloraste', 'she': 'lloró', 'he': 'lloró', 'it': 'lloró', 'we': 'lloramos', 'they': 'lloraron'},
                'wake': {'I': 'desperté', 'you': 'despertaste', 'she': 'despertó', 'he': 'despertó', 'it': 'despertó', 'we': 'despertamos', 'they': 'despertaron'},
                'had': {'I': 'tenia', 'you': 'tenias', 'she': 'tenia', 'he': 'tenia', 'it': 'tenia', 'we': 'teniamos', 'they': 'tenian'}
                }

OBJETO = {'good': 'bien', 'car':'carro'}

OBJETO_PRONOMBRE = {'me':'mi','you':'ti','him':'él','her':'ella','it':'eso','us':'nosotros', 'them':'ello(a)s'}

CONECTOR = {'while':'mientras', 'and':'y','with':'con', 'a':'un'}

tipo_token = {'SUJETO_PRIMERA_PERSONA': SUJETO_PRIMERA_PERSONA,
              'SUJETO_SEGUNDA_PERSONA': SUJETO_SEGUNDA_PERSONA,
              'SUJETO_TERCERA_PERSONA': SUJETO_TERCERA_PERSONA,
              'VERBO_PRESENTE': VERBO_PRESENTE,
              'VERBO_PRESENTE_TERCERA_PERSONA': VERBO_PRESENTE_TERCERA_PERSONA,
              'VERBO_PASADO': VERBO_PASADO,
              'OBJETO': OBJETO,
              'OBJETO_PRONOMBRE': OBJETO_PRONOMBRE,
              'AUXILIAR_PREGUNTA': AUXILIAR_PREGUNTA,
              'AUXILIAR_DO': AUXILIAR_DO,
              'AUXILIAR_DO_PASADO': AUXILIAR_DO_PASADO,
              'DO_TERCERA_PERSONA': DO_TERCERA_PERSONA,
              'INTERROGACION': INTERROGACION,
              'CONECTOR': CONECTOR,
              'AUXILIAR_NEGACION': AUXILIAR_NEGACION
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
        print('funcion traducirFrase palabra traducida', palabra_traducida)
        frase_traducida = frase_traducida + ' ' + palabra_traducida
    return frase_traducida


ultimo_sujeto = ''
auxiliar_pregunta = False
auxiliar_pasado = False

def traducir(tipo, valor):

  global auxiliar_pregunta
  global tipo_token
  global ultimo_sujeto
  global auxiliar_pasado
  global VERBO_PRESENTE_TERCERA_PERSONA
  global AUXILIAR_DO_PASADO
  global VERBO_PRESENTE
  global VERBO_PASADO
  global EQUIVALENCIAS

  print(tipo)
  print(valor)
  
    
    # auxiliar_pregunta = False

  palabra = ''
  token_clase = tipo_token[tipo]
  palabra = token_clase[valor]
    
  if(tipo == 'AUXILIAR_PREGUNTA'):
    auxiliar_pregunta = True
    print('auxiliar pregunta cambiado a TRUE')

  if(token_clase == AUXILIAR_DO_PASADO):
    auxiliar_pasado = True
    print('auxiliar pasado cambiado a TRUE')

  if(auxiliar_pasado == True and token_clase == VERBO_PRESENTE):
    
    token_clase = VERBO_PASADO  
    equivalecia_presente_pasado = EQUIVALENCIAS[valor]
    valor = equivalecia_presente_pasado
    print('condicional prueba auxiliar_pasado->', auxiliar_pasado, 'tipo->', tipo, 'valor->', valor, '')
    palabra = token_clase[valor]
    auxiliar_pasado = False

  print ('metodo traducir clase de token ', token_clase)
  print(isinstance(palabra,str))
  print('palabra antes del if',palabra)

  if (auxiliar_pregunta == True and (ultimo_sujeto == 'he' or ultimo_sujeto == 'she' or ultimo_sujeto == 'it') and tipo == VERBO_PRESENTE):
    pass

  if((valor == 'I') or (valor == 'you') or (valor == 'he') or (valor == 'she') or (valor == 'it') or (valor == 'we') or (valor == 'they')):
      print('metodo traducir palabra if pronombres',palabra)
      ultimo_sujeto = valor
      return palabra



  elif(isinstance(palabra,dict)):
  # if ((palabra == VERBO_PRESENTE) or (palabra == VERBO_PRESENTE_TERCERA_PERSONA) or (palabra == VERBO_PASADO)):
      if palabra == VERBO_PRESENTE_TERCERA_PERSONA :
        conjugacion = palabra[valor]
      else:
          conjugacion = palabra[ultimo_sujeto]
          print('funcion traducir palabra if Verbos',palabra)
      return conjugacion

  else:
    return palabra
  # return palabra


def traducirAEspaniol(data):

    tokens = test(data, lexer)
    # print (tokens)
    traduccion = ''
    ParserTraductorI_E.VERBOSE = 0

    try:
        ParserTraductorI_E.parser.parse(data, tracking=True)
        # print(data)
        # tokens = test(data)
        # print(tokens)
        traduccion = traducirFrase(tokens)
        print('[ok]')
    except:
        print('[Error de syntaxis]')
        traduccion = 'Error de syntaxis'
    # traduccion = traducirFrase(tokens)
    return traduccion
