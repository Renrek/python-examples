import random

class MovieSelecter:
    def __init__(self, movieCatalog):
        self._movieList = []
        self._movieCatalog = movieCatalog

    def fetchRandom(self):
        self._movieList.clear()
        try:
            del self._movieCatalog['Title']
            self._movieList = list(self._movieCatalog.keys())
            return random.choice(self._movieList)
        except KeyError:
            print()
            print('"Title" must be in cell A1')
            print("Please correct and try again.")
    
    #By anticipation (Scale: 1-10) per user
    def listTopTen(self):
        self._movieList.clear()
        try:
            del self._movieCatalog['Title']
            for line in self._movieCatalog:
                #Weight is bases on total anticipation for movie
                self._movieList.append([line, sum(map(int, self._movieCatalog[line]))])
            self._movieList = sorted(self._movieList, key=lambda k: int(k[1]), reverse=True)
            topTen = []
            for movie in self._movieList[:10]:
                topTen.append(movie[0])
            return topTen
        except KeyError:
            print()
            print('"Title" must be in cell A1')
            print("Please correct and try again.")

    def fetchRandomFromTopTen(self):
        return random.choice(self.listTopTen())
            
        

       
  

    