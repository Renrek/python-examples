def main():

    verbalizeNumber(123000004056777888999012345)
    #verbalizeNumber(123000004056777888999012345000)
    #verbalizeNumber(88999012345)
    #verbalizeNumber(1000)
    #verbalizeNumber(-1345000)
    #verbalizeNumber("I'm a number")
    #verbalizeNumber(int(input("Enter a Number: ")))

def verbalizeNumber(number):
    maxLength = 27 #Magic number for max place values of number
    valueLabel = ['','thousand','million', 'billion', 'trillion', 
            'quadrillion', 'quintillion', 'sextillion', 'septillion']
    payload = [] #For storing the printout

    #Verify that number is an integer
    if isinstance(number, int):

        #Verify that number is positive
        if number > 0:

            #Verify that number is less than 27 characters long.
            numberAsString = str(number)
            charlen = len(numberAsString)
            if charlen <= maxLength: 
                valueLabelCounter = 0 #For valueLabel iteration
                #Cycle through place values of 3, reads number from right to left
                for i in range(0,charlen,3):
                    placeCount = charlen - (i+3)

                    #Handles numbers that length can not divided by 3 perfectly
                    if placeCount < 0 :
                        placeCount = 0

                    #Wash string of leading zeroes by converting it back to int briefly
                    washedOfZeroesNumber = int(numberAsString[placeCount:charlen-i])

                    #Storing output for later use
                    payload.append(str(washedOfZeroesNumber).rjust(3)+" "
                        +valueLabel[valueLabelCounter])
                    valueLabelCounter += 1 

                print("\n") # Give the printout some space
                
                #Reverse through stored payload
                for i in range(len(payload),0, -1):
                    print(payload[i-1])

            else:
                print("\nNumber is too long, please select a number that is smaller.")

        else:
            print("\nNot a positive number, please try again.")

    else:
        print("\nNot a number, please try again.")

main()
