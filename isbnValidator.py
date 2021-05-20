def main():

    isbn = str(input("Enter and ISBN: "))
    #isbn = str("0-13-030657-6") #Test isbn = true
    #isbn = str("0-32-108599-X") #Test isbn = true
    #isbn = str("0-32-108299-X") #Test isbn = false

    if errorCheck(isbn):
        print("The number is vaild.")
    else:
        print("The number is invalid, please try again.")

def errorCheck(isbn):
    #Declare Var for running total
    checkSum = 0
    #Remove '-' from string
    isbn = isbn.replace('-','')
    #Reverse string for processing
    isbn = isbn[::-1]
    #Put word through reverse loop
    for i in range(10,0,-1):
        #if the last charicter is an "X" count it as a multiple of 10
        if i == 1 and isbn[0] == "X":
            checkSum = checkSum + (i * 10)
        #Multiply loop index countdown by the isbn charicter postion using index -1
        else:
            checkSum = checkSum + (i * int(isbn[i-1]))
    #Validate the sum by clean division of 11        
    if checkSum % 11 == 0:
        return bool(True)
    return bool(False)
        
main()
