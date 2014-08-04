class Person:
	def __init__(self):
		self.name = None
		self.age = None
		self.weight = None
		self.height = None
		self.hours = [0, 0, 0, 0, 0, 0, 0]
		self.mileTime = None

import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('inputPath', default=os.getcwd())
parser.add_argument('-o', action="store", dest="outputPath", nargs='?')
arguments = parser.parse_args()

printflag = False
if arguments.outputPath == None:
	printflag = True
	
if printflag == False:
	file = open(arguments.outputPath,"w")

personList = []

DAYS_IN_WEEK = 7

with open(arguments.inputPath, 'r') as personFile:
	for line in personFile:
		if 'Name' in line:
			l = [a.strip() for a in line.rstrip('\n').split(',')]
			
			p = Person()
			
			i = l.index('Name')
			p.name = l[i+1]
			
			i = l.index('Age')
			p.age = l[i+1]
			
			i = l.index('Weight')
			p.weight = float(l[i+1])
			
			i = l.index('Height')
			p.height = float(l[i+1])
			
			try:
				i = l.index('HoursAtGym-Sunday')
				p.hours[0] = int(l[i+1])
				
				i = l.index('HoursAtGym-Monday')
				p.hours[1] = int(l[i+1])
				
				i = l.index('HoursAtGym-Tuesday')
				p.hours[2] = int(l[i+1])
				
				i = l.index('HoursAtGym-Wednesday')
				p.hours[3] = int(l[i+1])
				
				i = l.index('HoursAtGym-Thursday')
				p.hours[4] = int(l[i+1])
				
				i = l.index('HoursAtGym-Friday')
				p.hours[5] = int(l[i+1])
				
				i = l.index('HoursAtGym-Saturday')
				p.hours[6] = int(l[i+1])
			except:
				pass
			
			i = l.index('MileTimeInSeconds')
			p.mileTime = l[i+1]
		
			personList.append(p)

youngest = min(p.age for p in personList)
averageAge = sum(int(p.age) for p in personList)/len(personList)
oldest = max(p.age for p in personList)

weightList = [p.weight for p in personList]

lightest = min(weightList)
heaviest = max(weightList)
averageWeight = sum(weightList)/len(personList)

sumhours = [0 for i in range(DAYS_IN_WEEK)]
for p in personList:
	sumhours = [x+y for x,y in zip(sumhours,p.hours)]
	
busiestIdx = sumhours.index(max(sumhours))
slowestIdx = sumhours.index(min(sumhours))

weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

slow = min(p.mileTime for p in personList)
fast = max(p.mileTime for p in personList)
averageMile = sum(int(p.mileTime) for p in personList)/len(personList)

if printflag == True:
	print ("The youngest age is: ", youngest)
	print ("The average age is: ", int(averageAge))
	print ("The oldest age is: ", oldest)
	print ("The range of weights is from: ", lightest, " to ", heaviest)
	print ("The average weight is: {:.2f}".format(averageWeight))
	print (weekdays[busiestIdx], " is the busiest day of the week.")
	print (weekdays[slowestIdx], " is the slowest day of the week.")
	print ("The slowest mile time is: ", slow)
	print ("The fastest mile time is: ", fast)
	print ("The average mile time is: ", averageMile, "\n")
	
if printflag == False:
	file.write ("The youngest age is: {}\n".format(youngest))
	file.write ("The average age is: {}\n".format(int(averageAge)))
	file.write ("The oldest age is: {}\n".format(oldest))
	file.write ("The range of weights is from: {} to {}\n".format(lightest,heaviest))
	file.write ("The average weight is: {:.2f}\n".format(averageWeight))
	file.write ("{} is the busiest day of the week.\n".format(weekdays[busiestIdx]))
	file.write ("{} is the slowest day of the week.\n".format(weekdays[slowestIdx]))
	file.write ("The slowest mile time is: {}\n".format(slow))
	file.write ("The fastest mile time is: {}\n".format(fast))
	file.write ("The average mile time is: {}\n\n".format(averageMile))

for p in personList:
	busiest = p.hours.index(max(p.hours))
	slowest = p.hours.index(min(p.hours))

	if printflag == True:
		print ("Name:",p.name," Age:", p.age," Weight:",p.weight," Busiest Gym Day:",weekdays[busiest], " Slowest Gym Day:", weekdays[slowest])
	if printflag == False:
		file.write ("Name:{} Age:{} Weight:{} Busiest Gym Day:{} Slowest Gym Day:{}\n".format(p.name, p.age, p.weight,weekdays[busiest], weekdays[slowest]))
