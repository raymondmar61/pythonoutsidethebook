#RM:  A crash course review on functions first
#RM 050619:  finish the Python tutorial https://www.python-course.eu/python3_functions.php
#https://www.python-course.eu/python3_functions.php
def fahrenheit(temperatureincelsius):
	return (temperatureincelsius* 9 / 5) + 32
for t in (22.6, 25.8, 27.3, 29.8):
	print(t,":",fahrenheit(t)) #print 22.6 : 72.68\n 25.8 : 78.44\n 27.3 : 81.14\n 29.8 : 85.64
def hello(noname="everybody"):
	print("Hello "+noname+"!")
hello("Peter") #print Hello Peter!
hello() #print Hello everybody!
def hellowithdocstring(noname="everybody"):
	"""The first statement is usually a string called Docstring"""
	print("Hello "+noname+"!")
hellowithdocstring("Paul") #print Hello Peter!
hellowithdocstring() #print Hello everybody!
print("Docstring "+hellowithdocstring.__doc__) #print Docstring The first statement is usually a string called Docstring
def keywordparameters(a, b, c=0, d=0):
	return (a - b + c - d)
print(keywordparameters(12, 4)) #print 8
print(keywordparameters(42, 15, d=10)) #print 17
#print(keywordparameters(c=5, 0, 0, d=10))  #error message positional argument follows keyword argument
print(keywordparameters(c=5, a=0, b=0, d=10)) #print 5
def returnnone(x, y):
	c = x + y
print(returnnone(4,5)) #print None
def returnnone2(x, y):
	c = x + y
	return
print(returnnone2(4,5)) #print None
def returnsomething(x, y):
	return x + y	
print(returnsomething(4,5)) #print 9
def globalvariable():
	print(s)
s = "Python"
globalvariable() #print Python
def globallocalvariable():
	s = "Perl"
	print(s)
s = "Python"
globallocalvariable() #print Perl
print(s) #print Python
# def globallocalvariable2():
# 	print(s2)
# 	s2 = "Perl2"
# 	print(s)
# s2 = "Python2"
# globallocalvariable2() #print UnboundLocalError: local variable 's2' referenced before assignment
# print(s2)
def globallocalvariable3():
	global s3
	print(s3)
	s3 = "Perl3"
	print(s3)
s3 = "Python3"
globallocalvariable3() #print Python3\n Perl 3
print(s3) Perl3

#https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/
#There are different ways to return multiple values from a function.  They're using an object using a class, using a tuple, using a list, and using a dictionary.
def tuplefunction():
	astring = "tuplegeeksforgeeks"
	aninteger = 55
	return astring, aninteger
print(tuplefunction) #print <function tuplefunction at 0x7f4a06d7bea0>
print(tuplefunction()) #print ('tuplegeeksforgeeks', 55)
astring, aninteger = tuplefunction()
print(astring) #print tuplegeeksforgeeks
print(aninteger) #print 55
abbott, iris = tuplefunction()
print(abbott) #print tuplegeeksforgeeks
print(iris) #print 55
def listfunction():
	astring = "listgeeksforgeeks"
	aninteger = 66
	return [astring, aninteger]
print(listfunction()) #print ['listgeeksforgeeks', 66]
wantoneoflistfunction = listfunction()
print(wantoneoflistfunction[1]) #print 66
def dictionaryfunction():
	mydictionary = dict()
	mydictionary["astring"] = "dictionarygeeksforgeeks"
	mydictionary["aninteger"] = 77
	return mydictionary
print(dictionaryfunction()) #print {'astring': 'dictionarygeeksforgeeks', 'aninteger': 77}
wantoneofdictionaryfunction = dictionaryfunction()
print(wantoneofdictionaryfunction["aninteger"]) #print 77

#https://stackoverflow.com/questions/9752958/how-can-i-return-two-values-from-a-function-in-python
def selectchoice():
	choice1 = "yes"
	choice2 = "maybe"
	choice3 = "no"
	return (choice1, choice2, choice3)
print(selectchoice()) #print ('yes', 'maybe', 'no')
unpackselectchoice = selectchoice()
print(unpackselectchoice[2]) #print no

#https://pythonbasics.org/multiple-return/
def returnsinglevariable(a, b):
	sumnumbers = a + b
	return sumnumbers
print(returnsinglevariable(3,9)) #print 12
def returnmultiplevariables():
	name = "Agnes"
	age = 35
	country = "USA"
	return name, age, country
print(returnmultiplevariables()) #print ('Agnes', 35, 'USA')
name, age, country = returnmultiplevariables()
print(name) #print Agnes
print(age) #print 35
print(country) #print USA

#https://dotnetcodr.com/2015/08/01/python-language-basics-34-returning-multiple-values-from-a-function/
def calculate(firstnumber, secondnumber):
	add = firstnumber + secondnumber
	subtract = firstnumber - secondnumber
	multiply = firstnumber * secondnumber
	divide = firstnumber / secondnumber
	return add, subtract, multiply, divide
print(calculate(8,4)) #print (12, 4, 32, 2.0)
allmath = calculate(8,4)
print(allmath) #print (12, 4, 32, 2.0)
print(allmath[1]) #print 4

#https://www.quora.com/When-returning-multiple-values-from-a-function-why-does-Python-use-a-tuple-instead-of-a-list
def onevariablemultiplevalues():
	onevariabletuple = 1, 2, 3
	return onevariabletuple
print(onevariablemultiplevalues()) #print (1, 2, 3)
def onevariablemultiplevalueslist():
	onevariablelist = [1, 2, 3]
	return onevariablelist
print(onevariablemultiplevalueslist()) #print [1, 2, 3]
print(onevariablemultiplevalueslist()[2]) #print 3
#unboxing
numbertwo = onevariablemultiplevalueslist()[1]
print(numbertwo) #print 2

