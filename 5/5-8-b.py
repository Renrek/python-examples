FILE_PATH = "C:/Users/rogue/Desktop/3-5-App-Dev/library/" #Win10-VSCode
#FILE_PATH = "" #PythonAnywhere

def main():
    #Outline
    rates = getRatesFromFile()
    exchangeRatesByUSDollar = getExchangeRatesByUSDollar(rates)
    printExchangeRateInfo(exchangeRatesByUSDollar)

def getRatesFromFile():
    infile = open(FILE_PATH + "Exchrate.txt", 'r')
    ratesList = [line.rstrip().split(',') for line in infile]
    infile.close()
    return ratesList

def getExchangeRatesByUSDollar(exchangeIndex:list):
    return sorted(exchangeIndex, key=lambda k: float(k[2]))

def printExchangeRateInfo(exchangeRate:list):
    print() #Please note that book shows Australia, however file has Austria
    for line in exchangeRate:
        print(line[0])

main()