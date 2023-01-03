# This is the mini-project week4 ------------------------------------------------------------------------------
# File Name     : test_funReadCSVtoDict.py
# Date          : 19 Nov 2022
# Developer     : Samuel KO
# Description   : This function receives four parameters.  The function will base
#               : on the pass in dictionary, the record index to indicate the
#                 position of the data that want to be updated.  Also, use the inFile
#                 and the inHeader to help the update process
# Input         : Pass in parameters 1) dictionary 2) file name 3) file header
# Output        : Print the updated list to the console for verification.   No
#                 printing if the operation fail
# -------------------------------------------------------------------------------------------------------------

import pytest
from chkItemExist import isExist

def test_isExist():
    # Arrange
    inList = [{'prodName': 'English Tea', 'price': 1.85},
                {'prodName': 'Whisky', 'price': 21.99},
                {'prodName': 'Pespi 1L', 'price': 0.99},
                {'prodName': 'Coke Zero', 'price': 2.99}]
    
    # Act
    # inList = [{'prodName': 'English Tea', 'price'}]  # abnormal data set
    inName = 'Whisky'
    inMenu = 'PRODUCT_MENU'
    result = True

    # Assert
    assert isExist(inList, inName, inMenu) == result
