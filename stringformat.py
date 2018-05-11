#https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
#String Formatting with str.format() in Python 3 | DigitalOcean

#Formatters work by putting in one or more replacement fields or placeholders — defined by a pair of curly braces {} — into a string and calling the str.format() method. You’ll pass into the method the value you want to concatenate with the string. This value will be passed through in the same place that your placeholder is positioned when you run the program.

#Common %s %string reference
print("Sammy the %s has a pet %s." %("shark","pilot fish")) #print Sammy the shark has a pet pilot fish.

print("Sammy has {} ballons.".format(5)) #print Sammy has 5 ballons.
print("Sammy the {} has a pet {}.".format("shark","pilot fish")) #print Sammy the shark has a pet pilot fish.
#They are essentially the tuple data type and each individual value contained in the tuple can be called by its index number, which starts with the index number 0.  We can pass these index numbers into the curly braces that serve as the placeholders in the original string.
print("Sammy the {1} has a pet {0}.".format("shark","pilot fish")) #print Sammy the pilot fish has a pet shark.
print("Sammy is a {3}, {2}, and {1} {0}!".format("happy", "smiling", "blue", "shark")) #print Sammy is a shark, blue, and smiling happy!
#we can also introduce keyword arguments that are called by their keyword name
print("Sammy is a {pr}, {xvariable}, and {1} {0}!".format("happy", "smiling", pr="pr blue", xvariable="x variable")) #print Sammy is a pr blue, x variable, and smiling happy!
print("\n")

print("Sammy ate {0} percent of a {1}." .format(75,"pizza")) #print Sammy ate 75 percent of a pizza.
print("Sammy ate {1} percent of a {0}." .format("pizza",75)) #print Sammy ate 75 percent of a pizza.
#We used the syntax of {field_name:conversion} for the first curly brace replacement field to output a float.  Modifying precision will cause the number to be rounded.  Use .0f for no decimal places.  .d for integers only; can't round decimals to whole numbers.
print("Sammy ate {1:f} percent of a {0}." .format("pizza",75)) #print Sammy ate 75.000000 percent of a pizza.
print("Sammy ate {1:.3f} percent of a {0}." .format("pizza",75)) #print Sammy ate 75.000 percent of a pizza.
print("Sammy ate {1:.3f} percent of a {0}." .format("pizza",75.369963)) #print Sammy ate 75.370 percent of a pizza.
print("Sammy ate {1:d} percent of a {0}." .format("pizza",75)) #print Sammy ate 75 percent of a pizza.
print("\n")

#You can pad or create space around an element  by increasing field size through additional parameters.  We can add a number to indicate field size (in terms of characters) after the colon : in the curly braces of our syntax.  Default strings left-justified and numbers right-justified.
print("Sammy has {0:4} red {1:16}!" .format(5, "baloons")) #print Sammy has    5 red baloons         !
print("Sammy has {1:4} red {0:16}!" .format(5, "baloons")) #print Sammy has baloons red                5!  RM:  no extra pad because baloons has 7 characters
print("Sammy has {1:10} red {0:16}!" .format(5, "baloons")) #print Sammy has baloons    red                5!
print("Sammy has {0:<4} red {1:^16}!" .format(5, "baloons")) #print Sammy has 5    red     baloons     ! 5 is left-aligned and baloons is centered
print("{:*^20s}".format("Sammy")) #print *******Sammy********  20 characters string, Sammy is centered 5 characters, * is 15 characters
print("Sammy ate {1:5.0f} percent of a {0}." .format("pizza",75.963)) #print Sammy ate   76  percent of a pizza. first curly brackets is index 1 .format() totaling five characters float numbers round to whole number
print("Sammy ate {1:7.2f} percent of a {0}." .format("pizza",75.963)) #print Sammy ate   75.96  percent of a pizza. first curly brackets is index 1 .format() totaling seven characters float numbers round to two decimal places
print("\n")

openstring = "Sammy loves {}"
print(openstring.format("string add to sentence openstring.")) #print Sammy loves string add to sentence openstring.
openstring2 = "Sammy loves {} {}"
print(openstring2.format("string add to sentence openstring","one more.")) #print Sammy loves string add to sentence openstring one more.
openstring4 = "Sammy loves {} {}, with two random {} strings {}."
print(openstring4.format("string add to sentence openstring","one more", "zebra","land")) #print Sammy loves string add to sentence openstring one more, with two random zebra strings land.
print("\n")

numberofballoons = 8
print("Sammy has {} baloons today." .format(numberofballoons)) #print Sammy has 8 baloons today.
#We can use variables for both the original string and what is passed into the method.
#Variables can be easily substituted for each part of our formatter syntax construction. This makes it easier to work with when we are taking in user-generated input and assigning those values to variables.
sammy = "Sammy has {} baloons today"
numberofballoons = 8
print(sammy.format(numberofballoons)) #print Sammy has 8 baloons today
print("\n")

for i in range(3,13):
	#print(i,i*i,i*i*i) #print 3 9 27\n . . . 12 144 1728
	#print("{d}".format(i)) #RM: for some reason {d} error message despite working with integers
	print("{0:d}:".format(i),end="") #RM:  no error message
	print("{0:3d} {1:4d} {2:5d}".format(i,i*i,i*i*i)) #padding added to read easier
	print("{1:4d} {2:5d} {0:3d}".format(i,i*i,i*i*i)) #padding added to read easier
for i in range(3,13):
	print("{:6d} {:6d} {:6d}".format(i, i*i, i*i*i)) #print 3 9 27\n . . . 12 144 1728 with six character pad
#We can also manipulate the alignment of the columns by adding < , ^ , and > for text alignment, change d to f to add decimal places, change field name index numbers, and more to ensure that we are displaying the data as we would like.