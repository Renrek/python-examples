FILE_PATH = "library/"

def main():
    study = getStudyFromFile()
    printPayload(study)

def getStudyFromFile():
    studyResults = {}
    infile = open(FILE_PATH + "Mileage.txt", 'r')
    studyList = [line.rstrip() for line in infile]
    infile.close()
    #Using the formation of a dict to remove duplicate entries
    #then a tuple to easlily iterate through
    models = tuple(dict([x.split(',') for x in studyList]))
    for model in models:
        gallons = 0
        count = 0
        for line in [x.split(',') for x in studyList]:
            if line[0] == model:
                gallons += float(line[1])
                count += 1
        #make dictionary {model:(test vehicle count , total gallons used)}
        studyResults.update({model : (int(count), float(gallons))})
    return studyResults

def printPayload(study:dict):
    width = 8 #width of columns
    payLoad = []
    print()
    print("Model".ljust(width), "MPG".ljust(width))
    for model in study:
        payLoad.append((model, round((study[model][0] / study[model][1])*(100),2)))
    payLoad = (sorted(payLoad, key=lambda k: k[1], reverse=True))
    for element in payLoad:
        print(element[0].ljust(width),"{0:,.2f}".format(element[1]).ljust(width))
        
main()