# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  05/27/17
# ------------------------------------------------------------

class idRefInformation:

    # Constructor
    def __init__(self):
        self.name = None
        self.is_global = False
        self.type = None

    # stringTo methods
    def __str__(self):
        return ('[' + str(self.name) + ', ' + str(self.is_global) + ', ' + str(self.type) + ']')

    def __unicode__(self):
        return ('[' + str(self.name) + ', ' + str(self.is_global) + ', ' + str(self.type) + ']')

    # Method definitions

    def get_name(self):
        return self.name

    def get_is_global(self):
        return self.is_global

    def get_type(self):
        return self.type

    def set_name(self, name):
        self.name = name

    def set_is_global(self, is_global):
        self.is_global = is_global

    def set_type(self, type):
        self.type = type