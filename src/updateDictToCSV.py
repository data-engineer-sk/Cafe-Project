# This is the mini-project week4 ------------------------------------------------------------------------------
# File Name     : updateDictToCSV.py
# Date          : 12 Nov 2022
# Developer     : Samuel KO
# Description   : This function receives four parameters.  The function will base
#               : on the pass in dictionary, the record index to indicate the
#                 position of the data that want to be updated.  Also, use the inFile
#                 and the inHeader to help the update process
# Input         : Pass in parameters 1) dictionary 2) file name 3) file header
# Output        : Print the updated list to the console for verification.   No
#                 printing if the operation fail
# -------------------------------------------------------------------------------------------------------------

import csv
import traceback
import readCSVtoDict
import printListToTableFormat as myPrint

def updateDictToCSV(inDict, inIndex, inFile, inHeader):
    localList = []

    fields = inHeader.split(',') # Convert str to list

    localList = readCSVtoDict.funReadCSVtoDICT(inFile)

    localList[inIndex]= inDict

    try:
        with open(inFile, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for data in localList:
                writer.writerow(data)
    except:
        traceback.print_exc()

    print(f'The information has been updated as below : ')
    # for counter, item in enumerate(localList):
    #     print(f'  [{counter}]=-->{item}')
    myPrint.showListInTable(localList)


