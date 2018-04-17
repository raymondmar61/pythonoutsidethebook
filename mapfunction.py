"""
Video title sources:
Socratica New 027 Map, Filter, and Reduce Functions Python Tutorial Learn Python Programming.mp4-->Socratica map function is at socraticaallvideos.py.

The Map, Filter, and Reduce Functions in Python.mp4.  pretty prettier(?) or pretty printer(?) is YouTube Channel

Python 3 Tutorial for Beginners #22 - Maps.mp4.  The Net Ninja

Learn to Program 12 Lambda Map Filter Reduce.mp4.  Includes function annotations.  Derek Banas
"""
numbers = [1,2,3,4,5]
values = ["abc","def","ghi"]
def square(x):
	return x**2d
def negative(x):
	return x*(-1)
def uppercase(string):
	return string.upper()
print(list(map(square,numbers))) #print [1, 4, 9, 16, 25]
print(list(map(lambda x: x**2,numbers))) #print [1, 4, 9, 16, 25]
print(list(map(negative,numbers))) #print [-1, -2, -3, -4, -5]
print(list(map(uppercase,values))) #print ['ABC', 'DEF', 'GHI']
print(list(map(lambda string: string.upper(),values))) #print ['ABC', 'DEF', 'GHI']
numbers2 = [1,2,3,4,5,6]
def greaterthanthree(x):
	return x > 3
print(list(filter(greaterthanthree,numbers2))) #print [4, 5, 6]
print(list(filter(lambda x: x>3,numbers2))) #print [4, 5, 6]
from functools import reduce
print(reduce(lambda x,y: x+y,numbers2)) #print 21
print(reduce(lambda x,y: x*y,numbers2)) #print 720
strings = ["This","is","a","sentence"]
print(reduce(lambda x,y: x+y,strings)) #print Thisisasentence
print((" ".join(strings))) #print This is a sentence
newsentence = ""
for eachstrings in strings:
	newsentence = newsentence + " " + eachstrings
print(newsentence) #print _This is a sentence
print("\n")

#newlist = map(function,oldlist)
from random import shuffle
def jumble(word):
	anagram = list(word) #separates word to a list of letters
	shuffle(anagram)	
	return "".join(anagram)
words = ["beetroot","carrots","potatoes"]
anagrams = []
for word in words:
	anagrams.append(jumble(word))
print(anagrams) #print ['bttoeroe', 'rtsarco', 'atoseotp']
print(map(jumble,words)) #print <map object at 0x7f8cfff70400>
print(list(map(jumble,words))) #print ['obrettoe', 'trocsar', 'tpeoaots']
print([jumble(word) for word in words]) #print ['boerttoe', 'rtarosc', 'topsoaet']
print("\n")

def multiplyby2(num):
	return num * 2
def domath(func, num):
	return func(num)
def getfuncmultbynum(num):
	print("getfuncmultbynum",num) #print 5
	def multby(value):
		print("multby",value) #print 10
		return num * value
	return multby
print("4 * 2 =",multiplyby2(4)) #print 4 * 2 = 8
timestwo = multiplyby2
print("4 * 2 =",timestwo(4)) #print 4 * 2 = 8
print("8 * 2 =",domath(multiplyby2,8)) #print 8 * 2 = 16
generatedfunc = getfuncmultbynum(5)
print("5*10=",generatedfunc(10))
listoffuncs = [timestwo, generatedfunc]
print("5*9=",listoffuncs[1](9)) #print 5*9= 45
def isitodd(num):
	if num % 2 == 0:
		return False
	else:
		return True
def changelist(lists, func):
	oddlist = []
	for i in lists:
		if func(i):
			oddlist.append(i)
	return oddlist
alist = range(1,20)
print(changelist(alist,isitodd)); #print [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
def randomfunction(name: str, age: int, weight: float)->str:
	print("Name:",name)
	print("Age:",age)
	print("Weight:",weight)
	return "{} is {} years old and weights {}".format(name, age, weight)
print(randomfunction("Derek", 41, 165.5)) #print Derek is 41 years old and weights 165.5
print("\n")
#lambda arg1, arg2, . . . argn: expression use the args
sum = lambda x, y: x + y
print("Sum",sum(4, 5)) #print Sum 9
canvote = lambda age: True if age >= 18 else False
print("Can vote:", canvote(16)) #print Can vote: False
powerlist = [lambda x: x**2, lambda x: x**3, lambda x: x**4]
for func in powerlist:
	print(func(4)) #print 16\n 64\n 256
attack = {"quick": (lambda: print("Quick Attack")), "power": (lambda: print("Power Attack")), "miss": (lambda: print("Missed Attack"))}
attack['quick']()
import random
attackkey = random.choice(list(attack.keys()))
attack[attackkey]()
print("\n")
fliplist = []
for i in range(1,101):
	fliplist += random.choice(["H","T"])
print("Heads:",fliplist.count("H"))
print("Tails:",fliplist.count("T"))
print("\n")
onetoten = range(1,11)
def doublenumber(num):
	return num * 2
print(list(map(doublenumber,onetoten))) #print [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(list(map((lambda x: x * 3),onetoten))) #print [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
alist = list(map((lambda x, y: x + y),[1, 2, 3], [1, 2, 3]))
print(alist) #print [2, 4, 6]
print("\n")
print(list(filter((lambda x: x % 2 == 0), range(1, 11)))) #print [2, 4, 6, 8, 10]
randomlist = list(random.randint(1, 1001) for i in range (1,101))
print(list(filter((lambda x: x % 9 == 0), randomlist))) #print [423, 783, 252, 441, 918, 189, 747]
print("\n")
from functools import reduce
print(reduce((lambda x, y: x + y),range(1,6))) #print 15

numbers = list(range(0,11))
print(numbers) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def squaremaplist(num):
	return pow(num,2)
print(list(map(squaremaplist, numbers))) #print [0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0, 100.0].  No need for the for loop.
print(list(map(str, numbers))) #print ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'.  str is a function
print(list(map(int, numbers))) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].  int is a function