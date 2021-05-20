FILE_PATH = "library/"

def main():
    #Outline
    rates = getRatesFromFile()
    userInput = getUserInput()
    exchangePayload = getExchangePayload(userInput, rates)
    printExchangeRatePayload(exchangePayload)
    
def getUserInput():
    firstCountry = str(input("Enter the name of first country: ")).strip()
    secondCountry = str(input("Enter the name of first country: ")).strip()
    amount = int(input("Amount of money to convert: "))
    return (amount, (firstCountry, secondCountry))

def getRatesFromFile():
    infile = open(FILE_PATH + "Exchrate.txt", 'r')
    ratesList = [line.rstrip().split(',') for line in infile]
    infile.close()
    return ratesList

def getExchangePayload(userInput:tuple, rates:list): 
    #Tuple map expected: userInput = 
    #(amount, ('America', secondCountry))
    firstCountry = getExchangeRate(userInput[1][0], rates)
    secondCountry = getExchangeRate(userInput[1][1], rates)
    amount = userInput[0]
    result = (float(firstCountry[2]) * float(secondCountry[2])) * amount
    return (firstCountry,secondCountry,amount, result)
    
def getExchangeRate(country:str, rates:list):
    for line in rates:
        if country == line[0]:
            return line

def printExchangeRatePayload(item:tuple):
    #Tuple map expected: item = 
    #(['America', 'Dollar', '1'],['Chile', 'Peso', '591.4077'], 100.0, 59140.77)
    print(str(item[2])+" "+ item[0][1].lower() +"s from "+ item[0][0] + 
            " equals {0:,.2f}".format(item[3]) + " " + item[1][1].lower() +"s from "+ item[1][0])
 
main()