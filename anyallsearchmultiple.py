#https://stackoverflow.com/questions/36550812/how-can-i-detect-multiple-words-from-a-string-python
stringword = "My favorite board games are Puerto Rico, Dominion, Pandemic, Mahjong, Chess, and Settlers of Catan."
findthesewords = ["Puerto","Mahjong","Settlers"]
if any(eachfindthesewords in stringword for eachfindthesewords in findthesewords):
	print("True") #print True
findthesewords2 = ["UNO","Monopoly","Jacks"]
if any(eachfindthesewords2 in stringword for eachfindthesewords2 in findthesewords2):
	print("True 2")
findthesewords3 = ["Candyland","Chutes And Ladders","Pandemic"]
if any(eachfindthesewords3 in stringword for eachfindthesewords3 in findthesewords3):
	print("True 3") #print True 3
for eachstringword in stringword.split():
	if any(eachfindthesewords in eachstringword for eachfindthesewords in findthesewords):
		print(eachstringword,"for true") #print Puerto for true\n Mahjong, for true\n Settlers for true

stringword = "My favorite board games are Puerto Rico, Dominion, Pandemic, Mahjong, Chess, and Settlers of Catan."
findthesewords = ["Puerto","Mahjong","Settlers"]
if all(eachfindthesewords in stringword for eachfindthesewords in findthesewords):
	print("All True") #print All True
findthesewords2 = ["UNO","Monopoly","Jacks"]
if all(eachfindthesewords2 in stringword for eachfindthesewords2 in findthesewords2):
	print("All True 2")

#https://stackoverflow.com/questions/16505456/how-exactly-does-the-python-any-function-work/16505590
names = ["King","Queen","Joker"]
print(any(anynames in "King and John" for anynames in names)) #print True
print(all(allnames in "King and John" for allnames in names)) #print False
print(all(allnames in "King and Queen" for allnames in names)) #print False
print(any(anynames in "King Queen" for anynames in names)) #print True
print(all(allnames in "King Queen" for allnames in names)) #print False
print(all(allnames in "King Queen Joker" for allnames in names)) #print True
print("\n")

#https://thepythonguru.com/python-builtin-functions/any/
#The any() function test whether any item in the iterable evaluates to True or not.  It accepts an iterable and returns True, if at least one item in the iterable is true, otherwise, it returns False.  any(iterable)-->returns boolean
print(any([10, "", "one"])) #print True
print(any(("",{}))) #print False
print(any([])) #print False
numbergenerator = [i for i in range(0,5)]
print(numbergenerator) #print [0, 1, 2, 3, 4]
print(any(numbergenerator)) #print True
print("\n")

#https://www.programiz.com/python-programming/methods/built-in/all
#The all() function returns True when all elements in the given iterable are true. all(iterable).  The iterable can be a list, tuple, dictionary which contains elements.
l = [1, 3, 4, 5]
print(all(l)) #print True
l = [0, False]
print(all(l)) #print False
l = [1, 3, 4, 0]
print(all(l)) #print False
l = [0, False, 5]
print(all(l)) #print False
l = []
print(all(l)) #print True  RM:  empty iterable True if all() and False if any()
string = "This is good"
print(all(string)) #print True
#In case of dictionaries, if all keys (not values) are true or the dictionary is empty, all() returns True. Else, it returns false
dictionaryd = {0: 'False', 1: 'False'}
print(all(dictionaryd)) #print False
dictionaryd = {1: 'True', 2: 'True'}
print(all(dictionaryd)) #print True
dictionaryd = {1: 'True', False: 0}
print(all(dictionaryd)) #print False
dictionaryd = {}
print(all(dictionaryd)) #print True
# 0 is False
# '0' is True
dictionaryd = {'0': 'True'}
print(all(dictionaryd)) #print True
print("\n")

#https://stackoverflow.com/questions/19389490/how-do-pythons-any-and-all-functions-work
#all checks for elements to be False (so it can return False), then it returns True if none of them were False.  All stops when there is a False.
#any checks for elements to be True (so it can return True), then it returns False if none of them were True.  Any stops when there is a True.
print(any([])) #print False
print(all([])) #print True
def noisy_iterator(iterable):
    for i in iterable:
        print('yielding ' + repr(i))
        yield i
all(noisy_iterator([1, 2, 3, 4])) #print yielding 1\n yielding 2\n yielding 3\n yielding 4
print(all(noisy_iterator([1, 2, 3, 4]))) #print yielding 1\n yielding 2\n yielding 3\n yielding 4\n True
all(noisy_iterator([0, 1, 2, 3, 4])) #print yielding 0.  all stops on the first False boolean check.
print(all(noisy_iterator([0, 1, 2, 3, 4]))) #print yielding 0\n False.  all stops on the first False boolean check.
def noisy_iterator(iterable):
    for i in iterable:
        #print('yielding ' + str(i))
        print('yielding ' + repr(i))
        yield i
any(noisy_iterator([0, 0.0, '', (), [], {}])) #print yielding 0\n yielding 0.0\n yielding ''\n yielding ()\n yielding []\n yielding {}
print(any(noisy_iterator([0, 0.0, '', (), [], {}]))) #print yielding 0\n yielding 0.0\n yielding ''\n yielding ()\n yielding []\n yielding {}\n False
any(noisy_iterator([1, 0, 0.0, '', (), [], {}])) #print yielding 1.  any stops on the first True boolean check.
print(any(noisy_iterator([1, 0, 0.0, '', (), [], {}]))) #print yielding 1\n True.  any stops on the first True boolean check.