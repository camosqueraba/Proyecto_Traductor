import ParserTraductorI_E
from TraduccionIngles import *
# -*- enconding: utf-8 -*-


if __name__ == '__main__':

    data = 'do they sing ?'
    #tests = ['examples/fibonacci.c']

    ParserTraductorI_E.VERBOSE = 0

    '''for test in tests:
        f = open(test, 'r')
        data = f.read()
        print('test: ', test, '..............\t')'''
    #try:
     #   ParserTraductorI_E.parser.parse(data, tracking=True)
    traduccion = traducirAEspaniol(data)
    print(traduccion)
        #print('[ok]')
    #except:
       # print('[Error de syntaxis]')
