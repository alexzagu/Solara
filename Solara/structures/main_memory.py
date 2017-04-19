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

    # stringTo methods

    def __str__(self):
        return ""

    def __unicode__(self):
        return ""

    # Method definitions

    # AVAIL for globals method
    def availGlobals(self, type):
        return self.globals.avail(type)

    # AVAIL for temporal method
    def availTemporal(self, type):
        return self.temporal.avail(type)

    # AVAIL for constants method
    def availConstants(self, type):
        return self.constants.avail(type)

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