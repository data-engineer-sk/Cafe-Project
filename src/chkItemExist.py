# This is the mini-project week4 ------------------------------------------------------------------------------
# File Name     : chkItemExist.py
# Date          : 12 Nov 2022
# Developer     : Samuel KO
# Description   : Check if the input list is defined in the .env file
# Input         : Three input parameters
#                 1) inList : the input list
#                 2) inName : the input field
#                 3) inMenu : the input menu name
# Output        : Return True if the menu is defined in .env, otherwise return False
# -------------------------------------------------------------------------------------------------------------

import traceback

def isExist(inList, inName, inMenu):
    # inList is a list of dictionary

    returnVal = False
    try:
        if inMenu == 'PRODUCT_MENU':
            key = 'prodName'
        elif inMenu == 'COURIER_MENU':
            key = 'name'
        elif inMenu == 'ORDER_MENU':
            key = 'customer_name'

        for item in inList:
            if (inName == item[key]):
                returnVal = True
                break
    except:
        traceback.print_exc()

    return returnVal
