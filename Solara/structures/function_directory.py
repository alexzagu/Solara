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