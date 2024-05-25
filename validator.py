# Combines all of the data validation checks together
import re

def validate(data, type=None, lBound=None, uBound=None, length=0, format=None, existence=[]):
    flag = True
    if data == None or data == "": # Presence Check
        flag = False
    
    if type != None:
        if type == int: # Type Check - Integer
            flag = data.isdigit()
        elif type == str: # Type Check - String
            try:
                flag = data.isalnum()
            except:
                flag = False

    if lBound != None and uBound != None:
        flag = True if data >= lBound and data <= uBound else False # Range Check
    
    if length != 0:
        flag = True if len(data) == length else False # Length Check
    
    if format != None:
        flag = True if re.search(format, data) else False # Format Check (using RegEx)

    if existence != []: # Existence Check
        for exist in existence:
            flag = True if data == exist else False
    
    return flag