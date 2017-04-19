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

    # stringTo methods

    def __str__(self):
        return ""

    def __unicode__(self):
        return ""

    # Method definitions

    # AVAIL for parameters method
    def availParameters(self, type):
        return self.parameters.avail(type)

    # AVAIL for local method
    def availLocal(self, type):
        return self.local.avail(type)

    # AVAIL for temporal method
    def availTemporal(self, type):
        return self.temporal.avail(type)

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