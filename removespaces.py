#http://www.datasciencemadesimple.com/remove-spaces-in-python/
#We learn how to remove or strip leading, trailing, and duplicate spaces in python with lstrip(), rstrip(), and strip().
leftstripstring = "     This is a lstrip()."
print(leftstripstring) #print     This is a lstrip().
print(leftstripstring.lstrip()) #print This is a lstrip().
rightstripstring = "This is a rstrip()    "
print(rightstripstring) #print This is a rstrip()
print(rightstripstring.rstrip()) #print This is a rstrip()
stripstring = "    This is a strip()    "
print(stripstring) #print     This is a strip()
print(stripstring.strip()) #print This is a strip()

#Remove or strip all spaces
replacestring = "    This is a replace    ."
print(replacestring) #print     This is a replace    .
print(replacestring.replace(" ","")) #print Thisisareplace.

#Remove or strip duplicated space
import re
duplicatespacesstring = "    This  is a  duplicate   string     ."
print(duplicatespacesstring) #print     This  is a  duplicate   string  .
print(re.sub("  +", " ",duplicatespacesstring)) #print  This is a duplicate string .  RM:  It didn't work.  There is one space on the left and one space before the period
#We will be using regular expression to remove the unnecessary duplicate spaces in python.  sub() function: re.sub() function takes the duplicatespacesstring argument and replaces one or more space with single space as shown above so the output will be.