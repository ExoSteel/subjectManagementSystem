# Edits one subject

def displaySubs(subjects):
    if subjects == []:
        print("There are no subjects loaded into the system currently.")
        return False
    else:
        count = 1
        for subject in subjects:
            print(count, subject)
            count += 1
    return count