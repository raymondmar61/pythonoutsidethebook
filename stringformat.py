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

#https://pyformat.info/
#PyFormat: Using % and .format() for great good!
#Basic formatting.  Simple positional formatting is probably the most common use-case. Use it if the order of your arguments is not likely to change and you only have very few elements you want to concatenate. Since the elements are not represented by something as descriptive as a name this simple style should only be used to format a relatively small number of elements.

print("old: %s %s" % ("one","two")) #print old: one two
print("new: {} {}" .format("one","two")) #print new: one two
print("old: %d %d" % (1,2)) #print old: 1 2
print("new: {} {}" .format(1,2)) #print new: 1 2
print("old: %d %d" % (2,1)) #print old: 2 1
print("new: {1} {0}" .format(1,2)) #print new: 1 2

#Value conversion.  The new-style simple formatter calls by default the __format__() method of an object for its representation. If you just want to render the output of str(...) or repr(...) you can use the !s or !r conversion flags.  In %-style you usually use %s for the string representation but there is %r for a repr(...) conversion.
class Data(object):
	def __str__(self):
		return "str"
	def __repr__(self):
		return "repr"
	def __str__(self):
		return "dodo"
print("%s" % (Data())) #print dodo
print("%r" % (Data())) #print repr
print("%s %r" % (Data(), Data())) #print dodo repr
print("%s %s" % (Data(), Data())) #print dodo dodo
print("{0!s}".format(Data())) #print dodo
print("{0!r}".format(Data())) #print repr
print("{0!s} {0!r}".format(Data())) #print dodo repr
print("{0!s} {0!s}".format(Data())) #print dodo dodo

#Padding and aligning strings.  By default values are formatted to take up only as many characters as needed to represent the content. It is however also possible to define that a value should be padded to a specific length. Unfortunately the default alignment differs between old and new style formatting. The old style defaults to right aligned while for new style it's left.  Default is right align for strings, integers, floats.
print("1234567890")
print("%10s" % ("Test")) #print       Test  6 padding left of Test for total characters 10.  Align right.
print("{:>10}" .format("test")) #print       test  6 padding left of test for align right.
print("%-10s" % ("Test")) #print Test       6 padding right of Test for total characters 10.  Align left.
print("{:10}" .format("test")) #print test       6 padding right of test for total characters 10.  Align left.
print("{:_<10}" .format("test")) #print test______ 6 padding right of test for total characters 10.  Align left.
print("{:_^10}" .format("test")) #print ___test___ centered 3 padding left and 3 padding right of test for total characters 10.  Align center.
print("{:_^10}" .format("tests")) #print __tests___ centered 2 padding left and 3 padding right of tests for total characters 10.  Align center.
print("{:_^6}" .format("zip")) #print _zip__ centered 1 padding left and 2 padding right of tests for total characters 10.  Align center.
print("1234567890")

#Truncate or truncating long strings.  Inverse to padding it is also possible to truncate overly long values to a specific number of characters.
print("1234567890")
print("%.5s" % ("xylophone")) #print xylop output 5 characters
print("{:.5}".format("xylophone")) #print xylop output 5 characters

#combine truncate and padding
print("{:_>10.5}".format("xylophone")) #print _____xylop right align 5 characters with _____ completing the 10 characters output
print("{:_>10.5}".format("xylophone"[::-1])) #print _____enohp right align 5 characters with _____ completing the 10 characters output

#Numbers integers, floats
print("%d" % (42)) #print 42
print("{}".format(42)) #print 42
print("{:d}".format(42)) #print 42
print("%f" % (3.141592653)) #print 3.141593
print("{}".format(3.141592653)) #print 3.1415932653
print("{:f}".format(3.141592653)) #print 3.141593
print("1234567890")
print("%4d"%(42)) #print   42 right align
print("{:4d}".format(42)) #print   42 right align
print("1234567890")
print("%6.3f"%(3.141592653589793)) #print  3.142 right align three decimal places with rounding up
print("{:6.3f}".format(3.141592653589793)) #print  3.142 right align three decimal places with rounding up
print("%07.3f"%(3.141592653589793)) #print 003.142 right align three decimal places with rounding up
print("{:07.3f}".format(3.141592653589793)) #print 003.142 right align three decimal places with rounding up
print("1234567890")
print("%08d"%(42)) #print 00000042 right align
print("{:08d}".format(42)) #print 00000042 right align
print("%+d" % (42)) #print +42
print("{:+}".format(42)) #print +42
print("{:+d}".format(42)) #print +42
print("%-d" % (23)) #print 23
print("{:-}".format(23)) #print 23
print("{:-d}".format(23)) #print 23
print("%d" % (-23)) #print -23
print("{:}".format(-23)) #print -23
print("{:d}".format(-23)) #print -23
print("1234567890")
print("{:5d}".format(-23)) #print  -23 left align with two spaces
print("{:=5d}".format(-23)) #print -  23 left align with two spaces between negative and 23
print("{:+5d}".format(23)) #print   +23 left align with two spaces
print("{:=+5d}".format(23)) #print +  23 left align with two spaces between positive and 23

#Named placeholders, dictionary, list, class
data = {"first": "cookies", "last": "popcorn"}
print("%s %s" % (data["first"], data["last"])) #print cookies popcorn
print("%(first)s %(last)s" % (data)) #print cookies popcorn
print("{first} {last}".format(**data)) #print cookies popcorn
print("{first} {last}".format(first="crackers", last="peanuts")) #print crackers peanuts
print("{last} {first}".format(first="crackers", last="peanuts")) #print peanuts, crackers
person = {"first": "Jean-Luc", "last": "Picard"}
print("{p[first]} {p[last]}".format(p=person)) #print Jean-Luc Picard
datalist = [4, 8, 15, 16, 23, 42]
print("{d[4]} {d[5]}".format(d=datalist)) #print 23 42
class Plant(object):
	type = "tree"
print("{p.type}".format(p=Plant())) #print tree
class Plant2(object):
	type= "tree"
	kinds = [{"name":"oak"},{"name":"maple"}]
print("{p2.type}: {p2.kinds[0][name]}".format(p2=Plant2())) #print tree: oak

#Datetime.  New style formatting also allows objects to control their own rendering. This for example allows datetime objects to be formatted inline.
#datetime(year, month, date, hour, minute)
print("{:%Y-%m-%d %H:%M}".format(datetime(2001, 2, 3, 4, 5))) #print 2001-02-03 04:05
print("{:%m/%d/%y %H:%M}".format(datetime(2001, 2, 3, 4, 5))) #print 02/03/01 04:05
print("{:%m/%d/%Y %H:%M}".format(datetime(2001, 7, 15, 18, 35))) #print 07/15/2001 18:35
print("{:%m/%d/%Y %H:%M}".format(datetime(2001, 7, 15, 18, 35))) #print 07/15/2001 18:35
print("{:%m/%d/%Y %I:%M %p}".format(datetime(2001, 7, 15, 18, 35))) #print 07/15/2001 06:35 PM
print("{:%m/%d/%y %I:%M%p}".format(datetime(2001, 7, 15, 18, 35))) #print 07/15/01 06:35PM
print("{:%m/%d/%y %I:%M%p}".format(datetime(2001, 7, 15, 18, 35)).lower()) #print 07/15/01 06:35pm

#Parametrized formats.  new style formatting allows all of the components of the format to be specified dynamically using parametrization. Parametrized formats are nested expressions in braces that can appear anywhere in the parent format after the colon.
print("1234567890")
print("{:{align}{width}}".format("test", align="^", width="10")) #print    test
print("{:_{align}{width}}".format("test", align="^", width="10")) #print ___test___
print("%.*s = %.*f"%(3, "Gibberish",3,2.7182)) #print Gib = 2.718
print("{:.{prec}} = {:.{prec}f}".format("Gibberish", 2.7182, prec=3)) #print Gib = 2.718
print("%*.*f"%(5,2,2.7182)) #print  2.72
print("{:{width}.{prec}f}".format(2.7182, width=5, prec=2)) #print  2.72
#print("{:_{width}.{prec}f}".format(2.7182, width=5, prec=2)) #error message ValueError: Invalid format specifier
print("{:0{width}.{prec}f}".format(2.7182, width=5, prec=2)) #print 02.72
print("{:{prec}} = {:{prec}}".format("Gibberish", 2.7182, prec=".3")) #print Gib = 2.72
print("{:{prec}} = {:{prec}}".format("Gibberish", 2.7182, prec=".6")) #print Gibber = 2.7182
print("{:{prec}} = {:0{width}{prec}}".format("Gibberish", 3.1, prec=".6", width="7")) #print Gibber = 00003.1
from datetime import datetime
dt = datetime(2001,3,15,19,30)
print(dt) #print 2001-03-15 19:30:00
print("{:{dfmt} {tfmt}}".format(dt, dfmt="%Y-%m-%d", tfmt="%H:%M")) #print 2001-03-15 19:30
print("{:{dfmt} {tfmt}}".format(dt, dfmt="%m/%d/%Y", tfmt="%H:%M")) #print 03/15/2001 19:30
print("{:{dfmt} {tfmt}}".format(dt, dfmt="%m/%d/%Y", tfmt="%I:%M%p")) #print 03/15/2001 07:30PM
#The nested formats can be positional arguments. Position depends on the order of the opening curly braces
print("{:{}{}{}.{}}".format(2.7182818284,">","+",10,3)) #print      +2.72
print("{:{}{}{}.{}}".format(2.7182818284,"0>","+",10,3)) #print 00000+2.72
print("{:{}{}{}.{}}".format(2.7182818284,"0>","+",10,5)) #print 000+2.7183
print("{:{}{}{}.{}}".format(2.7182818284,"0<","+",10,3)) #print +2.7200000
#keyword arguments can be added to the mix as before
print("{:{}{sign}{}.{}}".format(2.7182818284,">",10,3,sign="+")) #print      +2.72

#Custom objects. The datetime example works through the use of the __format__() magic method. You can define custom format handling in your own objects by overriding this method. This gives you complete control over the format syntax used.
class HAL9000(object):
	def __format__(self, format):
		if (format == "open-the-pod-bay-doors"):
			return "I'm afraid I can't do that."
		return "HAL 9000"
print("{:open-the-pod-bay-doors}".format(HAL9000())) #print I'm afraid I can't do that.

#35. Write a Python program to display a number with a comma separator.
print("{:,}".format(1000000)) #print 1,000,000
print("{:,}".format(123456789)) #print 123,456,789
print("{:,}".format(-987654321)) #print -987,654,321

#36. Write a Python program to format a number with a percentage.
half = 1/2
print("Percentage: {}%".format(half)) #print Percentage: 0.5%
third = 1/3
print("Percentage: {}%".format(third)) #print Percentage: 0.3333333333333333%

#20. Write a Python program to print a tuple with string formatting. Sample tuple: (100, 200, 300).  Output: This is a tuple (100, 200, 300).
sampletuple = (100, 200, 300)
print("This is a tuple", sampletuple) #print This is a tuple (100, 200, 300)
print("This is a tuple {0}".format(sampletuple)) #print This is a tuple (100, 200, 300)
print("This is a tuple {}".format(sampletuple)) #print This is a tuple (100, 200, 300)