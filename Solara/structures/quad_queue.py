# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  11/03/17
# ------------------------------------------------------------

#-------------------------------------------------------------

class quadQueue:

    # Constructor
    def __init__(self):
        print('Initializing quad queue....')

    # Class variable
    # List that holds all quads generated that symbolize the intermediate code representation of the whole program.
    # It follows the following format:
    # [(operator, left_operand, right_operand, assignable_variable)]
    quadList = []

    # Temporary AVAIL
    availList = []

    # stringTo methods

    def __str__(self):
        lines = []
        for item in self.quadList:
            lines.append(str(item[0]) + ', ' + str(item[1]) + ', ' + str(item[2]) + ', ' + str(item[3]))
        return '\n'.join(lines)

    def __unicode__(self):
        lines = []
        for item in self.quadList:
            lines.append(str(item[0]) + ', ' + str(item[1]) + ', ' + str(item[2]) + ', ' + str(item[3]))
        return '\n'.join(lines)

    # Method definitions

    # Add method
    def add(self, operator, left_operand, right_operand, assignable_variable):
        self.quadList.append((operator, left_operand, right_operand, assignable_variable))

    # Pop method
    def pop(self):
        return self.quadList.pop()

    # Avail method
    def avail(self):
        length = len(self.availList)
        self.availList.append(length)
        return 't' + str(length)
