#Mathematics For Individual Achievement page 307.
#Old math book on Raymond Mar's Shelf
from random import randint
x = randint(1,10)
y = randint(1,10)
xyplusminus = randint(-5,5)
z = (x+y)+(xyplusminus)
print("x",x,"y",y,"xyplusminus",xyplusminus,"z",z)
answer= ""
while answer != "x":
	answer = input("Is y=%d the answer to the equation %d+y=%d?  Enter y for yes and n for no " %(y,x,z))
	if answer == "y" and x+y==z:
		print("You're correct")
		break
	elif answer == "y" and x+y!=z:
		print("Incorrect.  Try again")		
	elif answer == "n" and x+y!=z:
		print("You're correct.  How about the next question below.")
		y = abs(y)
		y = z + randint(-y,y)
	elif answer == "n" and x+y==z:
		print("Incorrect.  y=%d is the correct answer to %d+%d=%d" %(y,x,y,z))
		break