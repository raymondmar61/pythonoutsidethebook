#Mathematics For Individual Achievement page 121.
#Old math book on Raymond Mar's Shelf
from random import randint
while True:
	numerator = randint(1,100)
	denominator = randint(1,numerator)
	if numerator%denominator == 0:
		answer = "y"
	else:
		answer = "n"
	inputanswer = input("Is "+str(numerator)+" divisible by "+str(denominator)+"?  Type \"y\" for yes and \"n\" for no.  Type \"q\" to quit: ")
	if (answer == "y" and inputanswer == "y") or (answer == "n" and inputanswer == "n"):
		print("Correct. "+str(numerator)+" is divisible by "+str(denominator)+" equals "+str(numerator//denominator))
	elif (answer == "y" and inputanswer == "n"):
		print("Incorrect. "+str(numerator)+" is divisible by "+str(denominator)+" equals "+str(numerator//denominator))
	elif (answer == "n" and inputanswer == "y"):
		print("Incorrect. "+str(numerator)+" is not divisible by "+str(denominator))
	elif inputanswer == "q":
		break
	else:
		print("Error")

