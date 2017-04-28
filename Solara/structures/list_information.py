# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  05/27/17
# ------------------------------------------------------------

class listInformation:

    # Constructor
    def __init__(self):
        self.base_virtual_address = None
        self.length = 0
        self.type = None

    # stringTo methods
    def __str__(self):
        return ('[' + str(self.base_virtual_address) + ', ' + str(self.length) + ', ' + str(self.type) + ']')

    def __unicode__(self):
        return ('[' + str(self.base_virtual_address) + ', ' + str(self.length) + ', ' + str(self.type) + ']')

    # Method definitions

    def get_base_virtual_address(self):
        return self.base_virtual_address

    def get_length(self):
        return self.length

    def get_type(self):
        return self.type

    def set_base_virtual_address(self, base_virtual_address):
        self.base_virtual_address = base_virtual_address

    def set_length(self, length):
        self.length = length

    def set_type(self, type):
        self.type = type