FILE_PATH = "C:/Users/rogue/Desktop/3-5-App-Dev/library/" #Win10-VSCode
#FILE_PATH = ""

def main():

    unitConvertions = createDictionary(getFilePath())
    printMeasurementLegend(unitConvertions)
    userInput = getUserInput()
    printLengthConverstion(userInput, unitConvertions)

def getFilePath(): #Change FILE_PATH to reflect system file location
    return FILE_PATH+"Units.txt"

def createDictionary(file):#Copied from book, why reinvent it.
    infile = open(file, 'r')
    textList = [line.rstrip() for line in infile]
    infile.close()
    return dict([x.split(',') for x in textList])

#File could always change, make legend flexable by printing keys
def printMeasurementLegend(data:dict):
    print()
    keys = list(data.keys())
    legendWidth = 15
    index = 0
    print("UNITS OF LENGTH")
    for option in keys:
        print(option.ljust(legendWidth), end='')
        index += 1
        if index == 3:
            print("")
            index = 0
    print()

def getUserInput():
    unitFrom = input(str("Units to convert from: ")).lower()
    unitTo = input(str("Units to convert to: ")).lower()
    unitCount = input(str("Enter length in "+unitFrom+": "))
    userInput = {
        "unitFrom":unitFrom,
        "unitTo":unitTo,
        "unitCount":unitCount
    }
    return userInput

def printLengthConverstion(userData:dict, referanceData:dict):
    # total units * (original unit / target unit)
    converted = (float(userData["unitCount"]) * \
        float(referanceData[userData["unitFrom"]])) / \
        float(referanceData[userData["unitTo"]])
    print("Length in "+ userData["unitTo"]+": "+str(round(converted, 4)))

main()