# This is the mini-project week4
# File Name     : readCSVtoDict.py
# Date          : 12 Nov 2022
# Developer     : Samuel KO

# input  : name of csv file
# output : return an object of dictionory in list
import csv 
import traceback

def funReadCSVtoDICT(filename):    
    myList = []
    try:
        with open(filename, mode ='r') as csvFile: 
            # opening the file using "with"
            # statement
            for line in csv.DictReader(csvFile):
                # print(line)
                myList.append(line)
            # print(myList)  # debug statement
        return myList # return a list of dictionary
    except:
        traceback.print_exc()# funReadCSVtoDICT() 