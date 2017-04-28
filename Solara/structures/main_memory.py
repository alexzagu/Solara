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

    # Get value method
    def get_value(self, virtual_address):
        if virtual_address >= self.globalMIN and virtual_address <= self.globalMAX:
            return self.globals.get_value(virtual_address - self.globalMIN)

        elif virtual_address >= self.temporalMIN and virtual_address <= self.temporalMAX:
            return self.temporal.get_value(virtual_address - self.temporalMIN)

        elif virtual_address >= self.constantsMIN and virtual_address <= self.constantsMAX:
            return self.constants.get_value(virtual_address - self.constantsMIN)

        else:
            return None

    # Set value method
    def set_value(self, virtual_address, value):
        if virtual_address >= self.globalMIN and virtual_address <= self.globalMAX:
            return self.globals.set_value(virtual_address - self.globalMIN, value)

        elif virtual_address >= self.temporalMIN and virtual_address <= self.temporalMAX:
            return self.temporal.set_value(virtual_address - self.temporalMIN, value)

        elif virtual_address >= self.constantsMIN and virtual_address <= self.constantsMAX:
            return self.constants.set_value(virtual_address - self.constantsMIN, value)

        else:
            return None

    # Set next method
    def set_next(self, virtual_address, next_virtual_address):
        if virtual_address >= self.globalMIN and virtual_address <= self.globalMAX:
            self.globals.set_next(virtual_address - self.globalMIN, next_virtual_address)

    # Get next method
    def get_next(self, virtual_address):
        if virtual_address >= self.globalMIN and virtual_address <= self.globalMAX:
            return self.globals.get_next(virtual_address - self.globalMIN)

        else:
            return None

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
    def malloc(self, listG, listT):
        for type in range(0, 5):
            for index in range(0, listG[type]):
                self.globals.save(None, type, None)

        for type in range(0, 5):
            for index in range(0, listT[type]):
                self.temporal.save(None, type, None)

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

    # Is virtual address global or constant or none
    def is_virtual_address_global_or_constant(self, virtual_address):
        if virtual_address >= self.globalMIN and virtual_address <= self.globalMAX:
            return True

        elif virtual_address >= self.constantsMIN and virtual_address <= self.constantsMAX:
            return True

        else:
            return False