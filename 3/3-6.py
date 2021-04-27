#Declare vars
letterRemoval = ('a','e','i','o','u','h','y','w')
oneReplace = ('b','f','p','v')
twoReplace = ('c','g','j','k','q','s','x','z')
threeReplace = ('d','t')
fiveReplace = ('m','n')

#Get user input and do initial formatting
word = str(input("Enter a word to code: "))
word = word.lower()
word = word.capitalize()

#Save first letter for later, send rest of word for processing
firstLetter = word[0]
word = word[1:len(word) + 1]

#Replace letters ('b','f','p','v') with 1
for i in oneReplace:
    word = word.replace(i, '1')

#Replace letters ('c','g','j','k','q','s','x','z') with 2
for i in twoReplace:
     word = word.replace(i, '2')

#Replace letters ('d','t') with 3
for i in threeReplace:
     word = word.replace(i, '3')

#Replace letter ('l') with 4
word = word.replace('l', '4')

#Replace letters ('m','n') with 5
for i in fiveReplace:
     word = word.replace(i, '5')

#Replace letters ('r') with 6
word = word.replace('r','6')

#Remove numbers that are not unique sequentially
wordCypher = ""
lastCharacter = ""
for character in word:
     if character != lastCharacter:
          wordCypher = wordCypher + character
     lastCharacter = character

#Remove letters ('a','e','i','o','u','h','y','w')
for i in letterRemoval:
     wordCypher = wordCypher.replace(i,'')

#Assemble Product
wordCypher = firstLetter + wordCypher

#Make sure that Product is 4 characters in length, add "0" to fill
cypherLen = len(wordCypher)
if cypherLen > 4 :
     wordCypher = wordCypher[0:4]
elif cypherLen < 4 :
     suffix = ""
     zeros = 4 - cypherLen
     wordCypher = wordCypher + suffix.zfill(zeros)

#Output
print("The coded word is " + wordCypher)