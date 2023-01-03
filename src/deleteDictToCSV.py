# This is the mini-project week4 ------------------------------------------------------------------------------
# File Name     : deleteDictToCSV.py
# Date          : 12 Nov 2022
# Developer     : Samuel KO
# Description   : This function will remove the selected item from the product csv file.
#               : Based on the passed in dictionary, dictionary index, file type and 
#               : file header, the function will match the file to delete the selected
#               : record.
# Input         : inDict, inIndex, inFile and inHeader
# Output        : Return the 1) OK and 2) NOT_OK status to the caller function
# -------------------------------------------------------------------------------------------------------------

import csv
import traceback
import readCSVtoDict
import printListToTableFormat as myPrint

def deleteDictToCSV(inDict, inIndex, inFile, inHeader):
    localList = []
    STATUS = 'NOT_OK'
    fields = inHeader.split(',') # Convert str to list

    localList = readCSVtoDict.funReadCSVtoDICT(inFile)

    localList.remove(localList[inIndex])

    try:
        with open(inFile, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(localList)  # for writing entire rows to file, its faster!!!!

            # It can also be done by wriing row in iteration....
            # for data in localList:
            #     writer.writerow(data)

            STATUS = 'OK'
    except:
        traceback.print_exc()

    print(f'Revised list after {inDict} deleted as below :')
    myPrint.showListInTable(localList)

    return STATUS
