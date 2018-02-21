import random as r
import time
import sys

INTEGER_MAX_VALUE = sys.maxsize
INTEGER_MIN_VALUE = -1 * sys.maxsize - 1

def genOut():
    printString = ""
    copyCheck   = []
    if r.randint(0,10) < 3:
        return "Error: Error is happening"
    else:
        while len(copyCheck) < 100:
            xCoord   = r.randint(INTEGER_MIN_VALUE, INTEGER_MAX_VALUE)
            yCoord   = r.randint(INTEGER_MIN_VALUE, INTEGER_MAX_VALUE)
            newCoord = "(" + str(xCoord) + "," + str(yCoord) + ")"
            if (newCoord not in copyCheck):
                copyCheck.append(newCoord)
                printString += newCoord

                if len(copyCheck) == 99:
                    break

                printString += ","

        return printString

    # print "***************************"

if __name__ == '__main__':
    while True:
        printString = ""
        copyCheck   = []
        print "***************************"
        if r.randint(0,10) < 3:
            print "Error: Error is happening"
        else:
            while len(copyCheck) < 100:
                xCoord   = r.randint(INTEGER_MIN_VALUE, INTEGER_MAX_VALUE)
                yCoord   = r.randint(INTEGER_MIN_VALUE, INTEGER_MAX_VALUE)
                newCoord = "(" + str(xCoord) + "," + str(yCoord) + ")"
                if (newCoord not in copyCheck):
                    copyCheck.append(newCoord)
                    printString += newCoord

                    if len(copyCheck) == 99:
                        break

                    printString += ","

            print printString

    # print "***************************"
        time.sleep(2)
