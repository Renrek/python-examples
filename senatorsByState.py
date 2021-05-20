FILE_PATH = "library/"

def main():
    #Get user Input
    state = getState()
    #Get Senator Lists
    senators = getSenatorsFromFile("Senate114.txt")
    #Tally up party totals
    senatorsList = senatorsFromState(senators, state)
    #Print results
    printPayload(senatorsList)

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

def getState():
    state = str(input("Enter the name of a state: "))
    state = state.strip().capitalize()
    return state

def senatorsFromState(senatorList:list,state:str):
    senatorsFromState = []
    for line in senatorList:
        if line[1] == state:
            senatorsFromState.append(line[0])
    return senatorsFromState

def printPayload(senatorList:list):
    if len(senatorList) > 0:
        for senator in senatorList:
            print(senator)
    else:
        print("Please check your spelling or enter an approperate state.")

main()