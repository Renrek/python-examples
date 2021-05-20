FILE_PATH = "library/"

def main():

    #Outline
    userInput = getUserInput()
    rates = getRatesFromFile()
    exchangeRate = getExchangeRate(userInput,rates)
    printExchangeRateInfo(exchangeRate)
    
def getUserInput():
    return str(input("Enter the name of a country: ")).strip().capitalize()

def getRatesFromFile():
    infile = open(FILE_PATH + "Exchrate.txt", 'r')
    ratesList = [line.rstrip().split(',') for line in infile]
    infile.close()
    return ratesList

def getExchangeRate(country:str, exchangeIndex:list):
    for line in exchangeIndex:
        if country == line[0]:
            return line

def printExchangeRateInfo(exchangeRate:list):
    print("Currency: "+exchangeRate[1])
    print("Exchange rate: "+exchangeRate[2])
 
main()