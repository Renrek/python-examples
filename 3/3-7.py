#Declare Vars
firstSet = int(0)
secondSet = int(0)

#should validate that a number is put in, but beyond exercise
#cardNumber = list("58667936100244")
cardNumber = str(input("Enter a credit card number: "))

#Take digit from even postions within the number
for i in range(0, len(cardNumber), 2):
    #Double the number
    number = 2 * int(cardNumber[i])
    #If doubling results in two digit number reduce by 9
    if number > 9:
        number = number - 9
    #Keep a running total
    firstSet += number

#Take digit from odd postions within the number
for i in range(1, len(cardNumber), 2):
    #Keep a running total
    secondSet += int(cardNumber[i])

total = firstSet + secondSet

if (firstSet + secondSet) % 10 == 0:
    print("The number is valid")
else:
    print("Your card is rejected.")


