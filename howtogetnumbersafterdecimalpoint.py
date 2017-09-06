#how to get numbers after decimal point?
#https://stackoverflow.com/questions/3886402/python-how-to-get-numbers-after-decimal-point

number = 125.55
#number = 987654321 * 9.167
numberdecimal = str(number - int(number))[1:4]
print(numberdecimal) #print .54
numberdecimal = str(number-int(number)).split(".")[1:4]
print(numberdecimal) #print ['5499999999999972']
print(number % 1) #print 0.5499999999999972
print(number - int(number)) #print 0.5499999999999972

import math
fraction, whole = math.modf(number)
print(fraction) #print 0.5499999999999972
print(whole) #print 125.0
x = math.floor(number)
print("x",x) #print x 125
print(number - x) #print 0.5499999999999972

import numpy
print(number - numpy.fix(number)) #print 0.55

from decimal import Decimal
print(Decimal(number) % 1) #print 0.5499999999999971578290569596

if "." in str(number):
	print("."+str(number).split(".")[-1]) #print .55