from .nation import nation
import pickle

FILE_PATH = "library/"

def main():
    createNationsDictionaryFile()
    #testPickles()

def createNationsDictionaryFile():
    nations = {}
    infile = open(FILE_PATH + 'UN.txt', 'r')
    for line in infile:
        line = line.rstrip().split(',')
        nations.update({str(line[0]).strip() : nation.Nation(
                        str(line[0]).strip(),
                        str(line[1]).strip(),
                        str(line[2]).strip(),
                        str(line[3]).strip())})
    infile.close()
    outfile = open(FILE_PATH + 'nationsDict.dat', 'wb')
    pickle.dump(nations, outfile)
    outfile.close()

def testPickles():
    infile = open(FILE_PATH + 'nationsDict.dat', 'rb')
    stuff = pickle.load(infile)
    print(stuff['Canada'])

main()