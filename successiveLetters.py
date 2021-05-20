def main():

    word = str(input("Enter a word: "))
    if isTripleConsecutive(word):
        print(word + " contains three successive letters \n"+
            "in consecutive alphabetical order.")
    else:
        print(word + " does NOT contains three successive letters \n"+
            "in consecutive alphabetical order.")

def isTripleConsecutive(word:str) -> bool:
    #Make word uniform
    word.lower()
    #Only allow words with 3 characters or more
    if len(word) < 3:
        return bool(False)
    
    consecutiveLettersNeeded = 3
    consecutiveLetterCount = 1
    #Prime loop with the first letter
    lastLetter = ord(word[0])
    #Send remainder of word through loop
    remanderOfWord = word[1:len(word)]
    for i in remanderOfWord:
        newLetter = ord(i)
        if lastLetter < newLetter:
            #Add to tally
            consecutiveLetterCount += 1
        else:
            #Reset tally
            consecutiveLetterCount = 1
        #Check for three consecutive letter
        if consecutiveLetterCount == consecutiveLettersNeeded:
            return bool(True)
        #Set letter to compare to next iteration
        lastLetter = newLetter
    #If we land here, word is a dud
    return bool(False)
    
main()
