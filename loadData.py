# Loads Data from .bat file

def load(fileName, subjects):
    count = 0
    try:
        with open(fileName, "tr") as infile:
            loadedSubject = infile.read().split("\n")
        header = int(loadedSubject[0].split( )[0])
        for subject in loadedSubject[1:]:
            if subject == "":
                loadedSubject.pop()
                continue
            count += 1
        if count == header:
            subjects += loadedSubject[1:]
            print(count, "subjects has been loaded")
            return subjects
        print("Number of subjects does not match the batch header count, ABORTING IMPORT")
        return subjects
    except:
        print("File does not exist")
        return subjects