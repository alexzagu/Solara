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
        '''
        Instance variable symbolicDic
        Dictionary that holds all variable information for a specific scope.
        It follows the following format:
        key: name value: [type, virtual_address] or
        key: name value: [type, list_information]
        '''
        print('Initializing symbol table....')
        self.symbolDic = {}

    # stringTo methods

    def __str__(self):
        lines = []
        for k, v in self.symbolDic.iteritems():
            lines.append('key: ' + str(k) + ' value: ' + str(v))
        return '\n'.join(lines)

    def __unicode__(self):
        lines = []
        for k, v in self.symbolDic.iteritems():
            lines.append('key: ' + str(k) + ' value: ' + str(v))
        return '\n'.join(lines)

    # Method definitions

    # Add method
    def add(self, name, type, virtual_address_or_object):
        self.symbolDic[name] = [type, virtual_address_or_object]

    # Search method
    def search(self, name):
        if name in self.symbolDic:
            return self.symbolDic[name]
        else:
            return None

    # Update list information
    def update_list_information(self, name, list_information):
        self.symbolDic[name][1] = list_information

    # Delete method
    def clear(self):
        self.symbolDic.clear()