#Mathematics For Individual Achievement page 245.
#Old math book on Raymond Mar's Shelf
from random import randint
dollars = randint(1,100)
cents = randint(0,99)*.01
mealcost = dollars + cents
mealcostdisplay = format(mealcost,".2f") #print exactly two decimal places to display
print("Today's meal cost "+mealcostdisplay)
print(type(mealcostdisplay))
tip15 = mealcost * .15
tip10 = mealcost * .10
print("cheat 15% tip ",tip15)
print(round(tip15,2))
calculatetip15 = float(input("The meal is "+mealcostdisplay+" How much is the 15% tip? "))
if calculatetip15 == round(tip15,2):
	print("Correct")	
elif calculatetip15 == round(tip15,2)+.01 or calculatetip15 == round(tip15,2)-.01:
	print("Close enought.  Off +/- .01")
calculatetip10 = float(input("The meal is "+mealcostdisplay+" How much is the 10% tip? "))
if calculatetip10 == round(tip10,2):
	print("Correct")
calculatetip = float(input("Enter the meal cost I calculate the 15% and 10% tip "))
tip15 = calculatetip * .15
tip10 = calculatetip * .10
tip15display = format(tip15,".2f")
tip10display = format(tip10,".2f")
print("15% tip is "+tip15display)
print("10% tip is "+tip10display)