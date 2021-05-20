#Declare Constants
DEPOSIT = 5000 # $
YEAR = 1
TIME_SPAN = 48 # years
IRA_INTREST = float(.04) #  4% annual
INVESTMENT_BENCHMARK = 15 # years

#formating
reportWidth = 40 #Columns
reportColumn = int(reportWidth / 2) #Columns

#Operational Variables
compoundInterest = IRA_INTREST + 1
timePassed = 0 #Starting Time
earlsBalance = 0 #Starting Balance
earlsTotalInvestment = 0 #Starting Balance
larrysTotalInvestment = 0 #Starting Balance
larrysBalance = 0 #Starting Balance

#Prepare Payload
while timePassed < TIME_SPAN:
    earlsBalance = compoundInterest * earlsBalance
    larrysBalance = compoundInterest * larrysBalance
    if timePassed < INVESTMENT_BENCHMARK:
        earlsBalance += DEPOSIT
        earlsTotalInvestment += DEPOSIT
    if timePassed >= INVESTMENT_BENCHMARK:
        larrysBalance += DEPOSIT
        larrysTotalInvestment += DEPOSIT
    timePassed += YEAR

#Output
print("\n")
print("AMOUNTS DEPOSITED".center(reportWidth))
earl = "Earl: ${0:,.2f}".format(earlsTotalInvestment)
larry = "Larry: ${0:,.2f}".format(larrysTotalInvestment)
print(earl.ljust(reportColumn), larry.rjust(reportColumn))
print("AMOUNTS IN IRA UPON RETIREMENT".center(reportWidth))
earl = "Earl: ${0:,.2f}".format(earlsBalance)
larry = "Larry: ${0:,.2f}".format(larrysBalance)
print(earl.ljust(reportColumn), larry.rjust(reportColumn))
