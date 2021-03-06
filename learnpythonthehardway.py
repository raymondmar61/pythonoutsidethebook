#Learn Python The Hard Way, 3rd Edition .pdf
#http://learnpythonthehardway.org/book/
#Do Not Copy-Paste
#You must type each of these exercises in, manually. If you copy and paste, you might as well just not even do them.  The point of these exercises is to train your hands, your brain, and your mind in how to read, write, and see code. If you copy-paste, you are cheating yourself out of the effectiveness of the lessons.

print("Exercise 1:  A Good First Program") #print Exercise 1:  A Good First Program
print("Hello World!") #print Hello World!
print("Exercise 2: Comments And Pound Characters") #print Exercise 2: Comments And Pound Characters
print("Why do I have to read code backwards?  It's a trick to make your brain not attach meaning to each part of the code, and doing that makes you process each piece exactly.  This catches errors and is a handy error checking technique.") #print Why do I have to read code backwards?  It's a trick to make your brain not attach meaning to each part of the code, and doing that makes you process each piece exactly.  This catches errors and is a handy error checking technique.
print("Exercise 3:  Numbers And Math Using Comma Separate string and numbers",100+200) #print Exercise 3:  Numbers And Math Using Comma Separate string and numbers 300
print(3+2) #print 5
print(3.0+2.0) #print 5.0
print(5-7) #print -1
print(7/4) #print 1.75
print("Drops the fractional part after the decimal",7//4) #print Drops the fractional part after the decimal 1
print(7.0/4.0) #print 1.75
print(75/4) #print 18.75
print((3+2)<(5-7)) #print False
print(10%2) #print 0
print("Exercise 4: Variables And Names")
cars = 100
spaceinacar = 4.0
drivers = 30
passengers = 90
carsnotdriven = cars - drivers
carsdriven = drivers
carpoolcapacity = carsdriven * spaceinacar
averagepassengersinacar = passengers / carsdriven
print("There are",cars,"cars available.") #print There are 100 cars available.
print("There are only",drivers,"drivers available.") #print There are only 30 drivers available.
print("There will be %d empty cars today." %carsnotdriven) #print There will be 70 empty cars today.
print("We can transport %.4f people today." %carpoolcapacity) #print We can transport 120.0000 people today.
print("We have {} to carpool today." .format(passengers)) #print We have 90 to carpool today.
print("We need to put about {} in each car." .format(averagepassengersinacar,".5f")) #print We need to put about 3.0 in each car.
print("Exercise 5: More Variables And Printing")
myname = "Zed A. Shaw"
myage = 35
myheight = 74
myweight = 180
myeyes = "blue"
myteeth = "white"
myhair = "brown"
print("Let's talk about %s" %myname) #print Let's talk about Zed A. Shaw
print("He's %d inches tall." %myheight) #print He's 74 inches tall.
print("He's {} pounds heavy." .format(myweight,"d")) #print He's 180 pounds heavy.
print("He's got %s eyes and %s hair." %(myeyes, myhair)) #print He's got blue eyes and brown hair.
print("His teeth are usually {} depending on the coffee." .format(myteeth)) #print His teeth are usually white depending on the coffee.
print("If I add {}, {}, and {}, I get {}." .format(myage, myheight, myweight, myage+myheight+myweight)) #print If I add 35, 74, and 180, I get 289.
print("Exercise 6: Strings And Text")
x = "There are %d types of people." %10
binary = "binary"
donot = "don't"
y = "Those who know %s and those who %s." %(binary, donot)
print(x) #print There are 10 types of people.
print(y) #print Those who know binary and those who don't.
print("I said: %r." %x) #print I said: 'There are 10 types of people.'.  #RM:  %r is for debugging which displays the raw data of the variable
print("I also said: '%s'." %y) #print I also said: 'Those who know binary and those who don't.'.
print("I also said: %s." %y) #print I also said: Those who know binary and those who don't..
hilarious = False
jokeevaluation = "Isn't that joke so funny?! %r"
print(jokeevaluation % hilarious) #print Isn't that joke so funny?! False
w = "This is the left side of . . . "
e = "a string with a right side."
print(w+e) #print This is the left side of . . . a string with a right side.
print("Exercise 7:  More Printing")
print("Mary had a little lamb.") #print Mary had a little lamb.
print("Its fleece was white as %s." %"snow") #print Its fleece was white as snow.
print("And everywhere that Mary went") #print And everywhere that Mary went
print("."*10) #print ..........
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print(end1+end2+end3+end4+end5+end6,end7+end8+end9+end10+end11+end12) #print Cheese Burger
print(end1+end2+end3+end4+end5+end6+end7+end8+end9+end10+end11+end12) #print CheeseBurger
number1 = 500
number2 = 743
print(number1,number2) #print 500 743
print(number1+number2) #print 1243
print("Exercise 8: Printing, Printing")
formatter = "%r %r %r %r"
print(formatter) #print %r %r %r %r
print(formatter %(1, 2, 3, 4)) #print 1 2 3 4
print(formatter %("one", "two", "three", "four")) #print 'one' 'two' 'three' 'four'
print(formatter %(True, False, False, True)) #print True False False True
print(formatter %(formatter, formatter, formatter, formatter)) #print '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
print(formatter %("I had this thing.","That you could type up right.", "But it didn't sing.", "So I said goodnight.")) #print 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
print("Exercise 9: Printing, Printing, Printing")
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFebMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the days: ",days) #orint Here are the days:  Mon Tue Wed Thu Fri Sat Sun
print("Here are the months:",months) 
'''
Here are the months: Jan
FebMar
Apr
May
Jun
Jul
Aug
''' 
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
'''
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
'''
print("""
	There's something going on here.
	With the three double-quotes.
	We'll be able to type as much as we like.
	Even 4 lines if we want, or 5, or 6.
	""")
'''
	There's something going on here.
	With the three double-quotes.
	We'll be able to type as much as we like.
	Even 4 lines if we want, or 5, or 6.
'''
print("Exercise 10:  What Was That?")
tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat) #print 	I'm tabbed in.
print(persian_cat) #print I'm split\n on a line.
print(backslash_cat) #print I'm \ a \ cat.
print(fat_cat)
"""
I'll do a list:
	* Cat food
	* Fishies
	* Catnip
	* Grass
"""
# while True:
# 	for i in ["/","-","|",",","\\","|"]:
# 		print("%s\r"%i,)
see = "Do you see?"
print("%s" %see) #print Do you see?
print("%r" %see) #print 'Do you see?'.  %r prints out the raw representation including the original escape sequences.
print("Exercise 11:  Asking Questions")
print("How old are you?"),  #RM:  tutorial says a comma at the end of the print line doesn't start a new line.  It doesn't work.
#age = input()
age = 45
print("How tall are you?",)
#height = input()
height = 45
print("How much do you weight?",)
#weight = input()
weight = 45
print("So, you're %r old, %r tall and %r heavy." %(age, height, weight)) #print So, you're 45 old, 45 tall and 45 heavy.
print("Give me a number")
#inputnumber = int(input())
inputnumber = 45
print("The number is %r" %inputnumber) #print The number is 45
#instructor says input() has security problems.  Use raw_input().  raw_input() doesn't work for python3.6.
print("Exercise 12:  Prompting People")
#y = input("Name? ") #display Name? .  Saves result into variable y.
y = "Raymond"
#age = input("How old are you? ")
age = (45)
#height = input("How tall are you? ")
height = (68)
#weight = input("How much do you weigh? ")
weight = (45)
print("So, you're %r old, %r tall and %r heavy." %(age, height, weight)) #print So, you're 45 old, 68 tall and 45 heavy.
print("Exercise 13:  Parameters, Unpacking, Variables")
# from sys import argv
# script, first, second, third = argv
# #run python in Linux type the following:  python3.6 first, 2nd, 3rd
# print("The script is called:", script) #print The script is called: learnpythonthehardway.py
# print("Your first variable is:", first) #print Your first variable is: first
# print("Your second variable is:", second) #print Your second variable is: 2nd
# print("Your third variable is:", third) #print Your third variable is: 3rd
print("Exercise 14:  Prompting And Passing")
# username = input("What is your name? ")
# script = input("Share a favorite movie. ")
# like = input("Do you like yourself, %s? " %username)
# location = input("Where do you live, "+username+" ")
# computer = input("What kind of computer do you have?  Desktop or laptop? ")
# print("""
# 	Alright, so you said %s about liking me.
# 	You live in %s.  Not sure where that is.
# 	And you have a %s computer.  Nice.
# 	""" %(like.lower(), location, computer.lower()))
print("Exercise 15:  Reading Files")
#The keyword with closes the file once access to it is no longer needed. Notice how we call open() in this program but not close().
filename = "exercise15sample.txt"
with open(filename) as fileobject:
	contents = fileobject.read()
	print(contents) #print This is stuff I typed into a file.\n It is really cool stuff.\n Lots and lots of fun to have in here.
with open(filename) as fileobject:
	contents = fileobject.read()
	print(contents.rstrip()) #rstrip() method removes or strips any whitespace characters from the right side of a string.
with open(filename) as fileobject:
	lines = fileobject.readlines() #readlines() method takes each line from the file and stores it in a list.
print(lines) #print ['This is stuff I typed into a file.\n', 'It is really cool stuff.\n', 'Lots and lots of fun to have in here.']
nospacesbetweenlines = ""
for line in lines:
	print(line.rstrip())
	nospacesbetweenlines += line.rstrip()
print(nospacesbetweenlines) #print This is stuff I typed into a file.It is really cool stuff.Lots and lots of fun to have in here.
print("Exercise 16:  Reading And Writing Files")
#"r" read mode, "w" write mode, "a" append mode, "r+" read and write mode, default is read mode
filename = "exercise16sample.txt"
#write = input("Enter text for %s " %filename)
write = "howard jones"
with open(filename, "w") as fileobject:
	fileobject.write(write)
	fileobject.write("""
this is a test
okay a test
three lines
		""")
	print(fileobject) #print <_io.TextIOWrapper name='exercise16sample.txt' mode='w' encoding='UTF-8'>
with open(filename, "r") as fileobject:	
	contents = fileobject.read()
	print(contents)
	'''
	howard jones
	this is a test
	okay a test
	three lines
	'''
print("Exercise 17:  More Files")
#create text file exercise17sample.txt.  Write the contents from Exercise 16 to text file text file exercise17sample.txt.
#The open() function automatically creates the file you’re writing to if it doesn’t already exist. However, be careful opening a file in write mode ('w') because if the file does exist, Python will erase the file before returning the file object.
filename = "exercise17sample.txt"
with open(filename, "w") as fileobject:
	for chapter16contents in contents:
		fileobject.write(chapter16contents)
with open(filename, "r") as fileobject:
	contents = fileobject.read()
	print(contents)
	'''
	howard jones
	this is a test
	okay a test
	three lines
	'''
print("Exercise 18:  Names, Variables, Code, Functions")
def printtwo(*args):
	arg1, arg2 = args
	print("arg1: %r, arg2: %r" %(arg1, arg2))
printtwo("Zed",5) #print arg1: 'Zed', arg2: 5
def printtwoagain(arg1, arg2):
	print("arg1: %r, arg2: %r" %(arg1, arg2))
printtwo("Zed2",52) #print arg1: 'Zed2', arg2: 52
def printone(arg1):
	print("arg1: %r" %arg1)
printone("Zed3") #print arg1: 'Zed3'
def printnone():
	print("I got nothin'.")
printnone() #print I got nothin'.
print("Exercise 19:  Functions And Variables")
def cheeseandcrackers(cheesecount, boxesofcrackers):
	print("You have %d cheeses!" %cheesecount)
	print("You have",boxesofcrackers,"boxes of crackers")
cheeseandcrackers(20, 30) #return You have 20 cheeses!\n You have 30 boxes of crackers
amountofcheese = 10
amountofcrackers = 50
cheeseandcrackers(amountofcheese, amountofcrackers) #return You have 10 cheeses!\n You have 50 boxes of crackers
cheeseandcrackers(10+20, 5+6) #return You have 30 cheeses!\n  You have 11 boxes of crackers
cheeseandcrackers(amountofcheese + 100, amountofcrackers + 200) #return You have 110 cheeses!\n You have 250 boxes of crackers
print("Exercise 19:  Functions And Variables")
def cheeseandcrackers(cheesecount, boxesofcrackers):
	print("You have %d cheeses!" %cheesecount)
	print("You have",boxesofcrackers,"boxes of crackers!")
cheeseandcrackers(20,30) #return You have 20 cheeses!\n You have 30 boxes of crackers!
amountofcheese = 10
amountofcrackers = 50
cheeseandcrackers(amountofcheese, amountofcrackers) #return You have 10 cheeses!\n You have 50 boxes of crackers!
cheeseandcrackers(10+20, 5+6) #return You have 30 cheeses!\n You have 11 boxes of crackers!
cheeseandcrackers(amountofcheese+100, amountofcrackers + 1000) #return You have 110 cheeses!\n You have 1050 boxes of crackers!
print("Exercise 20:  Functions And Files")
#"r" read mode, "w" write mode, "a" append mode, "r+" read and write mode, default is read mode
filename = "exercise20sample.txt"
#erase all text in exercise20sample.txt for a blank file
with open(filename, "w") as fileobject:
	fileobject.write("")
def functionwrite(n):
	name = "howard jones"
	with open(filename, "a") as fileobject:
		fileobject.write("%s %d\n" %(name, n))
for eachn in range(0,4):
	functionwrite(eachn)
with open(filename, "r") as fileobject:	
	contents = fileobject.read()
	print(contents)
print("Exercise 21:  Functions Can Return Something")
def add(a, b):
	print("Adding %d + %d" %(a,b))
	return a+b
def subtract(a, b):
	print("Subtracting",a,"-",b)
	return a-b
def multiply(a, b):
	print("Multiplying {} * {}" .format(a,b))
	return a*b
def divide(a, b):
	print("Dividing {} and {}" .format(a,b,".2f"))
	return a/b
age = add(30,5) #return Adding 30 + 5
height = subtract(78,4) #return Subtracting 78 - 4
weight = multiply(90,2) #return Multiplying 90 * 2
iq = divide(100,2) #return Dividing 100 and 2
print("Age: %d, Height: %d, Weight %d, IQ: %d" %(age, height, weight, iq)) #print Age: 35, Height: 74, Weight 180, IQ: 50
print("Exercise 22:  What Do You Know So Far?")
print("Exercise 23:  Read Some Code")
print("Exercise 24:  More Practice.  RM:  It's a review.")
print("Let's practice everything.") #print Let's practice everything.
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")
'''
You'd need to know 'bout escapes with \ that do 
 newlines and 	 tabs.
'''
poem = """
\t *paragraph indent \\t tab* The lovely world
with logic so firmly planted
cannot discern\nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print("----------")
print(poem)
print("-"*10)
'''
----------

	 *paragraph indent \t tab* The lovely world
with logic so firmly planted
cannot discern
the needs of love
nor comprehend passion from intuition
and requires an explanation

		where there is none.

----------
'''
five = 10 - 2 + 3 - 6
print("This should be five %s" %five) #print This should be five 5
print("This should be five",five) #print This should be five 5
print("This should be five {}" .format(five)) #print This should be five 5
def secretformula(started):
	jellybeans = started * 500
	jars = jellybeans // 1000
	crates = jars // 100
	return jellybeans, jars, crates
startpoint = 10000
beans, jars, crates = secretformula(startpoint)
print("With a starting point of: %d" %startpoint) #print With a starting point of: 10000
print("We'd have {} beans, {} jars, and {} crates." .format(beans, jars, crates)) #print We'd have 5000000 beans, 5000 jars, and 50 crates.
startpoint = startpoint /10
print("We can also do that this way:") #print We can also do that this way:
print("We'd have %d beans, %d jars, and %d crates." %(secretformula(startpoint))) #print We'd have 500000 beans, 500 jars, and 5 crates.
print("Exercise 25:  Even More Practice")
def breakwordssplit(stuff):
	words = stuff.split(" ")
	return words
def sortwordssorted(words):
	return sorted(words)
def printfirstwordpop(words):
	word = words.pop(0)
	return word
def printlastwordpop(words):
	word = words.pop(-1)
	return word
def sortsentencecallfunctions(sentence):
	#call functions breakwordssplit and sortwordssorted
	words = breakwordssplit(sentence)
	return sortwordssorted(words)
def printfirstandlastcallfunctions(sentence):
	#call functions breakwordssplit, printfirstwordpop, printlastwordpop
	words = breakwordssplit(sentence)
	print(printfirstwordpop(words))
	print(printlastwordpop(words))
def printfirstandlastsortedcallfunctions(sentence):
	#call functions breakwordssplit, sortwordssorted, printfirstwordpop, printlastwordpop.  RM:  break words first, sort words second.
	words = breakwordssplit(sentence)
	words = sortwordssorted(words)
	print(printfirstwordpop(words))
	print(printlastwordpop(words))
sentence = "All good things come to those who wait."
print(breakwordssplit(sentence)) #print ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
print(sortwordssorted(sentence)) #print [' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', 'A', 'a', 'c', 'd', 'e', 'e', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'l', 'l', 'm', 'n', 'o', 'o', 'o', 'o', 'o', 'o', 's', 's', 't', 't', 't', 't', 'w', 'w']
print(sortwordssorted(breakwordssplit(sentence))) #print ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
print(printfirstwordpop(breakwordssplit(sentence))) #print All  RM:  pop is a function for lists.
print(printlastwordpop(breakwordssplit(sentence))) #print wait.  RM:  pop is a function for lists.
printfirstandlastcallfunctions(sentence) #print All\n wait.
printfirstandlastsortedcallfunctions(sentence) #print All\n who
test = "the quick brown fox jumped over the lazy dog"
print(test.split(" ")) #print ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
print(sorted(test.split(" "))) #print ['brown', 'dog', 'fox', 'jumped', 'lazy', 'over', 'quick', 'the', 'the']
print(test.split(" ").pop(0)) #print the
print("Exercise 26:  Congratulations, Take A Test!")
#file saved exercise26learnpythonthehardway.txt
print("Exercise 27:  Memorizing Logic")
'''
1 != 0 True
1 != 1 False
0 != 1 True
0 != 0 False
1 == 0 False
1 == 1 True
0 == 1 False
0 == 0 True
'''
print("Exercise 28:  Boolean Practice")
print(True and True) #print True
print(1 and "top") #print top
print("top" and 1 and "la") #print la
print("top" or 1) #print top
print(1 or "top" or "la") #print 1
print(False and True) #print False
print(1==1 and 2==1) #print False
print("test" == "test") #print True
print(1==1 and 2!=1) #print True
print(True and 1==1) #print True
print(False and 0!=0) #print False
print(True or 1==1) #print True
print("test" == "testing") #print False
print(1!=0 and 2==1) #print False
print("test" != "testing") #print True
print("test" == 1) #print False
print(not (True and False)) #print True
print(not (1==1 and 0!=1)) #print False
print(not (10==1 or 1000 == 1000)) #print False
print(not (1!=10 or 3==4)) #print False
print(not ("testing" == "testing" and "Zed" == "Cool Guy")) #print True
print(1==1 and not ("testing"== 1 or 1==0)) #print True
print("chunky" == "bacon" and not (3==4 or 3==3)) #print False
print(3==3 and not ("testing" == "testing" or "Python" == "Fun")) #print False
print("Exercise 29:  What If")
people = 20
cats = 30
dogs = 15
if people < cats:
	print("Too many cats!  The world is doomed!") #print Too many cats!  The world is doomed!
if people > cats:
	print("Not many cats!  The world is saved!")
if people < dogs:
	print("The world is drooled on!")
if people > dogs:
	print("The world is dry!") #print The world is dry!
dogs += 5
if people >= dogs:
	print("People are greater than or equal to dogs.") #print People are greater than or equal to dogs.
if people <= dogs:
	print("People are less than or equal to dogs.") #print People are less than or equal to dogs.
if people == dogs:
	print("People are dogs.") #print People are dogs.
print("Exercise 30:  Else And If")
people = 30
cars = 40
buses = 15
if cars > people:
	print("We should take the cars.") #print We should take the cars.
elif cars < people:
	print("We should not take the cars.")
else:
	print("We can't decide")
if buses > cars:
	print("That's too many buses.")
elif buses < cars:
	print("Maybe we could take the buses.") #print Maybe we could take the buses.
else:
	print("We still can't decide.")
if people > buses:
	print("Alright, let's just take the buses.") #print Alright, let's just take the buses.
else:
	print("Find, let's stay home then.")
print("Exercise 31:  Making Decisions")
#print("You enter a dark room with two doors.  Do you go through door #1 or door #2?")
#door = int(input("You enter a dark room with two doors.  Do you go through door #1 or door #2? "))
door = 1
if door == 1:
	#bear = int(input("There's a giant bear here eating a cheese cake.  What do you do?  1. Take the cake or 2. Scream at the bear? "))
	bear = 1
	if bear == 1:
		print("The bear eats your face off.  Good job!")
	elif bear == 2:
		print("The bear eats your legs off.  Good job!")
	else:
		print("Well, doing %s is probably better.  Bear runs away." %bear)
elif door == 2:
	insanity = int(input("You stare into the endless abyss at Cthulu's retina.\n1. Blueberries.\n2. Yellow jacket clothespins.\n3. Understanding revolvers yelling melodies. "))
	if insanity == 1 or insanity == 2:
		print("Your body survives powered by a mind of jello.  Good job!")
	else:
		print("The insanity rots your eyes into a pool of muck.  Good job!")
else:
	print("You stumble around and fall on a knife and die.  Good job!")
print("Exercise 32:  Loops And Lists")
thecount = [1, 2, 3, 4, 5]
fruits = ["apples","oranges","pears","apricots"]
change = [1, "pennies",2,"dimes",3,"quarters"]
for number in thecount:
	print("This is count %d" %number) #print This is count 1\n . . . This is count 5
for fruit in fruits:
	print("A fruit of type: %s" %fruit) #print A fruit of type: apples\n . . . A fruit of type: apricots
for i in change:
	print("I got %r" %i) #print I got 1\n I got 'pennies'\n . . . I got 3\n I got 'quarters'
addelements = []
for i in range (0,6):
	print("Adding {} to the list." .format(i)) #print Adding 0 to the list.\n . . . Adding 5 to the list.
	addelements.append(i)
for i in addelements:
	print("Element was:",i) #print Element was: 0\n . . . Element was: 5
print("Exercise 33:  While Loops")
i = 0
numbers = []
while i < 6:
	print("At the top i is %d" %i) 
	numbers.append(i)
	i = i + 1
	print("Numbers now",numbers)
	print("At the bottom i is %d", i)
'''
At the top i is 0
Numbers now [0]
At the bottom i is %d 1
...
At the top i is 5
Numbers now [0, 1, 2, 3, 4, 5]
At the bottom i is %d 6
'''
print("The numbers: ")
for num in numbers:
	print(num) #print 0\n 1\n 2\n 3\n 4\n 5
print("Exercise 34:  Accessing Elements Of Lists")
print("Programmers pull elements out of a lists consistently by an address or an index.  Indices start at zero.  The indices number is a cardinal number.  Human translation is the ordinal number subtract one for the cardinal number; e.g. the third animal in the list is index second.  ordinal == ordered 1st; cardinal == cards at random zero.")
animals = ["bear","python","peacock","kangaroo","whale","platypus"]
print("The animal at 1. "+animals[1])
print("The 3rd animal. "+animals[2])
print("The 1st animal. "+animals[0])
print("The animal at 3. "+animals[3])
print("The 5th animal. "+animals[4])
print("The animal at 2. "+animals[2])
print("The 6th animal. "+animals[5])
print("The animal at 4. "+animals[4])
print("Exercise 35:  Branches And Functions")
from sys import exit
def goldroom():
	try:
		howmuchgold = int(input("This room is full of gold.  How much do you take? "))
	except ValueError:
		dead("Man, learn to type a number.  Learn to type an integer.")
	else:
		if howmuchgold < 50:
			print("Nice, you're not greedy, you win")
			exit(0)
		else:
			dead("You greedy bastard!")
def bearroom():
	print("There is a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of another door.")
	bearmoved = False
	while True:
		nextmove = input("How are you going to move the bear?  take honey, taunt bear, open door? ")
		if nextmove == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif nextmove == "taunt bear" and not bearmoved:
			print("The bear has moved from the door.  You can go through now.")
			bearmoved = True
		elif nextmove == "taunt bear" and bearmoved:
			dead("The bear gets pissed off and chews your leg off.")
		elif nextmove == "open door" and bearmoved:
			goldroom()
		else:
			dead("I got no idea what that means")
def cthulhuroom():
	print("Here your see the great evil Cthulhu.\nHe, it, whatever stares at you and you go insane.")
	nextmove = input("Do you flee for your life or eat your head?  flee or head? ")
	if nextmove == "flee":
		start()
	elif nextmove == "head":
		dead("Well that was tasty!")
	else:
		cthulhuroom()
def dead(why):
	print(why+" Good job!")
	exit(0)
def start():
	print("You are in a dark room.\nThere is a door to your right and left.")
	nextmove = input("Which one do you take?  right or left? ")
	if nextmove == "left":
		bearroom()
	elif nextmove == "right":
		cthulhuroom()
	else:
		dead("You stumble around the room until you starve.")
#start()
print("Exercise 36:  Designing And Debugging")
print("Use a while-loop to loop forever, and that means probably never.  However, sometimes rules are broken.")
print("Use a for-loop for all other kinds especially a fixed or limited number loops.")
print("Exercise 37:  Symbol Review")
print("Exercise 38:  Doing Things To Lists")
tenthings = "Apples Oranges Crows Telephone Light Sugar"
print("Wait, there's not 10 things in that list, let's fix that.")
stuff = tenthings.split(" ")
print(stuff) #print ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar']
morestuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]
while len(stuff) != 10:
	nextone = morestuff.pop()  #pop() removes the last indexed item in a list
	print("Adding",nextone)
	stuff.append(nextone)
	print("There's %d items now." %len(stuff))
print("There we got:",stuff) #print There we got: ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
print(stuff[1]) #print Oranges
print(stuff[-1]) #print Corn
print(" ".join(stuff)) #print Apples Oranges Crows Telephone Light Sugar Boy Girl Banana Corn
print(stuff.pop()) #print Corn
print(" ".join(stuff)) #print Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
print("#".join(stuff[3:5])) #print Telephone#Light
print("Exercise 39:  Dictionaries, Oh Lovely Dictionaries")
stuff = {"name":"Zed", "age":36, "height":6*12+2}
print(stuff["name"]) #print Zed
print(stuff["age"]) #print 26
print(stuff["height"]) #print 74
stuff["city"] = "San Francisco"
print(stuff) #print {'name': 'Zed', 'age': 36, 'height': 74, 'city': 'San Francisco'}
stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff) #print {'name': 'Zed', 'age': 36, 'height': 74, 'city': 'San Francisco', 1: 'Wow', 2: 'Neato'}
del stuff["city"]
del stuff[1]
del stuff[2]
print(stuff) #print {'name': 'Zed', 'age': 36, 'height': 74}
states = {"Oregon":"OR", "Florida":"FL", "California":"CA", "New York":"NY", "Michigan":"MI"}
cities = {"CA":"San Francisco", "MI":"Detroit", "FL":"Jacksonville"}
cities["NY"] = "New York"
cities["OR"] = "Portland"
print("NY State has: ", cities["NY"]) #print NY State has:  New York
print("OR State has: ", cities["OR"]) #print OR State has:  Portland
print("Michigan's abbreviation is: ",states["Michigan"]) #print Michigan's abbreviation is:  MI
print("Florida's abbreviation is: ",states["Florida"]) #print Florida's abbreviation is:  FL
print("Michigan has: ",cities[states["Michigan"]]) #print Michigan has:  Detroit
print("Florida has: ",cities[states["Florida"]]) #print Florida has:  Jacksonville
for state, abbrev in states.items():
	print("%s is abbreviated  %s " % (state, abbrev))
	'''
Oregon is abbreviated  OR 
Florida is abbreviated  FL 
California is abbreviated  CA 
New York is abbreviated  NY 
Michigan is abbreviated  MI 
'''
for abbrev, city in cities.items():
	print("%s has the city %s" %(abbrev, city))
'''
CA has the city San Francisco
MI has the city Detroit
FL has the city Jacksonville
NY has the city New York
OR has the city Portland
'''
for state, abbrev in states.items():
	print("%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev]))
'''
Oregon state is abbreviated OR and has city Portland
Florida state is abbreviated FL and has city Jacksonville
California state is abbreviated CA and has city San Francisco
New York state is abbreviated NY and has city New York
Michigan state is abbreviated MI and has city Detroit
'''
state = states.get("Texas", "No Texas")
print(state) #print No Texas
texascity = cities.get("TX","Doesn't exist")
print(texascity) #print Doesn't exist
print("The city for the state TX is: %s" %texascity) #print The city for the state TX is: Doesn't exist
cities["TX"] = "Austin"
texascity = cities.get("TX","Doesn't exist")
print(texascity) #print Austin
print("The city for the state TX is: %s" %texascity) #print The city for the state TX is: Austin
print("Exercise 40: Modules, Classes, And Objects")
mystuff = {"apple":"I am apples"}
print(mystuff["apple"]) #print I am apples
import mystuff #RM:  file mystuff.py
mystuff.apple() #print I am apples.  apple() function from mystuff.py python file.
print(mystuff.tangerine) #print Living reflection of a dream.  RM:  tangerine = "Living reflection of a dream" defined in mystuff.py python file.
thing = mystuff.MyStuff() #MyStuff() class is in mystuff.py python file
thing.apple() #return I am classy applies in class MyStuff from mystuff.py python file.
print(thing.tangerine) #print And now a thousand years between
class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def singmeasong(self):
		for eachlyrics in self.lyrics:
			print(eachlyrics)
happybirthdaylyrics = ["Happy birthday to you","I don't want to get sued","So I'll stop right there"]
happybirthday = Song(happybirthdaylyrics)
happybirthday.singmeasong() #return Happy birthday to you\n I don't want to get sued\n So I'll stop right there
bullsonparadelyrics = ["They rally around the family","With pockets full of shells"]
bullsonparade = Song(bullsonparadelyrics)
bullsonparade.singmeasong() #return They rally around the family\n With pockets full of shells
print("Exercise 41:  Learning To Speak Object Oriented")
classworddrill = "Tell python to make a new kind of thing."
objectworddrill = "Two meanings:  the most basic kind of thing and any instance of some thing."
instanceworddrill = "What you get when you tell Python to create a class."
defworddrill = "How you define a function inside a class."
selfworddrill = "Inside a functions in a class, self is a variable for the instance/object being accessed."
inheritanceworddrill = "The concept that one class can inherit traits from another class, much like you and your parents."
compositionworddrill = "The concept that a class can be composed of other classes as parts, much like how a car has wheels."
attributeworddrill = "A property classes have that are from composition and are usually variables."
isaworddrill = "A phase to say that something inherits from another, as in a salmon is-a fish."
hasaworddrill = "A phase to say that something is composed of other things or has a trait, as in a salmon has-a mouth."
class X1(object):
	def __init__(self):
		pass
	def printsomething(self):
		print("Make a class named X1 that is-an object.")
class X2(object):
	def __init__(self, J):
		self.jparameter = J
	def printsomething2(self):
		print("Class X2 has-a __init__ that takes self and J parameters.",self.jparameter)
class X3(object):
	def M(self, J):
		self.J = J
		print("Class X3 has-a function named M that takes self and J parameters.",self.J)
foo = X1() #set foo to an instance of class X1.
foo.printsomething() #return Make a class named X1 that is-an object.
fooreturnmakeaclassnamedX1again = X1()
fooreturnmakeaclassnamedX1again.printsomething() #return Make a class named X1 that is-an object.
foo2 = X2("Jam")
foo2.printsomething2() #return Class X2 has-a __init__ that takes self and J parameters. Jam
foo3 = X3() #from foo3 get the M function and call it with parameters self, J in class X3.
foo3.M("Jelly") #return Class X3 has-a function named M that takes self and J parameters. Jelly
foo.K = X3 #from foo.K get the K attribute and set it to X3.
print("Exercise 42:  Is-A, Has-A, Objects, and Classes")
class Animal(object):
	pass
class Dog(Animal):
	def __init__(self, name):
		self.name = name
	def printdogname(self):
		print(self.name+" is from class Dog(Animal).")
class Cat(Animal):
	def __init__(self, name):
		self.name = name
# class Employee(Person):
# 	def __init__(self, name, salary):
# 		super(Employee, self).__init__(name)
# 		#self.name = name
# 		self.salary = salary
class Fish(object):
	pass
class Salmon(Fish):
	pass
class Halibut(Fish):
	pass
rover = Dog("Rover")
rover.printdogname() #return Rover is from class Dog(Animal).
# satan = Cat("Satan")
# mary = Person("Mary")
# mary.pet = satan
# frank = Employee("Frank", 120000)
# frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()
print("Exercise 43:  Basic Object Oriented Analysis And Design")
print("Exercise 44:  Inheritance Vs. Composition")
#Inheritance indicates one class get most or all of its features from a parent class.  E.g. class Foo(Bar) make a class Foo which inherits from Bar.  Any instances of Foo also works of Bar.  Actions on the child imply an action on the parent.  Actions on the child override the action on the parent.  Actions on the child alter the action on the parent.
class Parent(object):
	def implicit(self):
		print("Parent implicit()")
class Child(Parent):
	#Child(Parent) inherits all behavior from Parent(object); e.g. if you put functions in a base class or parent class Parent(object) then all subclasses class Child(Parent) get the functions.
	pass
dad = Parent()
son = Child()
dad.implicit() #return Parent implicit()
son.implicit() #return Parent implicit()
class Parent(object):
	def override(self):
		print("Parent override()")
class Child(Parent):
	#Child(Parent) has its own override(self) function.  son is an instance of Child or son = Child().  Child(Parent) overrides override(self) function.
	def override(self):
		print("Child override()")
dad = Parent()
son = Child()
dad.override() #return Parent override()
son.override() #return Child override()
class Parent(object):
	def altered(self):
		print("Parent altered()")
class Child(Parent):
	def altered(self):
		print("Child before parent altered()")
		super(Child, self).altered() #get the Parent altered() from Parent(object) calling the altered() function
		print("Child after parent altered()")
dad = Parent()
son = Child()
dad.altered() #return Parent altered()
son.altered() #return Child before parent altered()\n Parent altered()\n Child after parent altered()
class Parent(object):
	def override(self):
		print("Parent override()")
	def implicit(self):
		print("Parent implicit()")
	def altered(self):
		print("Parent altered()")
class Child(Parent):
	def override(self):
		print("Child override()")
	def altered(self):
		print("Child before parent altered()")
		super(Child, self).altered()
		print("Child after parent altered()")
dad = Parent()
son = Child()
dad.implicit() #return Parent implicit()
son.implicit() #return Parent implicit()
dad.override() #return Parent override()
son.override() #return Child override()
dad.altered() #return Parent altered()
son.altered() #return Child before parent altered()\n Parent altered()\n Child after parent altered()
class Parent(object):
	def override(self):
		print("Parent override()")
class Child(Parent):
	def __init__(self, stuff):
		self.stuff = stuff
	def possession(self):
		print(self.stuff)
	def superwhat(self):
		super(Child, self).__init__()  #RM:  I don't know the purpose of super(Child, self).__init__().  The most common use of super() is actually in __init__ functions in base classes. This is usually the only place where you need to do some things in a child, then complete the initialization in the parent.
		super(Child, self).override()
dad = Parent()
dad.override() #return Parent override()
son = Child("pampers")
son.possession() #return pampers
son.override() #return Parent override()
son.superwhat() #return Parent override()
#RM:  skipped Composition pages 146-148.
#RM:  Satisifed skipped final exercises 45-52 because their projects game, input from browser, advanced user input.