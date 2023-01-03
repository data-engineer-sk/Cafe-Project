# This is the mini-project week4 ------------------------------------------------------------------------------
# File Name     : chkInput.py
# Date          : 12 Nov 2022
# Developer     : Samuel KO
# Description   : This function will check the input from user, if the input is a desired type
#                 it will return the input to the caller, otherwise, will display a message to 
#                 acknowledge user
# Input         : Desire type for checking
# Output        : Return a input if the input type is correct
# -------------------------------------------------------------------------------------------------------------
                    # 1 means expected type must be string
                    # 2 means expected type must be numeric
                    # 3 means expected type must be alpha numeric

import traceback

def chkUserInput(inField, inputDesireType):

    stringFound = 0
    dotFound = 0
    result = 'NOT_OK'
    try:
        for i in range(len(inField)):
            if (inField[i].isdigit()):
                pass
            elif (inField[i] == '.'):
                dotFound += 1
            else:
                stringFound += 1

        if (stringFound >= 1 and int(inputDesireType) == 1):
            result = 'OK'
        elif (stringFound == 0 and dotFound == 1 and int(inputDesireType) == 2):
            result = 'OK'
        elif (stringFound == 0 and dotFound == 0 and int(inputDesireType) == 2):
            result = 'OK'
        elif (stringFound > 0 and dotFound == 0 and int(inputDesireType) == 3):
            result = 'OK'

        # print('your input value is ' + inField)
    except:
        traceback.print_exc()

    return result

