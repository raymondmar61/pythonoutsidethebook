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
#start exercise 8














