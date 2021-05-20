from .nation import nation
import pickle

FILE_PATH = "library/"

def main():
    print()
    userSelectedContinent = str(input("Enter a continent: ")).strip()
    #userSelectedContinent = "South America"
    nationsOfContinent = getNationsOfContinentOrderByPopDens(getNations(), userSelectedContinent)
    printFirstFiveNations(nationsOfContinent)
   
def getNations():
    infile = open(FILE_PATH + 'nationsDict.dat', 'rb')
    return pickle.load(infile)

def getNationsOfContinentOrderByPopDens(nations:dict, continent:str):
    nationsOfContinent = []
    for line in list(nations.values()): #Grab Nations and PopDens in a Continent
        if line._continent == continent:
            nationsOfContinent.append([line._name, line.popDensity()])
    nationsOfContinent.sort(reverse=True, key = lambda x: x[1]) #Order by PopDens
    return nationsOfContinent

def printFirstFiveNations(nations:list):
    for index in range(5): # 5 nations to be printed
        print("  "+nations[index][0])

main()