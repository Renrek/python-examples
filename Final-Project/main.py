FILENAME = "movies.csv"
FILE_PATH = "" #Win10-VSCode
#FILE_PATH = "" #PythonAnywhere

from File import File
from MovieSelecter import MovieSelecter

def main():
    print()
    print("Welcome to the Johansen Family Movie Night Assignment System")
    menu()

#Main Interface
def menu():
    movieMatrix = File(FILE_PATH + FILENAME) #Fetch info from file
    movieCatalog = movieMatrix.getCatalog() #Get Dict format of the information
    print()
    movieCount = str(len(movieCatalog)-1) #"Row" count except for the Title row

    #Main menu
    print("Current movies available: "+ movieCount)
    print()
    print("Please select from the following: ")
    print("L - List Top 10 most anticipated movies.")
    print("T - Random selection from Top 10 most anticipated.")
    print("C - Completely random selection")
    print("Q - Quit")
    operation = str(input("Select L T C or Q: ")).strip().upper()

    # List Top 10 Most anticipated movies
    if operation == "L": 
        index = 1
        print()
        for line in MovieSelecter(movieCatalog).listTopTen():
            print(str(index) +". "+line)
            index += 1
        print()
        input("Press enter to continue...")
        menu()
    
    # Random selection from Top 10 most anticipated
    elif operation == "T": 
        print()
        randomMovie = MovieSelecter(movieCatalog).fetchRandomFromTopTen()
        print('Looks like you are watching "'+ randomMovie+'" Tonight.')
        print()
        removeOption = str(input('Would you like to remove it from your list? Y or N: ')).strip().upper()
        if removeOption == 'Y':
            File(FILE_PATH + FILENAME).removeMovie(randomMovie) #Remove selection from list
        continueOption = str(input('Would you like to continue with another selection? Y or N: ')).strip().upper()
        if continueOption == 'Y':
            menu()

    #Completely random selection of movie catalog
    elif operation == "C": 
        print()
        randomMovie = MovieSelecter(movieCatalog).fetchRandom()
        print('Looks like you are watching "'+ randomMovie+'" Tonight.')
        print()
        removeOption = str(input('Would you like to remove it from your list? Y or N: ')).strip().upper()
        if removeOption == 'Y':
            File(FILE_PATH + FILENAME).removeMovie(randomMovie) #Remove selection from list
        continueOption = str(input('Would you like to continue with another selection? Y or N: ')).strip().upper()
        if continueOption == 'Y':
            menu()
    
    #Quit Johansen Family Movie Night Assignment System
    elif operation == "Q": 
        print()
        print("Thank you for using the Johansen Family Movie Night Assignment System")

    #Catch input all other input, notify user that it is not usable
    else: 
        print()
        print("*****************************************************************")
        print('Sorry can not assist you with "'+operation+'", it is not an available option')
        print("*****************************************************************")
        menu()

    

main()