FILE_PATH = "library/"

def main():
    #Get Senator Lists
    senators = getSenatorsFromFile("Senate114.txt")
    #Tally up party totals
    statesWithPartyControl = statesControlledByParty(senators)
    #Print results
    printPayload(statesWithPartyControl)

def getSenatorsFromFile(senateFileName):
    senators = []
    infile = open(FILE_PATH + senateFileName, 'r')
    for line in infile:
        line = line.rstrip().split(',')
        senators.append([str(line[0]).strip(),
                         str(line[1]).strip(),
                         str(line[2]).strip()])
    infile.close()
    return senators

def statesControlledByParty(senatorList:list):
    previousParty = ''
    previousState = ''
    republicans = 0
    democrats = 0
    independents = 0
    for line in senatorList:
        if line[1] == previousState and line[2] == previousParty:
            if line[2] == 'R':
                republicans += 1
            elif line[2] == 'D':
                democrats += 1
            elif line[2] == 'I':
                independents += 1
        previousState = line[1]
        previousParty = line[2]
    return {'republicans':republicans,
            'democrats':democrats,
            'independents':independents}

def printPayload(senatorTotals:dict):
    print("\nCount of States Controlled By Party Affiliation:")
    print("  Republicans: " + str(senatorTotals["republicans"]))
    print("  Democrats: " + str(senatorTotals["democrats"]))
    print("  Independents: " + str(senatorTotals["independents"]))
    print("  TOTAL: " + str(senatorTotals["republicans"] +
                                   senatorTotals["democrats"] +
                                   senatorTotals["independents"]))

main()