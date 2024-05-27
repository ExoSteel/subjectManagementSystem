# Search database for subject

def search(subjectCode="", subjectName="", subjects=[]):
    found = []
    if subjects == []:
        return "Currently, there is no data loaded into the system"
    elif subjectCode != "":                                             # Using Subject Code to Search
        for subject in subjects:
            if subjectCode == subject[0:4]:
                found.append(subject)
    else:                                                               # Using Subject Name to Search
        for subject in subjects:
            subjectDetails = subject.split("|")
            if subjectName == subjectDetails[1]:
                found.append(subject)
    return found if len(found) > 0 else "No Subject Found"
