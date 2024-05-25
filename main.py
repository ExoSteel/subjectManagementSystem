import search, addSubject, edit, delete, display, loadData, saveData, validator
from datetime import datetime

running = True
subjects = [] # 2D Array storing all currently loaded data

while running:
    display.mainMenu()
    choice = input()
    if not validator.validate(choice, int, 1, 7):
        print("Wrong input, input must be an integer between 1 and 7!")
        continue
    if choice == "1":
        display.searchMenu()
        subjectCode = input()
    elif choice == "2":
        display.addMenu()
        subjectCode = input()
    elif choice == "3":
        display.editMenu()
        subjectCode = input()
    elif choice == "4":
        display.deleteMenu()
        subjectCode = input()
    elif choice == "5":
        display.loadMenu()
        subjectCode = input()
    elif choice == "6":
        display.saveMenu()
    else:
        print()
        print("Goodbye!")
        break