# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  05/03/17
# ------------------------------------------------------------


class virtualMachine:

    def __init__(self, quadQueue):
        print('Initializing virtual machine....')
        self.execute(quadQueue.quadList)

    # stringTo methods

    def __str__(self):
        return ""

    def __unicode__(self):
        return ""

    def execute(self, quadList):

        index = 0
        while index <= (len(quadList) - 1):
            if quadList[index][0] == "*":
                print(str(index) + ": " + str(quadList[index][1]) + " * " + str(quadList[index][2]) + " = " + str(quadList[index][3]))

            elif quadList[index][0] == "/":
                print(str(index) + ": " + str(quadList[index][1]) + " / " + str(quadList[index][2]) + " = " + str(quadList[index][3]))

            elif quadList[index][0] == "+":
                print(str(index) + ": " + str(quadList[index][1]) + " + " + str(quadList[index][2]) + " = " + str(quadList[index][3]))

            elif quadList[index][0] == "-":
                print(str(index) + ": " + str(quadList[index][1]) + " - " + str(quadList[index][2]) + " = " + str(quadList[index][3]))

            elif quadList[index][0] == "<":
                print(str(index) + ": " + str(quadList[index][1]) + " < " + str(quadList[index][2]) + " = " + str(quadList[index][3]))

            elif quadList[index][0] == ">":
                print(str(index) + ": " + str(quadList[index][1]) + " > " + str(quadList[index][2]) + " = " + str(quadList[index][3]))

            elif quadList[index][0] == "||":
                print(str(index) + ": " + str(quadList[index][1]) + " || " + str(quadList[index][2]) + " = " + str(quadList[index][3]))

            elif quadList[index][0] == "&&":
                print(str(index) + ": " + str(quadList[index][1]) + " && " + str(quadList[index][2]) + " = " + str(quadList[index][3]))

            elif quadList[index][0] == "==":
                print(str(index) + ": " + str(quadList[index][1]) + " == " + str(quadList[index][2]) + " = " + str(quadList[index][3]))

            elif quadList[index][0] == "%":
                print(str(index) + ": " + str(quadList[index][1]) + " % " + str(quadList[index][2]) + " = " + str(quadList[index][3]))

            elif quadList[index][0] == "=":
                print(str(index) + ": " + str(quadList[index][3]) + " = " + str(quadList[index][1]))

            elif quadList[index][0] == "GOTOF":
                prueba = False
                #print(str(quadList[index][3]))
                # prueba = quadList[index][1]
                if not prueba:
                    index = (quadList[index][3] - 1)

            elif quadList[index][0] == "GOTO":
                index = (quadList[index][3] - 1)

            index += 1


        # for quad in quadList:
        #     if quad[0] == "*":
        #         print(str(quad[1]) + " * " + str(quad[2]) + " = " + str(quad[3]))
        #
        #     elif quad[0] == "/":
        #         print(str(quad[1]) + " / " + str(quad[2]) + " = " + str(quad[3]))
        #
        #     elif quad[0] == "+":
        #         print(str(quad[1]) + " + " + str(quad[2]) + " = " + str(quad[3]))
        #
        #     elif quad[0] == "-":
        #         print(str(quad[1]) + " - " + str(quad[2]) + " = " + str(quad[3]))
        #
        #     elif quad[0] == "<":
        #         print(str(quad[1]) + " < " + str(quad[2]) + " = " + str(quad[3]))
        #
        #     elif quad[0] == ">":
        #         print(str(quad[1]) + " > " + str(quad[2]) + " = " + str(quad[3]))
        #
        #     elif quad[0] == "||":
        #         print(str(quad[1]) + " || " + str(quad[2]) + " = " + str(quad[3]))
        #
        #     elif quad[0] == "&&":
        #         print(str(quad[1]) + " && " + str(quad[2]) + " = " + str(quad[3]))
        #
        #     elif quad[0] == "==":
        #         print(str(quad[1]) + " == " + str(quad[2]) + " = " + str(quad[3]))
        #
        #     elif quad[0] == "%":
        #         print(str(quad[1]) + " % " + str(quad[2]) + " = " + str(quad[3]))
        #
        #     elif quad[0] == "=":
        #         print(str(quad[3]) + " = " + str(quad[1]))
        #
        #     else:
        #         print("Something else probably goto")