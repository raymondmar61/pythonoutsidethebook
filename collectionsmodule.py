#Python collections module comes with with a number of container data types.
#http://book.pythontips.com/en/latest/collections.html
#https://pymbook.readthedocs.io/en/latest/collections.html
#https://www.journaldev.com/19103/python-collections
#https://howchoo.com/g/mtbhy2qzota/python-collections
#https://dzone.com/articles/python-collections-high-performing-containers-for

from collections import defaultdict
#The default dictionary can contain duplicate keys. The advantage of using default dictionary is that we can collect items which belong to the same key.  defaultdict is a dictionary like object which provides all methods provided by dictionary but takes first argument (default_factory) as default data type for the dictionary.  Default Dictionary allows the user to specify a function to be called when a key is not present in the dictionary.  When a dictionary is queried for a key which does not exist, the function passed as an argument to the named argument "default_dictionary" of default_dict() will be called to set a value for a given "key" into the dictionary.
colors = (("yellow","banana"), ("red","apple"),("blue","sky"),("green","trees"),("white","walls"),("black","shirt"),("red","fire engine"))
print(colors) #print (('yellow', 'banana'), ('red', 'apple'), ('blue', 'sky'), ('green', 'trees'), ('white', 'walls'), ('black', 'shirt'), ('red', 'fire engine'))
# favoritecolors = defaultdict(colors)
# print(favoritecolors) #TypeError: first argument must be callable or None
favoritecolors = defaultdict(list)
for name, colors in colors:
	favoritecolors[name].append(colors)
print(favoritecolors) #print defaultdict(<class 'list'>, {'yellow': ['banana'], 'red': ['apple', 'fire engine'], 'blue': ['sky'], 'green': ['trees'], 'white': ['walls'], 'black': ['shirt']})
print(list(favoritecolors.items())) #print [('yellow', ['banana']), ('red', ['apple', 'fire engine']), ('blue', ['sky']), ('green', ['trees']), ('white', ['walls']), ('black', ['shirt'])]
print(favoritecolors["red"]) #print ['apple', 'fire engine']
print(favoritecolors["white"]) #print ['walls']
print(favoritecolors["sky"]) #print []
days = [('monday', 2.5), ('wednesday', 2), ('friday', 1.5), ('monday', 3), ('tuesday', 3.5), ('thursday', 2), ('friday', 2.5)]
activedays = defaultdict(float)
for k, v in days:
	activedays[k] += v
print(defaultdict) #print <class 'collections.defaultdict'>
print(activedays) #print defaultdict(<class 'float'>, {'monday': 5.5, 'wednesday': 2.0, 'friday': 4.0, 'tuesday': 3.5, 'thursday': 2.0})
books = defaultdict(lambda:"Not Available") #books is a defaultdict.  It sets Not Available as a value if any nonexistent key is accessed.
books["a"] = "Arts"
books["b"] = "Biology"
books["c"] = "Chemistry"
print(books) #print defaultdict(<function <lambda> at 0x7f2097ea4e18>, {'a': 'Arts', 'b': 'Biology', 'c': 'Chemistry'})
print(books["z"]) #print Not Available
print(books) #print defaultdict(<function <lambda> at 0x7fc71b331e18>, {'a': 'Arts', 'b': 'Biology', 'c': 'Chemistry', 'z': 'Not Available'})
booksaslist = [("a","Arts"),("b","Biography"),("c","Computer"),("a","Army"),("d","Dogs")] #list of tuples
favoritebooks = defaultdict(list)
for key, value in booksaslist:
	favoritebooks[key].append(value)
print(favoritebooks) #print defaultdict(<class 'list'>, {'a': ['Arts', 'Army'], 'b': ['Biography'], 'c': ['Computer'], 'd': ['Dogs']})
print(favoritebooks.items()) #print dict_items([('a', ['Arts', 'Army']), ('b', ['Biography']), ('c', ['Computer']), ('d', ['Dogs'])])
print(list(favoritebooks.items())) #print [('a', ['Arts', 'Army']), ('b', ['Biography']), ('c', ['Computer']), ('d', ['Dogs'])]


from collections import OrderedDict
#OrderedDict keeps its entries sorted as they are iniitially inserted.  The order of insertion is maintained when key and values are inserted into the dictionary. If we try to insert a key again, this will overwrite the previous value for that key.  OrderedDict can sort and store or rank.
stocks = {"GOOG": 520.54, "FB": 76.45, "YHOO": 39.28, "AMZN": 305.21, "AAPL": 99.76}
for key, value in stocks.items():
	print(key, value) #RM:  no OrderedDict required.  Prints in order GOOG, FB, YHOO, AMZN, AAPL
stocksordereddict = OrderedDict({"GOOG": 520.54, "FB": 76.45, "YHOO": 39.28, "AMZN": 305.21, "AAPL": 99.76})
for key, value in stocksordereddict.items():
	print(key, value) #prints Prints in order GOOG, FB, YHOO, AMZN, AAPL
thedictionary = OrderedDict()
thedictionary = {"a":1, "b":10, "c":8, "d":19, "e":80, "f":0}
for key, value in thedictionary.items():
	print(key, value) #prints Prints in order a, b, c, d, e, f
thedictionary.popitem()
print(thedictionary) #print {'a': 1, 'b': 10, 'c': 8, 'd': 19, 'e': 80}
#thedictionary.popitem(last=False) #TypeError: popitem() takes no keyword arguments
#for letter in reversed(thedictionary): #TypeError: 'dict' object is not reversible
#	print(letter)
armyalphabet = OrderedDict()
armyalphabet["a"] = "Alpha"
armyalphabet["b"] = "Bravo"
armyalphabet["c"] = "Charlie"
armyalphabet["d"] = "Delta"
armyalphabet["e"] = "Echo"
print(armyalphabet) #print OrderedDict([('a', 'Alpha'), ('b', 'Bravo'), ('c', 'Charlie'), ('d', 'Delta'), ('e', 'Echo')])
print(armyalphabet.items()) #print odict_items([('a', 'Alpha'), ('b', 'Bravo'), ('c', 'Charlie'), ('d', 'Delta'), ('e', 'Echo')])
print(armyalphabet.keys()) #print odict_keys(['a', 'b', 'c', 'd', 'e'])
print(armyalphabet.values()) #print odict_values(['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo'])
armyalphabet2 = OrderedDict()
armyalphabet2 = {"a":"Alpha", "b":"Bravo", "c":"Charlie", "d":"Delta", "e":"Echo"}
print(armyalphabet2) #print {'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo'}
print(armyalphabet2.items()) #print dict_items([('a', 'Alpha'), ('b', 'Bravo'), ('c', 'Charlie'), ('d', 'Delta'), ('e', 'Echo')])
print(armyalphabet2.keys()) #print dict_keys(['a', 'b', 'c', 'd', 'e'])
print(armyalphabet2.values()) #print dict_values(['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo'])
#RM:  armyalphabet2 is not an OrderedDict.  It's a plain dictionary it seems.
armyalphabet3 = OrderedDict({"a":"Alpha", "b":"Bravo", "c":"Charlie", "d":"Delta", "e":"Echo"})
print(armyalphabet3) #print OrderedDict([('a', 'Alpha'), ('b', 'Bravo'), ('c', 'Charlie'), ('d', 'Delta'), ('e', 'Echo')])
print(armyalphabet3.items()) #print odict_items([('a', 'Alpha'), ('b', 'Bravo'), ('c', 'Charlie'), ('d', 'Delta'), ('e', 'Echo')])
print(armyalphabet3.keys()) #print odict_keys(['a', 'b', 'c', 'd', 'e'])
print(armyalphabet3.values()) #print odict_values(['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo'])
keyvalues = [(1,"won"),(2,"shoe"),(3,"tree"),(4,"door"),(5,"wine"),(6,"six")]  #OrderedDict can also be created by passing a dictionary or a list of key, value pair tuples.
keyvaluesorddict = OrderedDict(keyvalues)
print(keyvaluesorddict) #print OrderedDict([(1, 'won'), (2, 'shoe'), (3, 'tree'), (4, 'door'), (5, 'wine'), (6, 'six')])
studentscores = {"Ason":85, "Shawn":99, "Ron":78, "Hope":67, "Skip":100}
print(studentscores) #print {'Ason': 85, 'Shawn': 99, 'Ron': 78, 'Hope': 67, 'Skip': 100}
print(sorted(studentscores.items(), key=lambda t:t[0])) #print [('Ason', 85), ('Hope', 67), ('Ron', 78), ('Shawn', 99), ('Skip', 100)]
#print(sorted(studentscores.items(), key=lambda t:-t[0])) #error message TypeError: bad operand type for unary -: 'str'
print(sorted(studentscores.items(), key=lambda t:t[1])) #print [('Hope', 67), ('Ron', 78), ('Ason', 85), ('Shawn', 99), ('Skip', 100)]
print(sorted(studentscores.items(), key=lambda t:-t[1])) #print [('Skip', 100), ('Shawn', 99), ('Ason', 85), ('Ron', 78), ('Hope', 67)]
rankOrder = OrderedDict(sorted(studentscores.items(), key=lambda t:-t[1]))
print(rankOrder) #print OrderedDict([('Skip', 100), ('Shawn', 99), ('Ason', 85), ('Ron', 78), ('Hope', 67)])

from collections import Counter
#Counter allows us to count the occurrences of a particular item.  Counter counts hashable objects.  Elements are stored as dictionary keys and counts are stored as values which can be zero or negative.  The Counter collections allow us to keep a count of all the items which are inserted into the collection with the keys.  The key is the item to be counted and value is the count.  Counter is used for rapid tallies. It is a dictionary, where the elements are stored as keys and their counts are stored as values.
colors = (("yellow","banana"), ("blue","sky"),("green","trees"),("white","walls"),("black","shirt"),("red","fire engine"),("white","heaven"))
numberlistofwords = Counter(whatever for whatever, colors in colors) #RM:  it appears the for and the in are key words, in is the source
print(numberlistofwords) #print Counter({'white': 2, 'yellow': 1, 'blue': 1, 'green': 1, 'black': 1, 'red': 1})
countthefollowingtext = "The late Steve Jobs said, \"You can\'t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.\"  There are sayings regarding a person living a bad life.  It can\'t get worse; it can only get better.  Everyone must experience hell before heaven.  Frustrations, mistakes, and pain are part of growing up.  Be prepared for failures before success.  Everyone has bad years and everyone has good years.  You win some and you lose some.  Sometimes bad years are nobody\'s fault--it\'s life.  The bottom line is everything we do today affects tomorrow; in particular, if life is bad today, then do something for a good life tomorrow.  Trust hard work intelligently, good luck, and favorable timing everything goes well soon.  There is a light at the end of the tunnel.  Hope for the best."
countthefollowingtext = countthefollowingtext.split()
print(Counter(countthefollowingtext)) #print Counter({'the': 5, 'a': 4, 'bad': 4, 'and': 4, 'connect': 3, 'you': 3, 'are': 3, 'for': 3, 'good': 3, 'is': 3, 'The': 2, "can't": 2, 'dots': 2, 'looking': 2, 'can': 2, 'only': 2, 'in': 2, 'There': 2, 'life.': 2, 'get': 2, 'Everyone': 2, 'before': 2, 'of': 2, 'has': 2, 'years': 2, 'everything': 2, 'do': 2, 'life': 2, 'late': 1, 'Steve': 1, 'Jobs': 1, 'said,': 1, '"You': 1, 'forward;': 1, 'them': 1, 'backwards.': 1, 'So': 1, 'have': 1, 'to': 1, 'trust': 1, 'that': 1, 'will': 1, 'somehow': 1, 'your': 1, 'future."': 1, 'sayings': 1, 'regarding': 1, 'person': 1, 'living': 1, 'It': 1, 'worse;': 1, 'it': 1, 'better.': 1, 'must': 1, 'experience': 1, 'hell': 1, 'heaven.': 1, 'Frustrations,': 1, 'mistakes,': 1, 'pain': 1, 'part': 1, 'growing': 1, 'up.': 1, 'Be': 1, 'prepared': 1, 'failures': 1, 'success.': 1, 'everyone': 1, 'years.': 1, 'You': 1, 'win': 1, 'some': 1, 'lose': 1, 'some.': 1, 'Sometimes': 1, "nobody's": 1, "fault--it's": 1, 'bottom': 1, 'line': 1, 'we': 1, 'today': 1, 'affects': 1, 'tomorrow;': 1, 'particular,': 1, 'if': 1, 'today,': 1, 'then': 1, 'something': 1, 'tomorrow.': 1, 'Trust': 1, 'hard': 1, 'work': 1, 'intelligently,': 1, 'luck,': 1, 'favorable': 1, 'timing': 1, 'goes': 1, 'well': 1, 'soon.': 1, 'light': 1, 'at': 1, 'end': 1, 'tunnel.': 1, 'Hope': 1, 'best.': 1})
print(Counter(countthefollowingtext).most_common(10)) #print [('the', 5), ('a', 4), ('bad', 4), ('and', 4), ('connect', 3), ('you', 3), ('are', 3), ('for', 3), ('good', 3), ('is', 3)] returns returns a list of tuples - the tuple structured like this (value, frequency).
print(Counter("Thequickbrownfoxjumpedoverthelazydog").most_common(6)) #print [('e', 4), ('o', 4), ('h', 2), ('u', 2), ('r', 2), ('d', 2)]
letters = Counter(a=4, b=2, c=0, d=-2, e=3)
print(list(letters.elements())) #print ['a', 'a', 'a', 'a', 'b', 'b', 'e', 'e', 'e']
countanimals = Counter({"birds":200, "lizards": 340, "hamsters":120})
print(countanimals) #print Counter({'lizards': 340, 'birds': 200, 'hamsters': 120})
print(countanimals["hamsters"]) #print 120
integerslist = [1,2,3,4,1,2,3,1,2,1]
print(Counter(integerslist)) #print Counter({1: 4, 2: 3, 3: 2, 4: 1})
print(Counter(integerslist).items()) #print dict_items([(1, 4), (2, 3), (3, 2), (4, 1)])
print(Counter(integerslist).keys()) #print dict_keys([1, 2, 3, 4])
print(Counter(integerslist).values()) #print dict_values([4, 3, 2, 1])
#or
integerslist = [1,2,3,4,1,2,3,1,2,1]
countermethods = Counter(integerslist)
print(countermethods) #print Counter({1: 4, 2: 3, 3: 2, 4: 1})
print(countermethods.items()) #print dict_items([(1, 4), (2, 3), (3, 2), (4, 1)])
print(countermethods.keys()) #print dict_keys([1, 2, 3, 4])
print(countermethods.values()) #print dict_values([4, 3, 2, 1])

#When dealing with multiple Counter objects you can perform operations against them. For instance, you can add two counters which would add the counts for each key. You can also perform intersection or union. If I wanted to compare the values for given keys between two counters, I can return the minimum or maximum values only. For example, a student has taken 4 quizzes two times each. She is allowed to keep the highest score for each quiz.
first_attempt = Counter({1: 90, 2: 65, 3: 78, 4: 88})
second_attempt = Counter({1: 88, 2: 84, 3: 95, 4: 92})
final = first_attempt | second_attempt
print(final) #print Counter({3: 95, 4: 92, 1: 90, 2: 84}) #Maximum values
a = Counter(x=1, y=2, z=3)
b = Counter(x=2, y=3, z=4)
print(Counter(a+b)) #print Counter({'z': 7, 'y': 5, 'x': 3}) #Sum values
print(a+b) #print Counter({'z': 7, 'y': 5, 'x': 3}) #Sum values
print(a-b) #print Counter() #Subtraction values, negative values ommitted
print(b-a) #print Counter({'x': 1, 'y': 1, 'z': 1}) #Subtraction values, negative values ommitted
print(a&b) #print Counter({'z': 3, 'y': 2, 'x': 1}) #Minimum values
print(a|b) #print Counter({'z': 4, 'y': 3, 'x': 2}) #Maximum values

from collections import deque
#deque stands for "double-ended queue" and is used as a stack or queue.  deque provides you with a double ended queue which means that you can append and delete elements from either side of the queue.  If you're structuring the data in a way that requires quickly appending to either end or retrieving from either end then you would want to use a deque.  Pronounced "deck".
dequeobject = deque()
dequeobject.append("Oh")
dequeobject.append("say")
dequeobject.append("can")
dequeobject.append(5)
print(dequeobject) #print deque(['Oh', 'say', 'can', 5])
print(len(dequeobject)) #print 4
print(dequeobject[0]) #print Oh
print(dequeobject[3]) #print 5
print(dequeobject[-1]) #print 5
dequeobject.appendleft("Left Oh")
print(dequeobject) #print deque(['Left Oh', 'Oh', 'say', 'can', 5])
d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
d.append(10)
print(d) #print deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 10])
d.remove(7)
print(d)  #print deque([0, 1, 2, 3, 4, 5, 6, 8, 10])
dequeobject = deque(range(0,5)) #RM:  new object for dequeobject
print(dequeobject) #print deque([0, 1, 2, 3, 4])
dequeobject.popleft()
print(dequeobject) #print deque([1, 2, 3, 4])
dequeobject.pop()
print(dequeobject) #print deque([1, 2, 3])
#We can also limit the amount of items a deque can hold. By doing this when we achieve the maximum limit of our deque it will simply pop out the items from the opposite end.
dequeobject = deque(maxlen=10)
dequeobject = deque(range(0,20))
print(dequeobject) #print deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
dequeobject = deque(range(0,20))
dequeobject = deque(maxlen=10)
print(dequeobject) #print deque([], maxlen=10) RM:  maxlen doesn't work
# dequeinput = deque()
# inputuser = ""
# while inputuser != "quit":
# 	inputuser = input("Enter a text")
# 	if inputuser == "quit":
# 		break
# 	else:
# 		dequeinput.append(inputuser)
# 		print(dequeinput)
print("\n")
maxlengthfive = deque([1,2,3,4,5], maxlen=5)
print(maxlengthfive) #print deque([1, 2, 3, 4, 5], maxlen=5)
maxlengthfive.append(6)
print(maxlengthfive) #print deque([2, 3, 4, 5, 6], maxlen=5)
maxlengthfive.appendleft(-10)
print(maxlengthfive) #print deque([-10, 2, 3, 4, 5], maxlen=5)
maxlengthfive.extend([7, 100, 1004])
print(maxlengthfive) #print deque([4, 5, 7, 100, 1004], maxlen=5) #extend starts from center to right
maxlengthfive.pop()
print(maxlengthfive) #print deque([4, 5, 7, 100], maxlen=5)
maxlengthfive.appendleft(0)
print(maxlengthfive) #print deque([0, 4, 5, 7, 100], maxlen=5)
maxlengthfive.extendleft([-1, -2, -3])
print(maxlengthfive) #print deque([-3, -2, -1, 0, 4], maxlen=5) #extendleft() starts from center to left
maxlengthfive.popleft()
print(maxlengthfive) #print deque([-2, -1, 0, 4], maxlen=5)
maxlengthfive.popleft()
maxlengthfive.popleft()
print(maxlengthfive) #print deque([0, 4], maxlen=5)
#If the maxlen value is not set, the deque does not perform any trimming operations to maintain the size of the deque.
anylengthfive = deque([1, 2, 3, 4, 5])
anylengthfive.appendleft(0)
print(anylengthfive) #print deque([0, 1, 2, 3, 4, 5])
anylengthfive.extendleft([-1, -2, -3])
print(anylengthfive) #print deque([-3, -2, -1, 0, 1, 2, 3, 4, 5])

from collections import namedtuple
#namedtuple is like dictionaries except it's immutable or can't reassign an item or can't reassign a value.  Namedtuple makes your tuples self-document. You are not bound to use integer indexes to access members of a tuple.  It makes it more easy to maintain your code.  It allows you to give names to each position making the code more readable and self-documenting. Also with a namedtuple you can access the positions by name as well as index.  User defines name for elements.
animal = namedtuple("animal","name age type")
winnie = animal(name="Winnie", age=4, type="bear")
geoffrey = animal(name="Geoffrey", age=50, type="giraffe")
snoopy = animal(name="Snoopy", age=30, type="dog")
justvalues = animal("Dumbo", 55, "elephant")
print(animal) #print <class '__main__.animal'>
print(winnie) #print animal(name='Winnie', age=4, type='bear')
print(geoffrey) #print animal(name='Geoffrey', age=50, type='giraffe')
print(snoopy.name) #print Snoopy
print(snoopy.type) #print dog
print(snoopy[0]) #print Snoopy.  Can use integer index reference.
print("Animal name "+snoopy[0]) #print Animal name Snoopy
print("Animal name "+snoopy.name) #print Animal name Snoopy
print(snoopy._asdict()) #print OrderedDict([('name', 'Snoopy'), ('age', 30), ('type', 'dog')]) #convert to dictionary
print(justvalues) #print animal(name='Dumbo', age=55, type='elephant')
snoopydictionary = snoopy._asdict()
print(snoopydictionary) #print OrderedDict([('name', 'Snoopy'), ('age', 30), ('type', 'dog')]) #convert to dictionary
print(snoopydictionary["name"]) #print Snoopy
for key, value in snoopydictionary.items():
	print(key, value) #print name Snoopy\n age 30\n type dog
kittylist = ["Garfield",50,"cat"] #convert a list into a namedtuple animal
kittylist = animal._make(kittylist)
print(kittylist) #print animal(name='Garfield', age=50, type='cat')
birdtuple = ("Woody",198,"woodpecker") #convert a tuple into a namedtuple animal
birdtuple = animal._make(birdtuple)
print(birdtuple) #print animal(name='Woody', age=198, type='woodpecker')
print(animal._fields) #print ('name', 'age', 'type')
#namedtuple will be very handy while processing a CSV data file, where we can access the data using names instead of indexes, which make the code more meaningful and efficient.

