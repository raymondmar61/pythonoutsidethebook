#http://book.pythontips.com/en/latest/collections.html

from collections import defaultdict
colors = (("yellow","banana"), ("red","apple"),("blue","sky"),("green","trees"),("white","walls"),("black","shirt"),("red","fire engine"))
print(colors) #print (('yellow', 'banana'), ('red', 'apple'), ('blue', 'sky'), ('green', 'trees'), ('white', 'walls'), ('black', 'shirt'), ('red', 'fire engine'))
# favoritecolors = defaultdict(colors)
# print(favoritecolors) #TypeError: first argument must be callable or None
favoritecolors = defaultdict(list)
for name, colors in colors:
	favoritecolors[name].append(colors)
print(favoritecolors) #print defaultdict(<class 'list'>, {'yellow': ['banana'], 'red': ['apple', 'fire engine'], 'blue': ['sky'], 'green': ['trees'], 'white': ['walls'], 'black': ['shirt']})
print(favoritecolors["red"]) #print ['apple', 'fire engine']
print(favoritecolors["white"]) #print ['walls']
print(favoritecolors["sky"]) #print []

from collections import OrderedDict
#OrderedDict keeps its entries sorted as they are iniitially inserted
stocks = {"GOOG": 520.54, "FB": 76.45, "YHOO": 39.28, "AMZN": 305.21, "AAPL": 99.76}
for key, value in stocks.items():
	print(key, value) #RM:  no OrderedDict required.  Prints in order GOOG, FB, YHOO, AMZN, AAPL
stocksordereddict = OrderedDict({"GOOG": 520.54, "FB": 76.45, "YHOO": 39.28, "AMZN": 305.21, "AAPL": 99.76})
for key, value in stocksordereddict.items():
	print(key, value) #prints Prints in order GOOG, FB, YHOO, AMZN, AAPL

from collections import Counter
#Counter allows us to count the occurrences of a particular item.
colors = (("yellow","banana"), ("blue","sky"),("green","trees"),("white","walls"),("black","shirt"),("red","fire engine"),("white","heaven"))
numberlistofwords = Counter(whatever for whatever, colors in colors) #RM:  it appears the for and the in are key words, in is the source
print(numberlistofwords) #print Counter({'white': 2, 'yellow': 1, 'blue': 1, 'green': 1, 'black': 1, 'red': 1})

from collections import deque
#deque provides you with a double ended queue which means that you can append and delete elements from either side of the queue.
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
d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d) #print deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
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

from collections import namedtuple
#namedtuple is like dictionaries except it's immutable or can't reassign an item or can't reassign a value.  Namedtuple makes your tuples self-document. You are not bound to use integer indexes to access members of a tuple.  It makes it more easy to maintain your code.
animal = namedtuple("animal","name age type")
winnie = animal(name="Winnie", age=4, type="bear")
geoffrey = animal(name="Geoffrey", age=50, type="giraffe")
snoopy = animal(name="Snoopy", age=30, type="dog")
print(animal) #print <class '__main__.animal'>
print(winnie) #print animal(name='Winnie', age=4, type='bear')
print(geoffrey) #print animal(name='Geoffrey', age=50, type='giraffe')
print(snoopy.name) #print Snoopy
print(snoopy.type) #print dog
print(snoopy[0]) #print Snoopy.  Can use integer index reference.
print(snoopy._asdict()) #print OrderedDict([('name', 'Snoopy'), ('age', 30), ('type', 'dog')]) #convert to dictionary
snoopydictionary = snoopy._asdict()
print(snoopydictionary) #print OrderedDict([('name', 'Snoopy'), ('age', 30), ('type', 'dog')]) #convert to dictionary
print(snoopydictionary["name"]) #print Snoopy
for key, value in snoopydictionary.items():
	print(key, value) #print name Snoopy\n age 30\n type dog




