# This is the mini-project week4 ------------------------------------------------------------------------------
# File Name     : orderFunc.py
# Date          : 12 Nov 2022
# Developer     : Samuel KO
# Description   : Perform all the order functions
#                 1) Print Order List
#                 2) Add Order
#                 3) Update Order Status
#                 4) Update Existing Order
#                 5) Delete Courier
#                 0) Return to Main
# Input         : Input the menu type (inMenuType).  i.e. The user can select from 0 to 5.
#               : When 0 detected, exit the courier menu and return to the main menu.
# Output        : 
# -------------------------------------------------------------------------------------------------------------
# order_status  : Preparing, Awaiting Pickup, Out-for-Delivery, Delivered
# -------------------------------------------------------------------------------------------------------------
# define a sample dictionary with key value pairs
#
# myOrderList = [{'customer_name':'Nishu','customer_address':'address in Manchester','customer_phone':'601','status':'processing'},
#                 {'customer_name':'Megha','customer_address':'address 1 for Megha','customer_phone':'602','status':'processing'},
#                 {'customer_name':'Zach', 'customer_address':'.address near the city center','customer_phone':'603','status':'processing'}
#                 {'customer_name':'Rachel','customer_address':'Bolton of UK','customer_phone':'604','status':'processing'},
#                 {'customer_name':'Rachal','customer_address':'The main office of Generation','customer_phone':'605','status':'processing'},
#                 {'customer_name':'Tom','customer_address':'Not specified','customer_phone':'606','status':'processing'}]

import os
from dotenv import load_dotenv
import traceback
import drawMenu
import readCSVtoDict
import writeDictToCSV
import updateDictToCSV
import deleteDictToCSV
import chkItemExist
import printListToTableFormat as myPrint

def allFunction(inMenuType):
# Get the environment variables
    load_dotenv()
    inWriteHeader = os.getenv('ORDER_HEADER')
    inWriteFile = os.getenv('ORDERFILE')

    # Initizal before used
    userChoice = 0

    myLocalList = []
    myLocalDict = {}

    STATUS = 'NOT_OK'
    
    try:
        keepOn = True
        while keepOn:
            userChoice = drawMenu.drawMenu(inMenuType)
            if userChoice in range(0, 6): # Use range(0,6) to control the number of item's choice in menu
                if userChoice == 0:
                    print("Return to Main Menau " + str(userChoice))
                    return userChoice
                elif userChoice == 1:
                    tempPrintStorage = ''
                    myLocalList = readCSVtoDict.funReadCSVtoDICT(inWriteFile)
                    print("The Order List:")
                    # for counter, item in enumerate(myLocalList):
                    #    print(f'  [{counter}]=-->{item}')
                    myPrint.showListInTable(myLocalList)
                elif userChoice == 2:
                    myLocalDict = {}
                    myLocalList = []
                    extractCourier = ''
                    # Collect the new order details for adding
                    print("Add a new order details")
                    # orderNumber = input("Please enter the order number : ")
                    custName = input("Please enter the customer name : ")
                    custAddress = input("Please enter the customer address : ")
                    try:
                        custPhone = input("Please enter the customer contact phone : ")
                        custPhone = int(custPhone)
                        # Select the Product :----
                        productList = readCSVtoDict.funReadCSVtoDICT('../data/fileProduct.csv')  # Get the updated-currentList for product
                        print("Please select product index value and separated by a comma : ")
                        # for productDict in productList:   # Get the dictionary from the list
                        #     for listItem in productDict:  # Get the key(s) from the dictionary
                        #         if (listItem == 'prodName'):  # Check if the key is name of courier
                        #             print(f"   [{productList.index(productDict)}] --> {productDict[listItem]}")
                        myPrint.showListInTable(productList)
                        productListIndex = input("Select the index number from the above listed products : ")
                        try:
                            # Select the Courier :----
                            courierList = readCSVtoDict.funReadCSVtoDICT('../data/fileCourier.csv')  # Get the updated-currentList 
                            print("Please select the index number from below's courier list: ")
                            # for courierDict in courierList:   # Get the dictionary from the list
                            #     for dictItem in courierDict:  # Get the key(s) from the dictionary
                            #         if (dictItem == 'name'):  # Check if the key is name of courier
                            #             print(f"   [{courierList.index(courierDict)}] --> {courierDict[dictItem]}")
                            myPrint.showListInTable(courierList)
                            inputIndex = input("Index number of the courier : ")
                            try:
                                inputIndex = int(inputIndex)
                                # After getting the selected index, iterates the name of the courier
                                for courierDict in courierList:   # Get the dictionary from the list
                                    for dictItem in courierDict:  # Get the key(s) from the dictionary
                                        if (dictItem == 'name' and courierList.index(courierDict) == inputIndex):
                                            extractCourier = courierDict[dictItem]

                                # Set the status to Preparing for every new order
                                STATUS = 'PREPARING'
                                # Prepare a new order dictionary to write
                                myLocalDict['customer_name'] = custName
                                myLocalDict['customer_address'] = custAddress
                                myLocalDict['customer_phone'] = custPhone
                                myLocalDict['status'] = STATUS
                                myLocalDict['couriers'] = extractCourier
                                myLocalDict['items'] = productListIndex
                                # Debug printing --->    # print(myLocalDict)
                                myLocalList.append(myLocalDict)
                                returnValue = writeDictToCSV.funWriteDICTtoCSV(myLocalList, inWriteFile, inWriteHeader )
                            except:
                                print("Invalid input, please try again")
                        except ValueError:
                            print("Invalid input, please try again")
                    except ValueError:
                        print("Invalid input, please try again!")
                elif userChoice == 3:  # Update existing order based on user's selection
                    try:
                        myLocalList = readCSVtoDict.funReadCSVtoDICT(inWriteFile)
                        # for listIndex in range(0, len(myLocalList)):  # listIndex
                        #      print(f'   [{listIndex}]-->{myLocalList[listIndex]}')
                        myPrint.showListInTable(myLocalList)
                        updateChoice = input("Please select the index from the above list for update : ")
                        try:
                            updateChoice = int(updateChoice)
                            print(f'You select {myLocalList[updateChoice]} to update')  # myLocalList[updateChoice] is the entire dictionary
                            inSTATUS_MENU = os.getenv('STATUS_MENU')
                            setSTATUS = ''
                            inStatus = 'status'

                        except IndexError:
                            print("Invalid input, please try again!")

                        selectStatus = drawMenu.drawMenu("STATUS_MENU") # Setup the status menue for user selection
                        
                        if (selectStatus == 1):
                            setSTATUS = "PREPARING"
                        elif(selectStatus == 2):
                            setSTATUS = "OUT-FOR-DELIVERY"
                        elif(selectStatus == 3):
                            setSTATUS = "DELIVERED"

                        if (selectStatus > 0 and selectStatus <= 3):    
                            myLocalList[updateChoice][inStatus] = setSTATUS
                            updateDictToCSV.updateDictToCSV(myLocalList[updateChoice], updateChoice, inWriteFile, inWriteHeader)
                        else:
                            print(f"Incorrect {selectStatus} index, abort change")

                        # for updateProperty in  myLocalList[updateChoice]:
                        #     selectedProperty = input(f'Enter an update for {updateProperty} : ')
                        #     if (len(selectedProperty) != 0):
                        #         myLocalList[updateChoice][updateProperty] = selectedProperty
                        #         print(f'{updateProperty} has been update to {selectedProperty}')
                        #     else:
                        #         print(f'Skip update for property : {updateProperty}')
                                            # (
                                            # print(f'{updateProperty}-->{myLocalList[updateChoice][updateProperty]}')
                                            #

                                            # Print the updated dictionary, and prepare to update.
                                            # print(f'updated : {myLocalList[updateChoice]}')
                                            # tempList = []
                                            # tempList.append(myLocalList[updateChoice])
                                            # )
                    except ValueError:
                        print("Invalid input, please try again!")

                elif userChoice == 4:
                    myLocalList = readCSVtoDict.funReadCSVtoDICT(inWriteFile)
                            # ----- Use emumerate() to do the same job as below -----------
                            # for listIndex in range(0, len(myLocalList)):  # listIndex
                            #      print(f'[{listIndex}]-->{myLocalList[listIndex]}')
                            # -------------------------------------------------------------
                    # for counter, dictValue in enumerate(myLocalList):
                    #     print(f'   [{counter}]-->{dictValue}')
                    myPrint.showListInTable(myLocalList)
                    getPropertyIndex = input("Please select the index from the above list for STRETCH update : ")
                    try:
                        getPropertyIndex = int(getPropertyIndex)
                        print(f'You select {myLocalList[getPropertyIndex]} to update')  # myLocalList[updateChoice] is the entire dictionary
                        
                        # Extract the Key and Value from the user's selected dictionary, then
                        # Loop through the properties
                        localCount = 0
                        for key, item in myLocalList[getPropertyIndex].items():  # Iterate through the selected dictionary
                            # print(f'   [{localCount}]-->{key} : {item}')  # Create a dynamic menu for selection (with index)
                            print(f'    {key} : {item}')  # Create a dynamic menu for selection (with index)
                            getPropertyToUpdate = input(f"Enter the property value for {key} to : ")
                            if (getPropertyToUpdate == ''):
                                print("Passed the update for this property!")
                            else: # the input index match!!!      (getPropertyIndex == itemList[key]):
                                if (key == 'customer_phone'):
                                    ## print(f'I am in cust_phone : {getPropertyToUpdate}')
                                    try:
                                        getPropertyToUpdate = int(getPropertyToUpdate)
                                    except:
                                        print(f"Invalid input of {key} and change no properties!!!, please try again!")
                                        break
                                else:
                                    pass
                                myLocalList[getPropertyIndex][key] = getPropertyToUpdate # Update the input property
                            localCount += 1  # move next property

                        # Write/Update back the results to csv file
                        updateDictToCSV.updateDictToCSV(myLocalList[getPropertyIndex], getPropertyIndex, inWriteFile, inWriteHeader)
                    except ValueError:
                        print(f'Invalid input of {getPropertyIndex}, please try again!')

                elif userChoice == 5:  # Delete order based on user's selection
                    myLocalList = readCSVtoDict.funReadCSVtoDICT(inWriteFile)
                    # for listIndex in range(0, len(myLocalList)):  # listIndex
                    #      print(f'   [{listIndex}]-->{myLocalList[listIndex]}')
                    myPrint.showListInTable(myLocalList)

                    updateChoice = input("Please select the index from the above list for delete : ")
                    try:
                        updateChoice = int(updateChoice)
                        print(f'You select {myLocalList[updateChoice]} to delete')  # myLocalList[updateChoice] is the entire dictionary
                        #
                        # print(f'{updateProperty}-->{myLocalList[updateChoice][updateProperty]}')
                        #

                        STATUS = deleteDictToCSV.deleteDictToCSV(myLocalList[updateChoice], updateChoice, inWriteFile, inWriteHeader)
                    except ValueError:
                        print("Invalid input, please try again")
            else:
                print("Order Menu : Invalid input, try again.")
                # Continue to order menu
    except:
        traceback.print_exc()    
    return userChoice