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

    # stringTo methods
    def __str__(self):
        return ""

    def __unicode__(self):
        return ""

    # Method definitions

    # Save method
    def save(self, value, type, next):
        tempMemUnit = memoryUnit()
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

        if self.intMIN <= virtual_address <= self.intMAX:
            return self.memBlock[0][virtual_address].get_value

        elif self.floatMIN <= virtual_address <= self.floatMAX:
            return self.memBlock[1][virtual_address - self.floatMIN].get_value

        elif self.stringMIN <= virtual_address <= self.stringMAX:
            return self.memBlock[2][virtual_address - self.stringMIN].get_value

        elif self.charMIN <= virtual_address <= self.charMAX:
            return self.memBlock[4][virtual_address - self.charMIN].get_value

        elif self.boolMIN <= virtual_address <= self.boolMAX:
            return self.memBlock[3][virtual_address - self.boolMIN].get_value

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