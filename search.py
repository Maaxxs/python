#!/bin/python
import os
import sys
import platform

fail = 0
matches = 0
skipped = 0
totalFiles = 0
blocked = 0

def main(filePath, pattern):
    global blocked
    global totalFiles
    forbidden = [".jpg", ".jpeg", ".png", ".mkv", ".mp4", ".gif", ".pdf"]
    pf = platform.system()

    if os.path.isfile(filePath):
        searchInFile(filePath, pattern)
    elif os.path.isdir(filePath):
        buff = os.walk(filePath)
        for line in buff:              # in buff: rootDir, dirNames, filesNames as list
            files = line[2]
            for element in files:
                totalFiles += 1
                for i in range(len(forbidden)):
                    if forbidden[i] in element:
                        blocked += 1
                        break   # beende aktuelle for schleife
                else:
                    if pf == "Linux":
                        fullFilePath = str(line[0]) + "/" + str(element)
                        searchInFile(fullFilePath, pattern)
                    elif pf == "Windows":
                        fullFilePath = str(line[0]) + "\\" + str(element)
                        searchInFile(fullFilePath, pattern)

            # multi Threading ? each file one thread
    else:
        sys.exit("what the fuck I got here?")

    print("\nTotal files found:\t\t" + str(totalFiles))
    print("Total matches:\t\t\t" + str(matches))
    print("skipped lines (too long):\t" + str(skipped))
    print("blocked files: \t\t\t" + str(blocked))
    print("unable to open files:\t\t" + str(fail))

def searchInFile(fileName, word):
    global matches
    global fail
    global skipped
    global totalFiles
    try:
        f = open(fileName, 'r')
        for line in f:
            if len(line) > 100:
                skipped += 1
                continue    # test next element in for loop
            if word in line:
                print(str(matches+1) + ". Match in: \""+ fileName + "\" -->\t" + str(line.strip('\n')))
                matches += 1
    except Exception:
        fail += 1


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Usage: $prog <pathToFileOrFolder> <WordOrString>")
    main(sys.argv[1], sys.argv[2])
