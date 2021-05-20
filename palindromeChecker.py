#Take user input
word = str(input("Enter a word or phrase: "))
#A man, a plan, a canal: Panama.
#Prepare original to save for deliveray
deliveryWord = word.upper()

#Quick clean up of word
word = word.strip().lower().replace(' ', '')

#Remove any charicters that are not of the alphabet
cleanWord =""
for i in word:
    if i.isalpha():
        cleanWord += i
        
#Switch the word in reverse order
wordInReverse = cleanWord[::-1]

#Compare both strings to see if a palindrome
if wordInReverse == cleanWord:
    print(deliveryWord + " is a palindrome.")
else:
    print(deliveryWord + " is NOT a palindrome.")