#Mathematics For Individual Achievement page 369.
#Old math book on Raymond Mar's Shelf
from random import randint
from statistics import mean, median, mode, StatisticsError
def meanmedianmode(numberslist):
	"""Function calculates mean, median, mode from a random list of numbers between 1 and 100 inclusive."""
	meananswer = round(mean(numberslist),1)
	mediananswer = int(median(numberslist))
	meanuseranswer = float(input("What's the mean round up to one decimal place? "))
	if meananswer == meanuseranswer:
		print(meananswer,"is correct")
	else:
		print(meanuseranswer,"is incorrect.  The correct mean is",meananswer)
	medianuseranswer = int(input("What's the median? "))
	if mediananswer == medianuseranswer:
		print(mediananswer,"is correct")
	else:
		print(medianuseranswer,"is incorrect.  The median is",mediananswer)
	try:
		round(mode(numberslist),1)
		modeanswer = round(mode(numberslist),1)
	except StatisticsError:
		print("There is no mode")
	else:
		print("mode cheat",modeanswer)
		modeuseranswer = int(input("What's the mode? "))
		if modeanswer == modeuseranswer:
			print(modeanswer,"is correct")
		else:
			print(modeuseranswer,"is incorrect.  The mode is",modeanswer)

print(meanmedianmode.__doc__)
numbers = int(input("How many numbers do you want? "))
numberslist = []
counter = 0
#generate numbers random numbers 1-100 in numberslist
while counter < numbers:
	numberslist.append(randint(1,100))
	counter +=1
print(numberslist)
print("mean cheat",round(mean(numberslist),1))
print("median cheat",int(median(numberslist)))
meanmedianmode(numberslist)