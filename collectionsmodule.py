#http://book.pythontips.com/en/latest/collections.html

from collections import defaultdict
colors = (("yellow","banana"), ("blue","sky"),("green","trees"),("white","walls"),("black","shirt"),("red","fire engine"))
print(colors) #print (('yellow', 'banana'), ('blue', 'sky'), ('green', 'trees'), ('white', 'walls'), ('black', 'shirt'), ('red', 'fire engine'))
#favoritecolors = defaultdict(colors)
#print(favoritecolors)

from collections import OrderedDict
#OrderedDict keeps its entries sorted as they are ini
stocks = {"GOOG": 520.54, "FB": 76.45, "YHOO": 39.28, "AMZN": 305.21, "AAPL": 99.76}
for key, value in stocks.items():
	print(key, value) #RM:  no OrderedDict required.  Prints in order GOOG, FB, YHOO, AMZN, AAPL
stocksordereddict = OrderedDict({"GOOG": 520.54, "FB": 76.45, "YHOO": 39.28, "AMZN": 305.21, "AAPL": 99.76})
for key, value in stocksordereddict.items():
	print(key, value)

from collections import Counter
#Counter allows us to count the occurrences of a particular item.
colors = (("yellow","banana"), ("blue","sky"),("green","trees"),("white","walls"),("black","shirt"),("red","fire engine"),("white","heaven"))
numberlistofwords = Counter(whatever for whatever, colors in colors) #RM:  it appears the for and the in are key words, in is the source
print(numberlistofwords) #print Counter({'white': 2, 'yellow': 1, 'blue': 1, 'green': 1, 'black': 1, 'red': 1})
#continue 12.4 deque