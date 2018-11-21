import ParserTraductorI_E
import LexerTraductorI_E
import sys


def traducirAEspaniol(data):

    palabras = test(data)

    ParserTraductorI_E.VERBOSE = 0

    try:
        ParserTraductorI_E.parser.parse(data, tracking=True)
        palabras = test(data)
        print('[ok]')
    except:
        print('[Error de syntaxis]')
