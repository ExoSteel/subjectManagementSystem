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
        if subjects == []:
            print()
            print("There are no subjects loaded into the system currently.")
            continue
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
        display.addSCMenu()
        subjectCode = input()
        if not validator.validate(subjectCode, int, None, None, 4): 
            print("Wrong input, input must be a 4-digit code!")
            continue

        display.addSNMenu()
        subjectName = input()
        if not validator.validate(subjectName, str): 
            print("Wrong input, input must be a string!")
            continue

        display.addSTMenu()
        subjectType = input()
        if not validator.validate(subjectType, str, None, None, 1, None, ["A", "P"]): 
            print("Wrong input, input must either be P or A!")
            continue
            
        if subjectType == "A":
            display.addP1Menu()
            P1Len = input()
            if not validator.validate(P1Len, float, None, None, 0, None, ["2.0", "2.5", "3.0"]): 
                print("Wrong input, input must be 2.0, 2.5 or 3.0!")
                continue

            display.addP2Menu()
            P2Len = input()
            if not validator.validate(P2Len, float, None, None, 0, None, ["2.0", "2.5", "3.0"]): 
                print("Wrong input, input must be 2.0, 2.5 or 3.0!")
                continue
            subjects.append(addSubject.add(subjectCode, subjectName, subjectType, P1Len=P1Len, P2Len=P2Len))
        else:
            display.addPracMenu()
            PracLen = input()
            if not validator.validate(PracLen, float, 10.0, 40.0): 
                print("Wrong input, input must be between 10.0 and 40.0!")
                continue

            display.addCDMenu()
            CDate = input()
            if not validator.validate(CDate, int, None, None, 6, "date"): 
                print("Wrong input, input must be in YYMMDD format!")
                continue
            subjects.append(addSubject.add(subjectCode, subjectName, subjectType, PracLen=PracLen, CDate=CDate))

    elif choice == "3":
        display.pickMenu("edit")
        Ubound = edit.displaySubs(subjects)
        if not Ubound:
            continue
        subjectIndex = input()
        if not validator.validate(subjectIndex, int, 1, Ubound):
            print(f"Wrong input, input must be an integer between 1 and {Ubound}!")
            continue
        
        subjectCode, subjectName, subjectType, P1Len, P2Len, PracLen, CDate = edit.decompose(subjects, int(subjectIndex) - 1)

        display.editMenu(subjectType)
        toChange = input()
        if not validator.validate(toChange, int, 1, 5):
            print("Wrong input, input must be between 1 and 5!")
            continue
        
        if toChange == "1":
            display.addSCMenu()
            subjectCode = input()
            if not validator.validate(subjectCode, int, None, None, 4): 
                print("Wrong input, input must be a 4-digit code!")
                continue
        elif toChange == "2":
            display.addSNMenu()
            subjectName = input()
            if not validator.validate(subjectName, str): 
                print("Wrong input, input must be a string!")
                continue
        elif toChange == "3":
            display.addSTMenu()
            subjectType = input()
            if not validator.validate(subjectType, str, None, None, 1, None, ["A", "P"]): 
                print("Wrong input, input must either be A or P!")
                continue
        if format == "A":
            if toChange == "4":
                display.addP1Menu()
                P1Len = input()
                if not validator.validate(P1Len, float, None, None, 0, None, ["2.0", "2.5", "3.0"]): 
                    print("Wrong input, input must be 2.0, 2.5 or 3.0!")
                    continue
            else:
                display.addP2Menu()
                P2Len = input()
                if not validator.validate(P2Len, float, None, None, 0, None, ["2.0", "2.5", "3.0"]): 
                    print("Wrong input, input must be 2.0, 2.5 or 3.0!")
                    continue
        else:
            if toChange == "4":
                display.addPracMenu()
                PracLen = input()
                if not validator.validate(PracLen, float, 10.0, 40.0): 
                    print("Wrong input, input must be between 10.0 and 40.0!")
                    continue
            else:
                display.addCDMenu()
                CDate = input()
                if not validator.validate(CDate, int, None, None, 6, "date"): 
                    print("Wrong input, input must be in YYMMDD format!")
                    continue

        newDetails = [subjectCode, subjectName, subjectType, P1Len, P2Len, PracLen, CDate]
        subjects = edit.replace(subjects, int(subjectIndex) - 1, newDetails)

    elif choice == "4":
        display.pickMenu("delete")
        Ubound = edit.displaySubs(subjects)
        if not Ubound:
            continue
        subjectIndex = input()
        if not validator.validate(subjectIndex, int, 1, Ubound):
            print(f"Wrong input, input must be an integer between 1 and {Ubound}!")
            continue

        subjects = delete.delete(subjects, int(subjectIndex) - 1)

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