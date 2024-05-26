# Prints out the display menus
import time

def mainMenu():
    print()
    print("-"*99)
    time.sleep(0.05)
    print("1. Search using Subject Code")
    time.sleep(0.05)
    print("2. Add Subject")
    time.sleep(0.05)
    print("3. Edit Subject")
    time.sleep(0.05)
    print("4. Delete Subject")
    time.sleep(0.05)
    print("5. Load Data")
    time.sleep(0.05)
    print("6. Save Data")
    time.sleep(0.05)
    print("7. Exit")
    time.sleep(0.05)
    print("-"*99)
    time.sleep(0.05)
    print("Enter your choice [1-7]: ")

def searchMenu():
    print()
    print("-"*99)
    time.sleep(0.05)
    print("Search by:")

    print("1. 4-Digit Subject Code")
    time.sleep(0.05)
    print("2. Subject Name")
    time.sleep(0.05)
    print("3. Exit")
    time.sleep(0.05)
    print("-"*99)

def searchOpt1():
    print()
    print("-"*99)
    time.sleep(0.05)
    print("Enter the 4-digit Subject Code: ")

def searchOpt2():
    print()
    print("-"*99)
    time.sleep(0.05)
    print("Enter the Subject Name: ")

def addMenu():
    print()
    print("-"*99)
    time.sleep(0.05)
    print("Enter the Subject's 4-Digit Code")

def editMenu():
    print()
    print("-"*99)
    time.sleep(0.05)
    print("Enter the Subject's 4-Digit Code")

def deleteMenu():
    print()
    print("-"*99)
    time.sleep(0.05)
    print("Enter the Subject's 4-Digit Code")

def loadMenu():
    print()
    print("-"*99)
    time.sleep(0.05)
    print("Enter the File's Name [""example.dat""]")

def saveMenu():
    print()
    print("-"*99)
    time.sleep(0.05)
    print("Enter the File's Name [""example.dat""]")
    time.sleep(1)