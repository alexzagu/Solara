# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  05/03/17
# ------------------------------------------------------------

class memoryUnit:

    # Constructor
    def __init__(self):
        print('')
        self.value = 0
        self.next = 0

    # stringTo methods
    def __str__(self):
        return ('[' + str(self.value) + ', ' + str(self.next) + ']')

    def __unicode__(self):
        return ('[' + str(self.value) + ', ' + str(self.next) + ']')

    # Method definitions

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next
