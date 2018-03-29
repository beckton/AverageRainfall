#Rainfall Statistics
#12m array display totRainfall for yr, avg/m, months w highest n lowest
totRain = 0.0
average = 0.0
aryYrOfRainfall = []
minRain = 0.0
maxRain = 0.0
high = 0.0
aryMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
highIndex = 0.0
lowIndex = 0.0
low = 0.0

for i in range(0,12):
    monthRain = input("What is the rainfall for month " + str(i + 1) + ": ")
    aryYrOfRainfall.append(monthRain)
    totRain += monthRain
    average = float(totRain / 12)
    minRain = min(aryYrOfRainfall) 
    maxRain = max(aryYrOfRainfall)
    if monthRain > high:
        high = monthRain
        highIndex = i
        low = minRain
    if monthRain <= low:
        low = monthRain
        lowIndex = i
        
    
print ("The total rainfall for the year was %i inches." % totRain)
print ("The average rainfall is %.2f inches per month" % average)
print ("The highest ammount of rainfall in %s was %i inches. " % (str(aryMonths[highIndex]), maxRain))
print ("The lowest ammount of rainfall in %s was %i inches. " % (str(aryMonths[lowIndex]), minRain))
