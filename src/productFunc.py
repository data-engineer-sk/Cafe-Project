## This is the mini-project week4 ------------------------------------------------------------------------------
# File Name     : productFunc.py
# Date          : 12 Nov 2022
# Developer     : Samuel KO
# Description   : Perform all the product functions
#                 1) Print Product List
#                 2) Add Product
#                 3) Update Product
#                 4) Delete Product
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
    inWriteHeader = os.getenv('PRODUCT_HEADER')
    inWriteFile = os.getenv('PRODUCTFILE')

    # Initizal before used
    userChoice = 0

    myLocalList = []
    myLocalDict = {}
    STATUS = 'NOT_OK'

    try:
        keepOn = True
        while keepOn:
            userChoice = drawMenu.drawMenu(inMenuType)
            if (userChoice in range(0, 5)): # Use range(0,5) to control the number of item's choice in menu
                if userChoice == 0:
                    print("Return to Main Menau " + str(userChoice))
                    return userChoice
                elif userChoice == 1:   # Print product list
                    tempPrintStorage = ''
                    myLocalList = readCSVtoDict.funReadCSVtoDICT(inWriteFile)
                    # Another way to print the list
                    # for counter, item in enumerate(myLocalList):
                    #    print(f'   [{counter}]=-->{item}')
                    myPrint.showListInTable(myLocalList)
                elif userChoice == 2:   # Add new product if new, other abort the add product operation
                    myLocalList = readCSVtoDict.funReadCSVtoDICT(inWriteFile)
                    tempList = [] # Create temperatory list for storage

                    # 1 means expected type must be string
                    # 2 means expected type must be numeric
                    # 3 means expected type must be alpha numeric
                    inputOK = False 

                    productName = input("Enter Product Name : ")                    
                    if (chkInput.chkUserInput(productName, 3) != 'OK'):  
                        pass
                    else:
                        productPrice = input("Enter Product Price : ")
                        try:
                            if (chkInput.chkUserInput(productPrice, 2) == 'OK'):
                                productPrice = float(productPrice)
                                inputOK = True
                        except ValueError:
                            print("Not valid input for "+productPrice+", try again!")
                            inputOK= False

                    if (inputOK): # Check if the input is ok, otherwise, exit the operation and return to the current menu
                        myLocalDict['prodName'] = productName 
                        myLocalDict['price'] = productPrice
                        tempList.append(myLocalDict)  # Store dictionary to list
                        if chkItemExist.isExist(myLocalList, productName, 'PRODUCT_MENU'):
                            userInput = input(productName + " is already existed.  Do you want to as a new one (Y/N)?")
                            if (userInput.upper() == 'N'):
                                userChoice = 0
                                print("Not Added!!")
                            else:
                                STATUS = writeDictToCSV.funWriteDICTtoCSV(tempList, inWriteFile, inWriteHeader )
                        else:
                            STATUS = writeDictToCSV.funWriteDICTtoCSV(tempList, inWriteFile, inWriteHeader )
                    else:
                        print('Invalid input, please try again')

                elif userChoice == 3:  # Update existing product based on user' selection
                    myLocalList = readCSVtoDict.funReadCSVtoDICT(inWriteFile)
                    # for listIndex in range(0, len(myLocalList)):  # listIndex
                    #      print(f'   [{listIndex}]-->{myLocalList[listIndex]}')
                    
                    # for i, item in enumerate(myLocalList):
                    #     print (f'[{i}]-->{item}')
                    myPrint.showListInTable(myLocalList)
                    updateChoice = input("Please select the index from the above list for update : ")
                    try:
                        updateChoice = int(updateChoice)
                        print(f'You select {myLocalList[updateChoice]} to update') 
                        for updateProperty in  myLocalList[updateChoice]:
                            selectedProperty = input(f'Enter an update for \"{updateProperty}\" : ')
                            if (len(selectedProperty) != 0):
                                myLocalList[updateChoice][updateProperty] = selectedProperty
                                print(f'\"{updateProperty}\" has been update to {selectedProperty}')
                            else:
                                print(f'Skip update for property : \"{updateProperty}\"')
                            
                            inWriteHeader = os.getenv('PRODUCT_HEADER')
                            updateDictToCSV.updateDictToCSV(myLocalList[updateChoice], updateChoice, inWriteFile, inWriteHeader)
                    
                    except ValueError:
                        print("Invlid input, please try again!")
                    
                elif userChoice == 4:  # Delete product based on user's selection
                    try:
                        # print("Delete Product select " + str(userChoice))
                        myLocalList = readCSVtoDict.funReadCSVtoDICT(inWriteFile)
                        # for listIndex in range(0, len(myLocalList)):  # listIndex
                        #     print(f'   [{listIndex}]-->{myLocalList[listIndex]}')
                        myPrint.showListInTable(myLocalList)
                        deletedChoice = input("Please select the index from the above list for delete : ")
                        
                        if (chkInput.chkUserInput(deletedChoice, 2) == 'OK'):
                            deletedChoice = int(deletedChoice)
                            print(f'You select {myLocalList[deletedChoice]} to delete')  # myLocalList[updateChoice] is the entire dictionary
                            #
                            # print(f'{updateProperty}-->{myLocalList[updateChoice][updateProperty]}')
                            #
                            STATUS = deleteDictToCSV.deleteDictToCSV(myLocalList[deletedChoice], deletedChoice, inWriteFile, inWriteHeader)
                        else:
                            print(f'Invalid input for delete, please try again.') 
                    except ValueError:
                        print("Not valid input for "+deletedChoice+", try again!")

            else:
                print("Product Menu : Invalid input, try again.")
                # Continue the product menu
    except:
        traceback.print_exc()

    return userChoice