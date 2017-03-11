# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  11/03/17
# ------------------------------------------------------------

#-------------------------------------------------------------

class symbolTable:

    # Constructor
    def __init__(self):
        print('Initializing symbol table....')

    # Class variable
    # Dictionary that holds all variable information for a specific scope.
    # It follows the following format:
    # key: name value: [type, value]
    symbolDic = {}

    # Method definitions

    # Add method
    def add(self, name, type, value):
        self.symbolDic[name] = [type, value]

    # Search method
    def search(self, name):
        if name in self.symbolDic:
            return self.symbolDic[name]
        else:
            return None