import search, addSubject, edit, delete, display, loadData,saveData
from Validation import typeCheck, formatCheck, existenceCheck, batchHeaderCheck, lengthCheck, presenceCheck, rangeCheck
from datetime import datetime

running = True
subjects = [] # 2D Array storing all currently loaded data

while running:
    display.mainMenu()
    choice = input()
    if not (typeCheck.check(choice, int) and rangeCheck.check(int(choice), 1, 7)):
        print("Wrong input, input must be an integer between 1 and 7!")
        continue
    if choice == "1":
        display.searchMenu()
        subjectCode = input()
        search.
    if choice == "2":
        display.addMenu()
        subjectCode = input()
    if choice == "3":
        display.editMenu()
        subjectCode = input()
    if choice == "4":
        display.deleteMenu()
        subjectCode = input()
    if choice == "5":
        display.loadMenu()
        subjectCode = input()
    if choice == "6":
        display.saveMenu()
    if choice == "7":
        print()
        print("Goodbye!")
        break