#Declare Vars
CAFFEINE_PER_CUP = 130 # .mg
ELIMINATION_RATE = float(.13)
RATE = 1 # hour
TIME_SPAN = 24 # hours
CAFFEINE_HALF_LIFE = 65 # .mg

#Calculate output payload

#Caffeine elimination process
caffeineEliminationBalance = CAFFEINE_PER_CUP
caffeineClock = 0 #Stopwatch start point
halfLifeTimeIsSet = bool(False) # I am used to PHP isset(variable)
while caffeineClock < TIME_SPAN:
    #Check if the caffeine has reached it's half life and skip if half life is set
    if caffeineEliminationBalance < CAFFEINE_HALF_LIFE and not halfLifeTimeIsSet:
        halfLifeTime = caffeineClock
        halfLifeTimeIsSet = bool(True) 

    #Cycle through the caffeine elimination process
    caffeineReduction = caffeineEliminationBalance * ELIMINATION_RATE
    caffeineEliminationBalance -= caffeineReduction
    caffeineClock += RATE

#Caffeine marathon abosorption process
caffeineClock = 0 #Stopwatch reset
caffeineAbsorptionBalance = CAFFEINE_PER_CUP
while caffeineClock < TIME_SPAN:
    caffeineReduction = caffeineAbsorptionBalance * ELIMINATION_RATE
    caffeineAbsorptionBalance -= caffeineReduction
    caffeineAbsorptionBalance += CAFFEINE_PER_CUP
    caffeineClock += RATE
    
#Output
print("\nCAFFEINE VALUES")
print("One cup: less than " + str(CAFFEINE_HALF_LIFE) +" mg. will remain after "
     + str(halfLifeTime) +" hours")
print("One cup: {0:,.2f}".format(caffeineEliminationBalance) +" mg. will remain after "
     + str(TIME_SPAN) +" hours")
print("Hourly cups: {0:,.2f}".format(caffeineAbsorptionBalance) +" mg. will remain after "
     + str(TIME_SPAN) +" hours")

