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
        flag = True if int(data) >= lBound and int(data) <= uBound else False # Range Check
    
    if length != 0:
        flag = True if len(data) == length else False # Length Check
    
    if format != None:
        flag = True if re.search(format, data) else False # Format Check (using RegEx)

    if existence != []: # Existence Check
        for exist in existence:
            flag = True if data == exist else False
    
    return flag

'''
# Test
print(validate(None)) # False
print(validate("1", int)) # True
print(validate("1", str)) # True
print(validate("1", None, 0, 9)) # True
print(validate("1", None, -5, 0)) # False
print(validate("1", None, 0, 0, 1)) # True
print(validate("1", None, 0, 0, 5)) # False
print(validate("1", None, 0, 0, 0, "\d")) # True
print(validate("1", None, 0, 0, 0, "\d\d")) # False
print(validate("1", None, 0, 0, 0, None, ["1"])) # True
print(validate("1", None, 0, 0, 0, None, ["1", "2"])) # False
'''
