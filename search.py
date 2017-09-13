#!/bin/python
import os
import sys

fail = 0
matches = 0
skipped = 0
totalFiles = 0

def main(filePath, pattern):
    if os.path.isfile(filePath):
        searchInFile(filePath, pattern)
    elif os.path.isdir(filePath):
        buff = os.walk(filePath)
        for line in buff:              # in buff: rootDir, dirNames, filesNames as list
            i = 0
            files = line[2]
            for element in files:
                fullFilePath = str(line[0]) + "/" + str(files[i])
                searchInFile(fullFilePath, pattern)
                i += 1
            # multi Threading ? each file one thread
    else:
        sys.exit("what the fuck I got here?")
        
    print("\nTotal files searched:\t\t" + str(totalFiles))
    print("Total matches:\t\t\t" + str(matches))
    print("skipped lines (too long):\t" + str(skipped))
    print("couldn't open " + str(fail) + " files")

def searchInFile(fileName, word):
    global matches
    global fail
    global skipped
    global totalFiles
    try:
        totalFiles += 1
        f = open(fileName, 'r')
        for line in f:
            if len(line) > 100:
                skipped += 1
                continue
            if word in line:
                print(str(matches+1) + ". Match in: \""+ fileName + "\" -->\t" + str(line.strip('\n')))
                matches += 1
    except Exception:
        fail += 1
        pass



if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Usage: $prog <pathToFile> <WordOrString>")
    main(sys.argv[1], sys.argv[2])
