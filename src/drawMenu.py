# This is the mini-project week4 ------------------------------------------------------------------------------
# File Name     : drawMenu.py
# Date          : 12 Nov 2022
# Developer     : Samuel KO
# Description   : This function will draw the system menu for 
#               : 1) Product menu 2) Courier menu 3) Order menu 4) Main menu
#               : By reading the .env file, this function will draw the 
#               : desire menu based on the input menu type
# Input         : inMenuType
# Output        : Return the menu number (0 to 3) back to the caller
#               :   1 - Proudct menu
#               :   2 - Courier menu
#               :   3 - Order menu
#               :   0 - Main menu
# -------------------------------------------------------------------------------------------------------------

# Import the system required packages
import os
from dotenv import load_dotenv
import traceback

def drawMenu(inMenuType):

    try:
        # Clearing the Screen
        # temperary supspend the clear screen
        # os.system('clear')

        # Get the environment variables
        load_dotenv()

        Menu = os.getenv(inMenuType)

        userChoice = ''
        menuList = Menu.split(',')
        print()
        for menuItem in menuList:
            print(menuItem.strip())
        print()
            
        userChoice = input("Please select your choice : ")
        if (userChoice.isdigit()):
            return int(userChoice)
        else:
            # Return a invalid input indicator and back to main menu
            userChoice = 9

        ## Debug --> print('DrawMenu return : ' + str(userChoice))
    except:
        traceback.print_exc()

    return userChoice

