class Nation:
    def __init__(self, name, continent, population, landArea):
        self._name = name
        self._continent = continent
        self._population = population
        self._landArea = landArea
    
    def popDensity(self):
        #population_density = population/land_area
        #population was given in millions, multiplied 10^6 to have actual value
        #both were made floats, there was a landArea that was throwing a curve ball
        return (float(self._population) * 10**6) / float(self._landArea)

    #added for testing
    def __str__(self):
        return  str(self._name) + ' ' + str(self._continent) + ' ' + str(self._population) + ' ' + str(self._landArea)