class Person:
	def __init__(self):
		self.name = None
		self.age = None
		self.weight = None
		self.height = None
		self.hours = [None, None, None, None, None, None, None]
		self.mileTime = None

personList = []
pathname = 'C:\\Users\\Brian\\Desktop\\test.txt'

DAYS_IN_WEEK = 7

with open(pathname, 'r') as personFile:
	for line in personFile:
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

print ("The youngest age is: ", youngest)
print ("The average age is: ", int(averageAge))
print ("The oldest age is: ", oldest)
print ("The range of weights is from: ", lightest, " to ", heaviest)
print ("The average weight is: {:.2f}".format(averageWeight))

sumhours = [0 for i in range(DAYS_IN_WEEK)]
for p in personList:
	sumhours = [x+y for x,y in zip(sumhours,p.hours)]
	
busiestIdx = sumhours.index(max(sumhours))
slowestIdx = sumhours.index(min(sumhours))

weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

print (weekdays[busiestIdx], " is the busiest day of the week.")
print (weekdays[slowestIdx], " is the slowest day of the week.")

slow = min(p.mileTime for p in personList)
fast = max(p.mileTime for p in personList)
averageMile = sum(int(p.mileTime) for p in personList)/len(personList)

print ("The slowest mile time is: ", slow)
print ("The fastest mile time is: ", fast)
print ("The average mile time is: ", averageMile, "\n")

for p in personList:
	busiest = p.hours.index(max(p.hours))
	slowest = p.hours.index(min(p.hours))

	print ("Name:",p.name," Age:", p.age," Weight:",p.weight," Busiest Gym Day:",weekdays[busiest], " Slowest Gym Day:", weekdays[slowest])
