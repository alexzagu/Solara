# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  05/03/17
# ------------------------------------------------------------

from structures.memory_unit import memoryUnit

class memoryBlock:

    # Constructor
    def __init__(self):
        print('Initializing memory block....')
        self.countInt = 0
        self.countFloat = 0
        self.countString = 0
        self.countBool = 0
        self.countChar = 0
        self.memBlock = [[], [], [], [], []]

    # Class variables

    # Initializing ranges

    intMAX = 4999
    floatMAX = 9999
    stringMAX = 14999
    charMAX = 19999
    boolMAX = 24999

    intMIN = 0
    floatMIN = 5000
    stringMIN = 10000
    charMIN = 15000
    boolMIN = 20000

    # Trash values for default assignation
    trash_values = [0, 0.0, "", '', False]

    # stringTo methods

    def __str__(self):
        lines = []
        lines.append('[')
        for range in self.memBlock:
            lines.append('  [')
            for unit in range:
                lines.append('      ' + str(unit))
            lines.append('  ]')
        lines.append(']')
        return '\n'.join(lines)

    def __unicode__(self):
        lines = []
        lines.append('[')
        for range in self.memBlock:
            lines.append('  [')
            for unit in range:
                lines.append('      ' + str(unit))
            lines.append('  ]')
        lines.append(']')
        return '\n'.join(lines)

    # Method definitions

    # Save method
    def save(self, value, type, next):
        tempMemUnit = memoryUnit()
        if value is None:
            tempMemUnit.set_value(self.trash_values[type])
        else:
            tempMemUnit.set_value(value)
        tempMemUnit.set_next(next)

        if type == 0 and self.countInt <= self.intMAX:
            self.memBlock[0].append(tempMemUnit)
            self.countInt += 1
            return self.intMIN + (self.countInt - 1)

        elif type == 1 and self.countFloat <= self.floatMAX:
            self.memBlock[1].append(tempMemUnit)
            self.countFloat += 1
            return self.floatMIN + (self.countFloat - 1)

        elif type == 2 and self.countString <= self.stringMAX:
            self.memBlock[2].append(tempMemUnit)
            self.countString += 1
            return self.stringMIN + (self.countString - 1)

        elif type == 3 and self.countChar <= self.charMAX:
            self.memBlock[3].append(tempMemUnit)
            self.countChar += 1
            return self.charMIN + (self.countChar - 1)

        elif type == 4 and self.countBool <= self.boolMAX:
            self.memBlock[4].append(tempMemUnit)
            self.countBool += 1
            return self.boolMIN + (self.countBool - 1)

        else:
            return None

    # Get value method
    def get_value(self, virtual_address):
        if virtual_address >= self.intMIN and virtual_address <= self.intMAX:
            return self.memBlock[0][virtual_address].get_value()

        elif virtual_address >= self.floatMIN and virtual_address <= self.floatMAX:
            return self.memBlock[1][virtual_address - self.floatMIN].get_value()

        elif virtual_address >= self.stringMIN and virtual_address <= self.stringMAX:
            return self.memBlock[2][virtual_address - self.stringMIN].get_value()

        elif virtual_address >= self.charMIN and virtual_address <= self.charMAX:
            return self.memBlock[3][virtual_address - self.charMIN].get_value()

        elif virtual_address >= self.boolMIN and virtual_address <= self.boolMAX:
            return self.memBlock[4][virtual_address - self.boolMIN].get_value()

        else:
            return None

    # Set value method
    def set_value(self, virtual_address, value):
        if virtual_address >= self.intMIN and virtual_address <= self.intMAX:
            return self.memBlock[0][virtual_address].set_value(value)

        elif virtual_address >= self.floatMIN and virtual_address <= self.floatMAX:
            return self.memBlock[1][virtual_address - self.floatMIN].set_value(value)

        elif virtual_address >= self.stringMIN and virtual_address <= self.stringMAX:
            return self.memBlock[2][virtual_address - self.stringMIN].set_value(value)

        elif virtual_address >= self.charMIN and virtual_address <= self.charMAX:
            return self.memBlock[3][virtual_address - self.charMIN].set_value(value)

        elif virtual_address >= self.boolMIN and virtual_address <= self.boolMAX:
            return self.memBlock[4][virtual_address - self.boolMIN].set_value(value)

        else:
            return None

    # Set next method
    def set_next(self, virtual_address, next_virtual_address):
        if virtual_address >= self.intMIN and virtual_address <= self.intMAX:
            self.memBlock[0][virtual_address].set_next(next_virtual_address)

        elif virtual_address >= self.floatMIN and virtual_address <= self.floatMAX:
            self.memBlock[1][virtual_address - self.floatMIN].set_next(next_virtual_address)

        elif virtual_address >= self.stringMIN and virtual_address <= self.stringMAX:
            self.memBlock[2][virtual_address - self.stringMIN].set_next(next_virtual_address)

        elif virtual_address >= self.charMIN and virtual_address <= self.charMAX:
            self.memBlock[3][virtual_address - self.charMIN].set_next(next_virtual_address)

        elif virtual_address >= self.boolMIN and virtual_address <= self.boolMAX:
            self.memBlock[4][virtual_address - self.boolMIN].set_next(next_virtual_address)

    # Get next method
    def get_next(self, virtual_address):
        if virtual_address >= self.intMIN and virtual_address <= self.intMAX:
            return self.memBlock[0][virtual_address].get_next()

        elif virtual_address >= self.floatMIN and virtual_address <= self.floatMAX:
            return self.memBlock[1][virtual_address - self.floatMIN].get_next()

        elif virtual_address >= self.stringMIN and virtual_address <= self.stringMAX:
            return self.memBlock[2][virtual_address - self.stringMIN].get_next()

        elif virtual_address >= self.charMIN and virtual_address <= self.charMAX:
            return self.memBlock[3][virtual_address - self.charMIN].get_next()

        elif virtual_address >= self.boolMIN and virtual_address <= self.boolMAX:
            return self.memBlock[4][virtual_address - self.boolMIN].get_next()

        else:
            return None

    # AVAIL method
    def avail(self, type):
        if type == 0 and self.countInt <= self.intMAX:
            self.countInt += 1
            return self.intMIN + (self.countInt - 1)

        elif type == 1 and self.countFloat <= self.floatMAX:
            self.countFloat += 1
            return self.floatMIN + (self.countFloat - 1)

        elif type == 2 and self.countString <= self.stringMAX:
            self.countString += 1
            return self.stringMIN + (self.countString - 1)

        elif type == 3 and self.countChar <= self.charMAX:
            self.countChar += 1
            return self.charMIN + (self.countChar - 1)

        elif type == 4 and self.countBool <= self.boolMAX:
            self.countBool += 1
            return self.boolMIN + (self.countBool - 1)

        else:
            return None

    # Search method
    def search(self, value, type):
        if type == 0:
            for index in range(0, len(self.memBlock[0])):
                if self.memBlock[0][index].value == value:
                    return self.intMIN + index
            return None
        elif type == 1:
            for index in range(0, len(self.memBlock[1])):
                if self.memBlock[1][index].value == value:
                    return self.floatMIN + index
            return None
        elif type == 2:
            for index in range(0, len(self.memBlock[2])):
                if self.memBlock[2][index].value == value:
                    return self.stringMIN + index
            return None
        elif type == 3:
            for index in range(0, len(self.memBlock[3])):
                if self.memBlock[3][index].value == value:
                    return self.charMIN + index
            return None
        elif type == 4:
            for index in range(0, len(self.memBlock[4])):
                if self.memBlock[4][index].value == value:
                    return self.boolMIN + index
            return None
        else:
            return None

    # Clear method
    def clear(self):
        self.countInt = 0
        self.countFloat = 0
        self.countString = 0
        self.countChar = 0
        self.countBool = 0
        for range in self.memBlock:
            for unit in range:
                range.remove(unit)