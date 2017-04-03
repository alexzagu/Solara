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
    # [[operator, left_operand, right_operand, assignable_variable]] or
    # [[operator, right_operand, None, left_operand]] or
    # [[operator, operand, None, jump_to_quad]]
    quadList = []

    # Temporary AVAIL
    availList = []

    # stringTo methods

    def __str__(self):
        lines = []
        count = 0
        for item in self.quadList:
            lines.append(str(count) + ': ' + str(item[0]) + ', ' + str(item[1]) + ', ' + str(item[2]) + ', ' + \
                         str(item[3]))
            count = count + 1
        return '\n'.join(lines)

    def __unicode__(self):
        lines = []
        count = 0
        for item in self.quadList:
            lines.append(str(count) + ': ' + str(item[0]) + ', ' + str(item[1]) + ', ' + str(item[2]) + ', ' + \
                         str(item[3]))
            count = count + 1
        return '\n'.join(lines)

    # Method definitions

    # Add method specified with the format of the first type of quadruple
    def add(self, operator, left_operand, right_operand, assignable_variable):
        self.quadList.append([operator, left_operand, right_operand, assignable_variable])

    # Pop method
    def pop(self):
        return self.quadList.pop()

    # Count method
    def count(self):
        return len(self.quadList)

    # Append jump method
    def append_jump(self, quad_number, jump_number):
        self.quadList[quad_number][3] = jump_number

    # Avail method
    def avail(self):
        length = len(self.availList)
        self.availList.append(length)
        return 't' + str(length)
