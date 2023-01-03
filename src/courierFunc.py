# This is the mini-project week4 ------------------------------------------------------------------------------
# File Name     : courierFunc.py
# Date          : 12 Nov 2022
# Developer     : Samuel KO
# Description   : Perform all the courier functions
#                 1) Print Courier List
#                 2) Add Courier
#                 3) Update Courier
#                 4) Delete Courier
#                 5) Return to Main
# Input         : Input the menu type (inMenuType).  i.e. The user can select from 0 to 4.
#               : When 0 detected, exit the courier menu and return to the main menu.
# Output        : 
# -------------------------------------------------------------------------------------------------------------

import os
from dotenv import load_dotenv
import traceback
import drawMenu
import readCSVtoDict
import writeDictToCSV
import updateDictToCSV
import deleteDictToCSV
import chkItemExist
import chkInput
import printListToTableFormat as myPrint



def allFunction(inMenuType):
# Get the environment variables
    load_dotenv()
    inWriteHeader = os.getenv('COURIER_HEADER')
    inWriteFile = os.getenv('COURIERFILE')

    # Initizal before used
    userChoice = 0

    myLocalList = []
    myLocalDict = {}
    STATUS = 'NOT_OK'

    try:
        keepOn = True
        while keepOn:
            userChoice = drawMenu.drawMenu(inMenuType)
            if userChoice in range(0, 5): # Use range(0,5) to control the number of item's choice in menu
                if userChoice == 0:
                    print("Return to Main Menau " + str(userChoice))
                    return userChoice
                elif userChoice == 1:

                    tempPrintStorage = ''
                    myLocalList = readCSVtoDict.funReadCSVtoDICT(inWriteFile)
                    print("The Couriers List:")
                    # for counter, item in enumerate(myLocalList):
                    #    print(f'   [{counter}]=-->{item}')
                    myPrint.showListInTable(myLocalList)

                elif userChoice == 2:   # Add new courier if new, other abort the add courier operation
                    inputOK = False
                    myLocalList = readCSVtoDict.funReadCSVtoDICT(inWriteFile)
                    tempList = [] # Create temperatory list for storage
                    courierName = input("Enter Courier Name : ")
                    try:
                        courierPhone = (input("Enter Courier Phone Number : "))
                        if (chkInput.chkUserInput(courierPhone, 2) == 'OK'):
                            inputOK = True
                    except ValueError:
                            print("Not valid input for "+courierPhone+", try again!")
                            inputOK= False

                    if (inputOK):
                        myLocalDict['name'] = courierName 
                        myLocalDict['phone'] = courierPhone
                        tempList.append(myLocalDict)  # Store dictionary to list
                        if chkItemExist.isExist(myLocalList, courierName, 'COURIER_MENU'):
                            userInput = input(courierName + " is already existed.  Do you want to as a new one (Y/N)?")
                            if (userInput.upper() == 'N'):
                                # userChoice = 0
                                print("Not Added!!")
                            else:
                                STATUS = writeDictToCSV.funWriteDICTtoCSV(tempList, inWriteFile, inWriteHeader )
                        else:
                            STATUS = writeDictToCSV.funWriteDICTtoCSV(tempList, inWriteFile, inWriteHeader )

                elif userChoice == 3:  # Update existing courier based on user' selection
                    myLocalList = readCSVtoDict.funReadCSVtoDICT(inWriteFile)
                    # for listIndex in range(0, len(myLocalList)):  # listIndex
                    #      print(f'   [{listIndex}]-->{myLocalList[listIndex]}')
                    myPrint.showListInTable(myLocalList)
                    updateChoice = input("Please select the index from the above list for update : ")
                    try:
                        updateChoice = int(updateChoice)
                        print(f'You select {myLocalList[updateChoice]} to update')  # myLocalList[updateChoice] is the entire dictionary
                        for updateProperty in  myLocalList[updateChoice]:
                            selectedProperty = input(f'Enter an update for {updateProperty} : ')
                            if (len(selectedProperty) != 0):
                                myLocalList[updateChoice][updateProperty] = selectedProperty
                                print(f'{updateProperty} has been update to {selectedProperty}')
                            else:
                                print(f'Skip update for property : {updateProperty}')
                            #
                            # print(f'{updateProperty}-->{myLocalList[updateChoice][updateProperty]}')
                            #

                            # Print the updated dictionary, and prepare to update.
                            # print(f'updated : {myLocalList[updateChoice]}')
                            # tempList = []
                            # tempList.append(myLocalList[updateChoice])
                            inWriteHeader = os.getenv('COURIER_HEADER')
                            updateDictToCSV.updateDictToCSV(myLocalList[updateChoice], updateChoice, inWriteFile, inWriteHeader)
                    except ValueError:
                        print("Invalid input, please try again")
                elif userChoice == 4:  # Delete courier based on user's selection
                    try:
                        print("Delete Courier select " + str(userChoice))
                        myLocalList = readCSVtoDict.funReadCSVtoDICT(inWriteFile)
                        # for listIndex in range(0, len(myLocalList)):  # listIndex
                        #     print(f'   [{listIndex}]-->{myLocalList[listIndex]}')
                        myPrint.showListInTable(myLocalList)
                        deletedChoice = input("Please select the index from the above list for delete : ")
                        try:
                            deletedChoice = int(deletedChoice)
                        except ValueError:
                            pass # let the final try...except to print

                        print(f'You select {myLocalList[deletedChoice]} to delete')  # myLocalList[updateChoice] is the entire dictionary
                        #
                        # print(f'{updateProperty}-->{myLocalList[updateChoice][updateProperty]}')
                        #

                        STATUS = deleteDictToCSV.deleteDictToCSV(myLocalList[deletedChoice], deletedChoice, inWriteFile, inWriteHeader)
                    except TypeError:
                            print("Not valid input for "+deletedChoice+", try again!")
            else:
                print("Courier Menu : Invalid input, try again.")
                # Continue to courier menu
    except:
        traceback.print_exc()

    return userChoice