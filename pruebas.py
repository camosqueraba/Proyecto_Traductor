# -*- enconding: utf-8 -*-

import ParserTraductorI_E
import sys

if __name__ == '__main__':

    tests = ['Ejemplos/oraciones.txt']
    #tests = ['examples/fibonacci.c']
    ParserTraductorI_E.VERBOSE = 0

    for test in tests:
        f = open(test, 'r')
        data = f.read()
        print('test: ', test, '..............\t')
        try:
            ParserTraductor.parser.parse(data, tracking=True)
            print('[ok]')
        except:
            print('[Error de syntaxis]')
