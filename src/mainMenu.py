# This is the mini-project week4 ------------------------------------------------------------------------------
# File Name     : mainMenu.py
# Date          : 12 Nov 2022
# Developer     : Samuel KO
# Description   : This function responsible for routing to the specific menu.
#               : Namely, 1) Product menu 2) Courier menu 3) Order menu 0) Exit the system
#               : User can select the menu number and switch to the desire menu.
# Input         : None
# Output        : 
# -------------------------------------------------------------------------------------------------------------

import traceback
import os
import drawMenu     # Draw the specific menu which provide by .env file
import productFunc  # For all product functions
import courierFunc  # For all courier functions
import orderFunc    # For all order functions

def main():
    try:
        keepOn = True
        while keepOn:
            userChoice = drawMenu.drawMenu("MAIN_MENU") # Setup the entry menu
            if userChoice in range(0, 4): # Use range(0,6) to control the number of item's choice in menu
                if userChoice == 0:
                    print("You terminate the System, goodbye~\n")
                    keepOn = False
                    # exit() # will exit the system by throw an exception
                    os._exit # Thus, use os._exit or os._exit(1) to exit the system without throwing an exception
                elif (userChoice == 1):
                    returnChoice = productFunc.allFunction("PRODUCT_MENU")
                elif (userChoice == 2):
                    returnChoice  = courierFunc.allFunction("COURIER_MENU")
                elif (userChoice == 3):
                    returnChoice = orderFunc.allFunction("ORDER_MENU")
            else:
                print("Main Menu : Invalid input, please enter menu index again.\n")
                # Continue the main menu
    except:
        traceback.print_exc()

main()