# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  18/04/17
# ------------------------------------------------------------

from structures.memory_block import memoryBlock

class mainMemory:
    # Constructor
    def __init__(self):
        print('Initializing main memory....')
        self.globals = memoryBlock()
        self.temporal = memoryBlock()
        self.constants = memoryBlock()

    # Initializing ranges

    globalMIN = 0
    temporalMIN = 50000
    constantsMIN = 75000

    globalMAX = 24999
    temporalMAX = 74999
    constantsMAX = 99999

    # stringTo methods

    def __str__(self):
        lines = []
        lines.append('Main Memory:')
        lines.append('Global:')
        lines.append(str(self.globals))
        lines.append('Temporal:')
        lines.append(str(self.temporal))
        lines.append('Constant:')
        lines.append(str(self.constants))
        return '\n'.join(lines)

    def __unicode__(self):
        lines = []
        lines.append('Main Memory:')
        lines.append('Global:')
        lines.append(str(self.globals))
        lines.append('Temporal:')
        lines.append(str(self.temporal))
        lines.append('Constant:')
        lines.append(str(self.constants))
        return '\n'.join(lines)

    # Method definitions

    # AVAIL for globals method
    def availGlobals(self, type):
        virtual_address = self.globals.avail(type)
        if not virtual_address is None:
            return virtual_address + self.globalMIN
        else:
            return None

    # AVAIL for temporal method
    def availTemporal(self, type):
        virtual_address = self.temporal.avail(type)
        if not virtual_address is None:
            return virtual_address + self.temporalMIN
        else:
            return None

    # AVAIL for constants method
    def availConstants(self, type):
        virtual_address = self.constants.avail(type)
        if not virtual_address is None:
            return virtual_address + self.constantsMIN
        else:
            return None

    # Clear method
    def clear(self):
        self.globals.clear()
        self.temporal.clear()
        self.constants.clear()

    # Memory allocation method
    def malloc(self, listG, listT, listC):
        for x in listG:
            for y in listG[x]:
                self.globals.save(None, x, None)

        for x in listT:
            for y in listT[x]:
                self.temporal.save(None, x, None)

        for x in listC:
            for y in listC[x]:
                self.constants.save(None, x, None)

    # Save constant method
    def saveConstant(self, value, type):
        virtual_address = self.constants.save(value, type, None)
        if not virtual_address is None:
            return virtual_address + self.constantsMIN
        else:
            return None

    # Search constant memory method
    def searchConstants(self, value, type):
        virtual_address = self.constants.search(value, type)
        if not virtual_address is None:
            return virtual_address + self.constantsMIN
        else:
            return None