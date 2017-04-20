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
        for x in listP:
            for y in listP[x]:
                self.parameters.save(None, x, None)

        for x in listL:
            for y in listL[x]:
                self.local.save(None, x, None)

        for x in listT:
            for y in listT[x]:
                self.temporal.save(None, x, None)