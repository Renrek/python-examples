import nation
import pickle

FILE_PATH = "C:/Users/rogue/Desktop/3-7-App-Dev/library/" #Win10-VSCode
#FILE_PATH = "" #PythonAnywhere

def main():
    
    userSelectedNation = str(input("Enter a country: ")).strip()
    nations = getNations()
    print
    print("Continent: "+nations[userSelectedNation]._continent)
    print("Population: {:,.0f}".format(float(nations[userSelectedNation]._population) * 10**6))
    print("Area: {:,.2f}".format(float(nations[userSelectedNation]._landArea)) + " square miles")
    
def getNations():
    infile = open(FILE_PATH + 'nationsDict.dat', 'rb')
    return pickle.load(infile)

main()