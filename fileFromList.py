
FILE_PATH = "library/"

def main():
    #Input from file while appending win percentage
    teamRoster = createListFromFile(FILE_PATH+"ALE.txt")
    #Sort by last column of list in decendering order
    sortedTeamRoster = sorted(teamRoster, key= lambda x:x[3], reverse=True)
    #Unceremoniously dump list into new file
    createFileFromList(sortedTeamRoster)

def createListFromFile(file):
    teams = []
    infile = open(file, 'r')
    for line in infile:
        article = line.rstrip().split(',')
        winPercent = round(float(article[1]) / (float(article[2]) + float(article[1])), 3)
        teams.append([article[0],article[1],article[2], winPercent])
    infile.close()
    return teams

def createFileFromList(list:list):
    outfile = open(FILE_PATH+"ALE_Standings.txt", 'w')
    for line in list:
        outfile.write(line[0]+", "+line[1]+", "+line[2]+", "+str(line[3])+"\n")
    outfile.close()
main()