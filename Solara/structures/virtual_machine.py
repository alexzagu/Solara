# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  05/03/17
# ------------------------------------------------------------
import sys
from structures.execution_block import executionBlock
from turtle import *
from tkinter import *

class virtualMachine:

    def __init__(self, quadQueue, mainMemory, funDir, programID):
        print('Initializing virtual machine....')
        self.mainMemory = mainMemory
        self.funDir = funDir
        self.mainMemory.malloc(self.funDir.search(programID)[4], self.funDir.search(programID)[5])
        print(self.mainMemory)
        self.pen = self.turtle_setup()
        self.terminal = Tk()
        self.terminalCount = 0
        self.top_frame_terminal = Frame(self.terminal)
        self.bottom_frame_terminal = Frame(self.terminal)
        print(quadQueue)
        self.execute(quadQueue.quadList)
        self.ide_setup()
        if self.have_predefined_solutions_been_used:
            self.pen.getscreen()._root.mainloop()

    # Class variables
    currentParameters = []
    have_global_definitions_been_processed = False
    executionBlock = executionBlock()
    have_predefined_solutions_been_used = False
    executionStack = []
    nextExecutionBlock = None

    # stringTo methods

    def __str__(self):
        return ""

    def __unicode__(self):
        return ""

    def turtle_setup(self):
        pen = Pen()
        screen_width = pen.screen.window_width()
        screen_height = pen.screen.window_height()
        pen.screen.setup(width=screen_width, height=screen_height/2+50, startx=screen_width, starty=0)

        pen.color('#f4425c')

        return pen

    def terminal_print(self, strprint):
        label = Label(self.bottom_frame_terminal, text=strprint, anchor='w')
        label.grid(sticky=E)
        label.configure(bg="#363835")
        label.configure(fg="white")
        self.terminalCount += 1
        label.pack()

    def is_virtual_address_global(self, virtual_address):
        if self.mainMemory.is_virtual_address_global_or_constant(virtual_address):
            return True
        else:
            return False

    def ide_setup(self):
        screen_width = self.terminal.winfo_screenwidth()
        screen_height = self.terminal.winfo_screenheight()
        self.terminal.configure(bg="#363835")
        self.terminal.geometry('%dx%d+%d+%d' % (screen_width/2, screen_height/2-80, screen_width/2, screen_height/2))

        self.top_frame_terminal.pack()
        self.bottom_frame_terminal.pack(side=BOTTOM)
        self.bottom_frame_terminal.configure(bg="#363835")

        #self.terminal.mainloop()

    def execute(self, quadList):

        index = 0
        while index <= (len(quadList) - 1):

            # Multiplication operation
            if quadList[index][0] == "*":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    result = left_value * right_value
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    result = left_value * right_value
                    self.mainMemory.set_value(quadList[index][3], result)

            # Division operation
            elif quadList[index][0] == "/":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if right_value == 0:
                        self.error_division_by_zero()
                    result = left_value / right_value
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if right_value == 0:
                        self.error_division_by_zero()
                    result = left_value / right_value
                    self.mainMemory.set_value(quadList[index][3], result)

            # Addition operation
            elif quadList[index][0] == "+":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    result = left_value + right_value
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    result = left_value + right_value
                    self.mainMemory.set_value(quadList[index][3], result)

            # Subtraction operation
            elif quadList[index][0] == "-":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    result = left_value - right_value
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    result = left_value - right_value
                    self.mainMemory.set_value(quadList[index][3], result)

            # Less than operation
            elif quadList[index][0] == "<":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value < right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value < right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # Less equal than operation
            elif quadList[index][0] == "<=":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value <= right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value <= right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # Greater than operation
            elif quadList[index][0] == ">":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value > right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value > right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # Greater equal than operation
            elif quadList[index][0] == ">=":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value >= right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value >= right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # Or operation
            elif quadList[index][0] == "||":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value or right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value or right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # And operation
            elif quadList[index][0] == "&&":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value and right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value and right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # Is equals operation
            elif quadList[index][0] == "==":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    if left_value == right_value:
                        result = True
                    else:
                        result = False
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    if left_value == right_value:
                        result = True
                    else:
                        result = False
                    self.mainMemory.set_value(quadList[index][3], result)

            # Mod operation
            elif quadList[index][0] == "%":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        left_value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        left_value = self.executionBlock.get_value(quadList[index][1])

                    if self.is_virtual_address_global(quadList[index][2]):
                        right_value = self.mainMemory.get_value(quadList[index][2])
                    else:
                        right_value = self.executionBlock.get_value(quadList[index][2])
                    result = left_value % right_value
                    self.executionBlock.set_value(quadList[index][3], result)
                else:
                    left_value = self.mainMemory.get_value(quadList[index][1])
                    right_value = self.mainMemory.get_value(quadList[index][2])
                    result = left_value % right_value
                    self.mainMemory.set_value(quadList[index][3], result)

            # Assignation operation
            elif quadList[index][0] == "=":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        value = self.mainMemory.get_value(quadList[index][1])
                        self.executionBlock.set_value(quadList[index][3], value)
                    else:
                        value = self.executionBlock.get_value(quadList[index][1])
                        self.executionBlock.set_value(quadList[index][3], value)
                else:
                    value = self.mainMemory.get_value(quadList[index][1])
                    self.mainMemory.set_value(quadList[index][3], value)

            # Negation operation
            elif quadList[index][0] == "!":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        value = self.executionBlock.get_value(quadList[index][1])

                    self.executionBlock.set_value(quadList[index][3], not value)
                else:
                    value = self.mainMemory.get_value(quadList[index][1])
                    self.mainMemory.set_value(quadList[index][3], not value)

            # GOTOF operation
            elif quadList[index][0] == "GOTOF":
                value = self.executionBlock.get_value(quadList[index][1])

                if not value:
                    index = (quadList[index][3] - 1)

            # GOTO operation
            elif quadList[index][0] == "GOTO":
                index = (quadList[index][3] - 1)

            # ERA operation
            elif quadList[index][0] == "ERA":
                self.nextExecutionBlock = executionBlock()
                self.nextExecutionBlock.malloc(self.funDir.search(quadList[index][1])[3], self.funDir.search(quadList[index][1])[4], self.funDir.search(quadList[index][1])[5])

            # GOSUB operation
            elif quadList[index][0] == "GOSUB":
                if quadList[index][1] == "main":
                    self.have_global_definitions_been_processed = True
                    self.executionBlock.malloc(self.funDir.search('main')[3], self.funDir.search('main')[4], self.funDir.search('main')[5])
                else:
                    self.executionStack.append((self.executionBlock, index))
                    self.executionBlock = self.nextExecutionBlock
                    parameter_virtual_address = 100000
                    for parameter in self.currentParameters:
                        self.executionBlock.set_value(parameter_virtual_address, parameter)
                        parameter_virtual_address = parameter_virtual_address + 1

                    self.currentParameters = []

                index = (quadList[index][3] - 1)

            # RETURN operation
            elif quadList[index][0] == "RETURN":
                if self.is_virtual_address_global(quadList[index][1]):
                    value = self.mainMemory.get_value(quadList[index][1])
                else:
                    value = self.executionBlock.get_value(quadList[index][1])

                self.mainMemory.set_value(quadList[index][3], value)

            # ENDPROC operation
            elif quadList[index][0] == "ENDPROC":
                if len(self.executionStack) > 0:
                    execution_unit = self.executionStack.pop()
                    self.executionBlock = execution_unit[0]
                    index = execution_unit[1]

            # PRINT operation
            elif quadList[index][0] == "PRINT":
                print('')


            # PARAMETER operation
            elif quadList[index][0] == "PARAMETER":
                if self.is_virtual_address_global(quadList[index][1]):
                    self.currentParameters.append(self.mainMemory.get_value(quadList[index][1]))
                else:
                    self.currentParameters.append(self.executionBlock.get_value(quadList[index][1]))

            # SET_NEXT operation
            elif quadList[index][0] == "SET_NEXT":
                if self.is_virtual_address_global(quadList[index][3]):
                    self.mainMemory.set_next(quadList[index][3], quadList[index][1])
                else:
                    self.executionBlock.set_next(quadList[index][3], quadList[index][1])

            # VERIFY operation
            elif quadList[index][0] == "VERIFY":
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][1]):
                        value = self.mainMemory.get_value(quadList[index][1])
                    else:
                        value = self.executionBlock.get_value(quadList[index][1])
                else:
                    value = self.mainMemory.get_value(quadList[index][1])

                if not (value >= quadList[index][2] and value < quadList[index][3]):
                    self.error_index_out_of_bounds()

            #LOCATE operation
            elif quadList[index][0] == "LOCATE":
                virtual_address = quadList[index][1]
                if self.have_global_definitions_been_processed:
                    if self.is_virtual_address_global(quadList[index][2]):
                        indexer = self.mainMemory.get_value(quadList[index][2])
                    else:
                        indexer = self.executionBlock.get_value(quadList[index][2])

                    if self.is_virtual_address_global(virtual_address):
                        for counter in range(0, indexer):
                            virtual_address = self.mainMemory.get_next(virtual_address)
                        value = self.mainMemory.get_value(virtual_address)
                        self.executionBlock.set_value(quadList[index][3], value)
                    else:
                        for counter in range(0, indexer):
                            virtual_address = self.executionBlock.get_next(virtual_address)
                        value = self.executionBlock.get_value(virtual_address)
                        self.executionBlock.set_value(quadList[index][3], value)
                else:
                    indexer = self.mainMemory.get_value(quadList[index][2])
                    for counter in range(0, indexer):
                        virtual_address = self.mainMemory.get_next(virtual_address)
                    value = self.mainMemory.get_value(virtual_address)
                    self.mainMemory.set_value(quadList[index][3], value)

            # LENGTH operation
            elif quadList[index][0] == "LENGTH":
                if self.have_global_definitions_been_processed:
                    self.executionBlock.set_value(quadList[index][3], quadList[index][1])
                else:
                    self.mainMemory.set_value(quadList[index][3], quadList[index][1])

            # EXEC operation
            elif quadList[index][0] == "EXEC":
                self.have_predefined_solutions_been_used = True
                if quadList[index][1] == "PRINT":
                    print(self.currentParameters[0])
                    self.terminal_print(self.currentParameters[0])
                elif quadList[index][1] == "MOVE_UP":
                    self.pen.up()
                    self.pen.sety(self.currentParameters[0])
                    self.pen.down()
                elif quadList[index][1] == "MOVE_DOWN":
                    self.pen.up()
                    self.pen.sety(self.currentParameters[0])
                    self.pen.down()
                elif quadList[index][1] == "MOVE_RIGHT":
                    self.pen.up()
                    self.pen.setx(self.currentParameters[0])
                    self.pen.down()
                elif quadList[index][1] == "MOVE_LEFT":
                    self.pen.up()
                    self.pen.setx(self.currentParameters[0])
                    self.pen.down()
                elif quadList[index][1] == "DRAW_RECTANGLE":
                    self.pen.up()
                    self.pen.setposition(self.currentParameters[0], self.currentParameters[1])
                    self.pen.down()
                    self.pen.sety(-self.currentParameters[2])
                    self.pen.setx(-self.currentParameters[3])
                    self.pen.sety(self.currentParameters[2])
                    self.pen.setx(self.currentParameters[3])
                elif quadList[index][1] == "DRAW_LINE":
                    self.pen.up()
                    self.pen.setposition(self.currentParameters[0], self.currentParameters[1])
                    self.pen.down()
                    self.pen.setposition(self.currentParameters[2], self.currentParameters[3])
                elif quadList[index][1] == "DRAW_CIRCLE":
                    self.pen.up()
                    self.pen.setposition(self.currentParameters[0], self.currentParameters[1])
                    self.pen.down()
                    self.pen.circle(self.currentParameters[2])

                self.currentParameters = []

            index += 1

    # Error-handling functions for execution-time semantic analysis

    # Error-handling function for division by zero
    def error_division_by_zero(self):
        print('Error!')
        print('Division by 0 not possible!')
        sys.exit()

    # Error-handling function for index out of bounds
    def error_index_out_of_bounds(self):
        print('Error!')
        print('Index out of bounds!')
        sys.exit()