# Adds Subject

def add(subjectCode, subjectName, subjectType, P1Len=0.0, P2Len=0.0, PracLen=0.0, CDate="001231"):
    formatted = subjectCode + "|" + subjectName + "|" + subjectType + "|" + P1Len + "|" + P2Len + "|" + PracLen + "|" + CDate

    print(subjectName + " has been added")
    return formatted