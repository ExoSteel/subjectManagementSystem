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

def addSCMenu():
    print()
    print("-"*99)
    time.sleep(0.05)
    print("Adding a new Subject Record: ")
    time.sleep(0.05)
    print("-"*99)
    print("Enter the Subject's 4-Digit Code ")

def addSNMenu():
    print()
    time.sleep(0.05)
    print("Enter the Subject's Name ")

def addSTMenu():
    print()
    time.sleep(0.05)
    print("Enter the Subject's Type [A or P] ")

def addP1Menu():
    print()
    time.sleep(0.05)
    print("Enter the Subject's Paper 1 Length [2.0, 2.5 or 3.0] ")

def addP2Menu():
    print()
    time.sleep(0.05)
    print("Enter the Subject's Paper 2 Length [2.0, 2.5 or 3.0] ")

def addPracMenu():
    print()
    time.sleep(0.05)
    print("Enter the Subject's Practical Length [10.0 - 40.0] ")

def addCDMenu():
    print()
    time.sleep(0.05)
    print("Enter the Subject's Final Deadline [YYMMDD] ")

def pickMenu(modifier):
    print()
    print("-"*99)
    time.sleep(0.05)
    print(f"Which subject would you like to {modifier}?")

def editMenu(format):
    print()
    print("-"*99)
    time.sleep(0.05)
    print("Which component would you like to edit?")
    time.sleep(0.05)
    print("1. Subject Code")
    time.sleep(0.05)
    print("2. Subject Name")
    time.sleep(0.05)
    print("3. Subject Type")
    time.sleep(0.05)
    if format == "A":
        print("4. P1 Length")
        time.sleep(0.05)
        print("5. P2 Length")
        time.sleep(0.05)
    else:
        print("4. Practical Length")
        time.sleep(0.05)
        print("5. Final Deadline Date")
        time.sleep(0.05)
    print("-"*99)

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