# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  Solara
#  Alejandro Zamudio A01280223
#  Melissa Figueroa A01280388
#  11/03/17
# ------------------------------------------------------------

#-------------------------------------------------------------

class functionDirectory:

    # Constructor
    def __init__(self):
        print('Initializing function directory....')

    # Class variable
    # Dictionary that holds all function information for the whole program.
    # It follows the following format:
    # key: name value: [type, (paramType1, paramType2, paramTypeN), symbolTable, [numIntParam, numFloatParam,
    #                   numStringParam, numCharParam, numBoolParam], [numLocalInt, numLocalFloat, numLocalString,
    #                   numLocalChar, numLocalBool], [numTempInt, numTempFloat, numTempString, numTempChar,
    #                   numTempBool], currentQuadCount] or
    # key: name value: [type, (paramType1, paramType2, paramTypeN), symbolTable, [numIntConst, numFloatConst,
    #                   numStringConst, numCharConst, numBoolConst], [numGlobalInt, numGlobalFloat, numGlobalString,
    #                   numGlobalChar, numGlobalBool], [numTempInt, numTempFloat, numTempString, numTempChar,
    #                   numTempBool], currentQuadCount]
    functionDic = {}

    # stringTo methods

    def __str__(self):
        lines = []
        for k, v in self.functionDic.iteritems():
            lines.append('key: ' + str(k) + ' value: ' + str(v))
        return '\n'.join(lines)

    def __unicode__(self):
        lines = []
        for k, v in self.functionDic.iteritems():
            lines.append('key: ' + str(k) + ' value: ' + str(v))
        return '\n'.join(lines)

    # Method definitions

    # Add method
    def add(self, name, type, parameters, symbolTable, numParamDefined, numLocalVarsDefined, numTempVarsDefined,
            currentQuadCount):
        self.functionDic[name] = [type, parameters, symbolTable, numParamDefined, numLocalVarsDefined,
                                  numTempVarsDefined, currentQuadCount]

    # Search method
    def search(self, name):
        if name in self.functionDic:
            return self.functionDic[name]
        else:
            return None

    # Method to append a new parameter for a specific solution
    def append_parameter(self, name, code):
        self.functionDic[name][1] += (code, )

    # Method to update the list of number of parameters defined of each data type
    def update_number_of_param_variables(self, name, numParamDefined):
        self.functionDic[name][3] = numParamDefined

    # Method to update the list of number of constants used of each data type
    def update_number_of_constants(self, name, numConstUsed):
        self.functionDic[name][3] = numConstUsed

    # Method to update the list of number of local variables defined of each data type
    def update_number_of_local_variables(self, name, numLocalVarsDefined):
        self.functionDic[name][4] = numLocalVarsDefined

    # Method to update the list of number of global variables defined of each data type
    def update_number_of_global_variables(self, name, numGlobalVarsDefined):
        self.functionDic[name][4] = numGlobalVarsDefined

    # Method to update the list of number of temporal variables defined of each data type
    def update_number_of_temp_variables(self, name, numTempVarsDefined):
        self.functionDic[name][5] = numTempVarsDefined

    # Method to include the global return variables from each solution to the list of global variables defined
    def add_global_return_var(self, name, type):
        self.functionDic[name][4][type] = self.functionDic[name][4][type] + 1

    # Method to update the list of number of global variables defined of each data type. Update specific type count
    def update_number_of_global_type(self, name, type):
        self.functionDic[name][4][type] = self.functionDic[name][4][type] + 1