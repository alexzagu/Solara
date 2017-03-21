# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  11/03/17
# ------------------------------------------------------------

#-------------------------------------------------------------

class functionDirectory:

    # Constructor
    def __init__(self):
        print('Initializing function directory....')

    # Class variable
    # Dictionary that holds all function information for the whole program.
    # It follows the following format:
    # key: name value: [type, (paramType1, paramType2, paramTypeN), symbolTable]
    functionDic = {}

    # stringTo methods

    def __str__(self):
        lines = []
        for k, v in self.functionDic.iteritems():
            lines.append('key: ' + str(k) + ' value: ' + str(v))
        return '\n'.join(lines)

    def __unicode__(self):
        lines = []
        for k, v in self.functionDic.iteritems():
            lines.append('key: ' + str(k) + ' value: ' + str(v))
        return '\n'.join(lines)

    # Method definitions

    # Add method
    def add(self, name, type, parameters, symbolTable):
        self.functionDic[name] = [type, parameters, symbolTable]

    # Search method
    def search(self, name):
        if name in self.functionDic:
            return self.functionDic[name]
        else:
            return None

    # Method to append a new parameter for a specific solution
    def append_parameter(self, name, code):
        self.functionDic[name][1] += (code, )