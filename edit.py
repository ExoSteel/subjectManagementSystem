# Edits one subject
import time

def displaySubs(subjects):
    if subjects == []:
        print("There are no subjects loaded into the system currently.")
        return False
    else:
        count = 1
        for subject in subjects:
            print(count, subject)
            time.sleep(0.05)
            count += 1
    return count - 1

def decompose(subjects, subjectIndex):
    subject = subjects[subjectIndex]
    subComponents = subject.split("|")
    return subComponents

def replace(subjects, subjectIndex, newDetails):
    newSubject = "|".join(newDetails)
    subjects.pop(subjectIndex)
    subjects.insert(subjectIndex, newSubject)

    return subjects