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
        choice = input()
        if not validator.validate(choice, int, 1, 3):
            print("Wrong input, input must be an integer between 1 and 3!")
            continue

        if choice == "1":
            display.searchOpt1()
            subjectCode = input()
            if not validator.validate(subjectCode, int, None, None, 4): 
                print("Wrong input, input must be a 4-digit code!")
                continue
            found = search.search(subjectCode=subjectCode, subjects=subjects)
            print(found)

        elif choice == "2":
            display.searchOpt2()
            subjectName = input()
            if not validator.validate(subjectName, str): 
                print("Wrong input, input must be a string!")
                continue
            found = search.search(subjectName=subjectName, subjects=subjects)
            if found == list:
                [print(subject) for subject in found]
            else:
                print(found)

        else:
            continue

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
        fileName = input()
        if not validator.validate(fileName, str, None, None, 0, ".[Dd][Aa][Tt]"):
            print("File must be a .dat type!")
            continue
        subjects = loadData.load(fileName, subjects)

    elif choice == "6":
        display.saveMenu()
        fileName = input()
        if not validator.validate(fileName, str, None, None, 0, ".[Dd][Aa][Tt]"):
            print("File must be a .dat type!")
            continue
        saveData.save(subjects, fileName)

    else:
        print()
        print("Goodbye!")
        break