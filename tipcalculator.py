#Mathematics For Individual Achievement page 245.
#Old math book on Raymond Mar's Shelf
from random import randint
import decimal
dollars = randint(1,100)
cents = randint(0,99)*.01
mealcost = dollars + cents
mealcostdisplay = format(mealcost,".2f") #print exactly two decimal places
print(mealcostdisplay)
print(type(mealcostdisplay))
tip = mealcost * .15
print(tip)
print(round(tip,2))
calculatetip = float(input("The meal is "+mealcostdisplay+" How much is the 15% tip? "))
if calculatetip == round(tip,2):
	print("Correct")