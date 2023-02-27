
# This is the mini-project week4 ------------------------------------------------------------------------------
# File Name     : printListToTableFormat.py
# Date          : 20 Nov 2022
# Developer     : Samuel KO
# Description   : Print the input list and output it to table format
# Input         : inList, the list of dictionary for print
# Output        : None
# -------------------------------------------------------------------------------------------------------------

from tabulate import tabulate

def showListInTable(inList):
    print()
    print(tabulate(tuple(inList), headers="keys", showindex="always"))
    # print(tabulate(tuple(inList), showindex="always",tablefmt="github"))
    print()