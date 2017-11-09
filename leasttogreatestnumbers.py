#Mathematics For Individual Achievement page 183.
#Old math book on Raymond Mar's Shelf
from random import randint
numberslist = []
while len(numberslist) < randint(5,10):
	addnumber = randint(1,99)
	if addnumber not in numberslist:		
		numberslist.append(addnumber)	
numberslist.sort()
print(numberslist)
userlist = input("Enter the numbers above least to greatest separated by comma no space: ")
userlist = userlist.split(",")
print(userlist)
userlist = list(map(int,userlist))
print(userlist)
if (userlist == numberslist):
	print("Winner")

from random import randint
numberslist = []
while len(numberslist) < randint(5,10):
	addnumber = randint(1,99)/100
	if addnumber not in numberslist:		
		numberslist.append(addnumber)	
numberslist.sort()
print(numberslist)
userlist = input("Enter the numbers above least to greatest separated by comma no space: ")
userlist = userlist.split(",")
print(userlist)
userlist = list(map(float,userlist))
print(userlist)
if (userlist == numberslist):
	print("Winner")