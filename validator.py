# Combines all of the data validation checks together
import re

def validate(data, type=None, lBound=None, uBound=None, length=0, format=None, existence=[]):
    flag = True
    if data == None or data == "":                                      # Presence Check
        flag = False
    
    if type != None:
        if type == int:                                                 # Type Check - Integer
            if not data.isdigit():
                return False
        elif type == str:                                               # Type Check - String
            try:
                data.isalnum()
            except:
                return False
        elif type == float:
            try:
                float(data)
            except:
                return False

    if lBound != None and uBound != None:
        if not (float(data) >= lBound and float(data) <= uBound):         # Range Check
            return False   
    
    if length != 0:
        if len(data) != length:                                         # Length Check
            return False                       
    
    if format != None:
        if format == "date":
            if not (format[2:4] >= 1 and format[2:4] <= 12):
                return False 
            elif not (format[4:6] >= 1 and format[4:6] <= 31):
                return False
        if re.search(format, data) == None:                             # Format Check (using RegEx)
            return False                   

    if existence != []:                                                 # Existence Check
        for exist in existence:
            if data != exist:
                return False
    
    return flag

'''
# Test
print(validate("1")) # True
print(validate(None)) # False
print(validate("1", int)) # True
print(validate("1", str)) # True
print(validate("1", None, 0, 9)) # True
print(validate("1", None, -5, 0)) # False
print(validate("1", None, 0, 9, 1)) # True
print(validate("1", None, 0, 9, 5)) # False
print(validate("1", None, 0, 9, 0, "\d")) # True
print(validate("1", None, 0, 9, 0, "\d\d")) # False
print(validate("1", None, 0, 9, 0, None, ["1"])) # True
print(validate("1", None, 0, 9, 0, None, ["1", "2"])) # False
'''
