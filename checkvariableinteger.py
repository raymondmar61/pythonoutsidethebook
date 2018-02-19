import numbers
x = 4
x2 = 4.1
love = isinstance(x, numbers.Integral)
print(love) #print True
love = isinstance(x2, numbers.Integral)
print(love) #print False
love = isinstance(3, int)
print(love,"no numbers.Integral") #print True
love = isinstance(x, int)
print(love,"no numbers.Integral") #print True
love = isinstance(x2, int)
print(love,"no numbers.Integral") #print False

fivex = 5
fiveonex = 5.1
fivezerox = 5.0
#print(fivex.is_integer()) #error message
#print(int(fivex).is_integer()) #error message
print(float(fivex).is_integer()) #print True
print(float(fiveonex).is_integer()) #print False
print(float(fivezerox).is_integer()) #print True

def isinteger(variable):
	if type(variable) == int:
		print("Is integer")
	else:
		print("Is not integer")
isinteger(fivex) #return Is integer
isinteger(fiveonex) #return Is not Integer
#Do not use type(). It is almost never the right answer in Python, since it blocks all the flexibility of polymorphism.
