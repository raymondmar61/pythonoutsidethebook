#Ask Marilyn Parade Sun Nov 11, 2018
#The last two digits of my birth year are the same as my age today.  Can you state with 100 percent centainty how old I am?

from datetime import datetime

currentyear = datetime.now().year
print(currentyear)
twodigitcurrentyear = str(currentyear)[2:4]
for n in range(10,100):
	if currentyear - (n+1900) == n:
		print(n,"is the age")
#Marilyn's Double.  If you're born in 1980, then 80 + 1980 = 2060.  If you're borin in 1959, then 59 + 1959 = 2018.
for n in range(1900,currentyear+1):
	twodigityear = str(n)[2:4]
	twodigityear = int(twodigityear)
	guessyear = n + twodigityear
	if guessyear == currentyear and len(str(twodigityear)) == 2:
		print(n,"is the age")