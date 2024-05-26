# Loads Data from .bat file

def load(fileName, subjects):
    count = 0
    with open(fileName) as infile:
        loadedSubject = infile.readlines()
        subjects.append(loadedSubject)
        count += 1
    print(count, "subjects has been loaded")