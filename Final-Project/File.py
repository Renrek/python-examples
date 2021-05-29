class File:
    def __init__(self, fileName):
        self._fileName = fileName
        self._movieRoster = {} #Returnable
        self.fetch() #Prepare data before being its called

    #Main purpose, takes into concideration of user/column flexablity
    def fetch(self):
        try:
            infile = open(self._fileName, 'r')
            for line in infile:
                line = line.rstrip().split(',')
                key, value = line[0], line[1:]
                #Dict Format - {Title : [User, User,..]} to utilize dict functions
                self._movieRoster[key] = value
            infile.close() 
        except FileNotFoundError:
            print("*******************************************")
            print("No file found, please ensure a file exists!")
            print("*******************************************")
    
    #Delete movie from list then update the file
    def removeMovie(self, movieTitle):
        del self._movieRoster[movieTitle]
        self.update()
        print()
        print(movieTitle + " was removed from your list.")

    #Updates file with modified information user/column flexable
    def update(self):
        outfile = open(self._fileName, 'w')
        for line in self._movieRoster:
            row = line
            for element in self._movieRoster[line]:
                row = row + "," + element
            outfile.write(row+"\n")
        outfile.close()
    
    #Returns movie catalog
    def getCatalog(self):
        return self._movieRoster
        