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
    def __init__(self, listP, listL, listT):
        print('Initializing execution block....')
        Parameters = memoryBlock()
        Local = memoryBlock()
        Temp = memoryBlock()

        for x in listP:
            for y in listP[x]:
                Parameters.save(None, x, None)

        for x in listL:
            for y in listL[x]:
                Local.save(None, x, None)

        for x in listT:
            for y in listT[x]:
                Temp.save(None, x, None)

    # stringTo methods

    def __str__(self):
        return ""

    def __unicode__(self):
        return ""