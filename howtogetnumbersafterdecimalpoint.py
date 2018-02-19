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
x2 = 1234.5678
x2fraction, x2whole = math.modf(x2)
print(x2whole) #print 1234.0
print(x2fraction) #print 0.5678000000000338
print(type(x2whole)) #print <class 'float'>

x3 = 1234.5678
integer, decimal = divmod(x3,1)
print(integer) #print 1234.0
print(decimal) #print 0.5678000000000338
print(type(integer)) #print <class 'float'>
#EDIT: The decimal part of a float number is approximate.  Use it as a human you must use the decimal library.

number = 125.55
import numpy
print(number - numpy.fix(number)) #print 0.55

number = 125.55
from decimal import Decimal
print(Decimal(number) % 1) #print 0.5499999999999971578290569596

number = 125.55
if "." in str(number):
	print("."+str(number).split(".")[-1]) #print .55

number = 1.23456789
print(number)
print(str(number-int(number))) #1.23456789-1
print(str(number)[1:2]+"here is the decimal") #print .here is the decimal
number2 = str(number-int(number))[2:3]
print(number2,"number2") #print 2 number2
print(type(number2)) #print <class 'str'>
number3 = str(number-int(number))[3:4]
print(number3,"number3") #print 3 number3
print(type(number3)) #print <class 'str'>
number4 = str(number-int(number))[4:5]
print(number4,"number4") #print 4 number4
print(type(number4)) #print <class 'str'>
number5 = str(number-int(number))[5:6]
print(number5,"number5") #print 5 number5
print(type(number5)) #print <class 'str'>
number6 = str(number-int(number))[6:7]
print(number6,"number6") #print 6 number6
print(type(number6)) #print <class 'str'>
print(int(4.99)) #print 4

a = 147.234
print(a % 1) #print 0.23400000000000887
print(a//1) #print 147.0
print("\n")

x4 = 1234.5678
onetwothreefour = ( lambda x, y : ( int( x ), int( x * y ) % y / y ) )( x4, 1e0 )
print(onetwothreefour) #print (1234, 0.0)
print(onetwothreefour[0]) #print 1234
print(type(onetwothreefour[0])) #print <class 'int'>
print(onetwothreefour[1]) #print 0.0
onedecimalpoint = ( lambda x, y : ( int( x ), int( x * y ) % y / y ) )( x4, 1e1 )
print(onedecimalpoint[1]) #print  0.5
twodecimalpoint = ( lambda x, y : ( int( x ), int( x * y ) % y / y ) )( x4, 1e2 )
print(twodecimalpoint[1]) #print  0.56
alldecimalpoint = ( lambda x, y : ( int( x ), int( x * y ) % y / y ) )( x4, 1e5 )
print(alldecimalpoint) #print (1234, 0.5678)
print(alldecimalpoint[0]) #print 1234
print(alldecimalpoint[1]) #print 0.5678
