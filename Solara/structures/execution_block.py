# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  05/03/17
# ------------------------------------------------------------

from structures.memory_block import memoryBlock

class executionBlock:
    # Constructor
    def __init__(self):
        print('Initializing execution block....')
        self.parameters = memoryBlock()
        self.local = memoryBlock()
        self.temporal = memoryBlock()

    # Initializing ranges

    parametersMIN = 100000
    temporalMIN = 50000
    localMIN = 25000

    parametersMAX = 124999
    temporalMAX = 74999
    localMAX = 49999

    # stringTo methods

    def __str__(self):
        lines = []
        lines.append('Execution Block:')
        lines.append('Parameters:')
        lines.append(str(self.parameters))
        lines.append('Local:')
        lines.append(str(self.local))
        lines.append('Temporal:')
        lines.append(str(self.temporal))
        return '\n'.join(lines)

    def __unicode__(self):
        lines = []
        lines.append('Execution Block:')
        lines.append('Parameters:')
        lines.append(str(self.parameters))
        lines.append('Local:')
        lines.append(str(self.local))
        lines.append('Temporal:')
        lines.append(str(self.temporal))
        return '\n'.join(lines)

    # Method definitions

    # Get value method
    def get_value(self, virtual_address):
        if virtual_address >= self.parametersMIN and virtual_address <= self.parametersMAX:
            return self.parameters.get_value(virtual_address - self.parametersMIN)

        elif virtual_address >= self.temporalMIN and virtual_address <= self.temporalMAX:
            return self.temporal.get_value(virtual_address - self.temporalMIN)

        elif virtual_address >= self.localMIN and virtual_address <= self.localMAX:
            return self.local.get_value(virtual_address - self.localMIN)

        else:
            return None

    # Set value method
    def set_value(self, virtual_address, value):
        if virtual_address >= self.parametersMIN and virtual_address <= self.parametersMAX:
            return self.parameters.set_value(virtual_address - self.parametersMIN, value)

        elif virtual_address >= self.temporalMIN and virtual_address <= self.temporalMAX:
            return self.temporal.set_value(virtual_address - self.temporalMIN, value)

        elif virtual_address >= self.localMIN and virtual_address <= self.localMAX:
            return self.local.set_value(virtual_address - self.localMIN, value)

        else:
            return None

    # AVAIL for parameters method
    def availParameters(self, type):
        virtual_address = self.parameters.avail(type)
        if not virtual_address is None:
            return virtual_address + self.parametersMIN
        else:
            return None

    # AVAIL for local method
    def availLocal(self, type):
        virtual_address = self.local.avail(type)
        if not virtual_address is None:
            return virtual_address + self.localMIN
        else:
            return None

    # AVAIL for temporal method
    def availTemporal(self, type):
        virtual_address = self.temporal.avail(type)
        if not virtual_address is None:
            return virtual_address + self.temporalMIN
        else:
            return None

    # Clear method
    def clear(self):
        self.parameters.clear()
        self.local.clear()
        self.temporal.clear()

    # Memory allocation method
    def malloc(self, listP, listL, listT):
        for type in range(0, 5):
            for index in range(0, listP[type]):
                self.parameters.save(None, type, None)

        for type in range(0, 5):
            for index in range(0, listL[type]):
                self.local.save(None, type, None)

        for type in range(0, 5):
            for index in range(0, listT[type]):
                self.temporal.save(None, type, None)