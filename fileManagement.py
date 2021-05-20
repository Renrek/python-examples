FILE_PATH = "library/"

def main():
    #Get Senator Lists
    originalSenators = getSenatorsFromFile("Senate113.txt")
    retiredSenators = getSenatorsFromFile("RetiredSen.txt")
    newSenators = getSenatorsFromFile("NewSen.txt")
    print(originalSenators)
    #Remove Retired Senators from RetiredSen.txt
    senatorRoster = removeSenatorsfromDict(originalSenators, retiredSenators)

    #Add New Senators NewSen.txt
    senatorRoster.update(newSenators)
    updatedSenate = unpackToList(senatorRoster)

    #Create File with Senator list arranged by state
    sortList(updatedSenate)
    #createFileFromList(updatedSenate)
    
    

def getSenatorsFromFile(file):
    senators = {} 
    infile = open(FILE_PATH + file, 'r')
    for line in infile:
        line = line.rstrip().split(',')
        key, value = line[0], line[1:]
        #Dict Format - {Senator : [State, Party]} to utilize dict functions
        senators[key] = value
    infile.close()
    return senators

def removeSenatorsfromDict(senatorDict:dict, senatorsLeaving:dict):
    for senator in senatorsLeaving:
        del senatorDict[senator]
    return senatorDict

def unpackToList(senatorDict): 
    senatorList = []
    for line in senatorDict:
        #Change dict: {Senator : [State, Party]} to list: [Senator, State, Party] 
        # to utilize list functions and prepare for document.
        #This one I had to noodle through, may not be elegant...
        senatorList.append([line, senatorDict.get(line)[0], senatorDict.get(line)[1]])
    return senatorList

def sortList(senatorsList:list):
    senatorsList.sort(key = lambda x: x[1])
    return senatorsList

def createFileFromList(list:list):
    outfile = open(FILE_PATH+"Senate114.txt", 'w')
    for line in list:
        outfile.write(line[0]+", "+line[1]+", "+line[2]+"\n")
    outfile.close()
        
main()