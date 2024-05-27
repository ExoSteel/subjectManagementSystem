# Deletes chosen subject from system

def delete(subjects, subjectIndex):
    subjectName = subjects[subjectIndex].split("|")[1]
    print(subjectName + " has successfully been removed.")
    
    subjects.pop(subjectIndex)

    return subjects