# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  11/03/17
# ------------------------------------------------------------

#-------------------------------------------------------------

class semanticCube:

    # Constructor
    def __init__(self):
        print('Initializing semantic cube....')

    # Class variable
    # Dictionary that holds all information about type matching
    # It follows the following format:
    # key: (left_type, operator, right_type) value: type or
    # key: (operator, type) value: type
    semanticDic = {
        # Integers
        (0, '+', 0) : 0,
        (0, '-', 0): 0,
        (0, '*', 0): 0,
        (0, '/', 0): 0,
        (0, '%', 0): 0,
        (0, 'mod', 0): 1,
        (0, 'is', 0): 4,
        (0, '==', 0): 4,
        (0, '<=', 0): 4,
        (0, '>=', 0): 4,
        (0, '<', 0): 4,
        (0, '>', 0): 4,
        # Floats
        (1, '+', 1): 1,
        (1, '-', 1): 1,
        (1, '*', 1): 1,
        (1, '/', 1): 1,
        (1, '%', 1): 1,
        (1, 'mod', 1): 1,
        (1, 'is', 1): 4,
        (1, '==', 1): 4,
        (1, '<=', 1): 4,
        (1, '>=', 1): 4,
        (1, '<', 1): 4,
        (1, '>', 1): 4,
        # Strings
        (2, '+', 2): 2,
        (2, 'is', 2): 4,
        (2, '==', 2): 4,
        (2, '<=', 2): 4,
        (2, '>=', 2): 4,
        (2, '<', 2): 4,
        (2, '>', 2): 4,
        # Characters
        (3, 'is', 3): 4,
        (3, '==', 3): 4,
        (3, '<=', 3): 4,
        (3, '>=', 3): 4,
        (3, '<', 3): 4,
        (3, '>', 3): 4,
        # Booleans
        (4, 'and', 4): 4,
        (4, '&&', 4): 4,
        (4, 'or', 4): 4,
        (4, '||', 4): 4,
        ('not', 4): 4,
        ('!', 4): 4,
        (4, 'is', 4): 4,
        (4, '==', 4): 4,
        # Lists
        (5, '+', 5): 5,
        (5, 'is', 5): 4,
        (5, '==', 5): 4,
        # Mixtures
        # (0, '+', 1): 1,
        # (0, '-', 1): 1,
        # (1, '+', 0): 1,
        # (1, '-', 0): 1,
        # (0, '*', 1): 1,
        # (0, '/', 1): 1,
        # (1, '*', 0): 1,
        # (1, '/', 0): 1,
        # (0, '%', 1): 1,
        # (0, 'mod', 1): 1,
        # (0, '<=', 1): 4,
        # (0, '>=', 1): 4,
        # (0, '<', 1): 4,
        # (0, '>', 1): 4,
        # (0, 'is', 1): 4,
        # (0, '==', 1): 4,
        # (1, '%', 0): 1,
        # (1, 'mod', 0): 1,
        # (1, '<=', 0): 4,
        # (1, '>=', 0): 4,
        # (1, '<', 0): 4,
        # (1, '>', 0): 4,
        # (1, 'is', 0): 4,
        # (1, '==', 0): 4,
        (0, '=', 0): 0,
        #(0, '=', 1): 0,
        (1, '=', 1): 1,
        #(1, '=', 0): 1,
        (2, '=', 2): 2,
        (3, '=', 3): 3,
        (4, '=', 4): 4,
        (5, '=', 5): 5,
    }

    # stringTo methods

    def __str__(self):
        lines = []
        for k, v in self.semanticDic.iteritems():
            lines.append('key: ' + str(k) + ' value: ' + str(v))
        return '\n'.join(lines)

    def __unicode__(self):
        lines = []
        for k, v in self.semanticDic.iteritems():
            lines.append('key: ' + str(k) + ' value: ' + str(v))
        return '\n'.join(lines)

    # Method definitions

    # Search method
    def search(self, tuple):
        if tuple in self.semanticDic:
            return self.semanticDic[tuple]
        else:
            return None