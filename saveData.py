# Saves Data in a .DAT file
import datetime as datetime

def save(data, fileName):
    with open(fileName, "tw") as outfile:
        outfile.write(str(len(data)) + " " + str(datetime.datetime.now()).split(" ")[0])
        for subject in data:
            outfile.write("\n" + subject)

    print("Data has been saved!")