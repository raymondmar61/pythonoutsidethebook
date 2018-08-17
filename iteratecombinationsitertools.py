#https://docs.python.org/3.5/library/itertools.html, https://stackoverflow.com/questions/41680388/how-do-i-iterate-through-combinations-of-a-list, https://stackoverflow.com/questions/16384109/iterate-over-all-combinations-of-values-in-multiple-lists-in-python
#RM:  there are more functions in itertools.  I selected the product(), combinations(), permutations(), chain(), chain.from_iterable().  08/02/18:  there are more itertools below the selected functions.

#product creates a cartesian products from a series of iterables
import itertools
firstlist = [1,5,8]
secondlist = [0.5, 4]
print(list(itertools.product(firstlist, secondlist))) #print [(1, 0.5), (1, 4), (5, 0.5), (5, 4), (8, 0.5), (8, 4)]
print(list(itertools.product(firstlist, secondlist))) #print [(1, 0.5), (1, 4), (5, 0.5), (5, 4), (8, 0.5), (8, 4)]

#combinations sorts lexicographicaly
list1234 = [1, 2, 3, 4]
for combopairs in itertools.combinations(list1234, 2):
	print(combopairs) #print (1, 2)\n (1, 3)\n (1, 4)\n (2, 3)\n (2, 4)\n (3, 4)
for combotriplets in itertools.combinations(list1234, 3):
	print(combotriplets) #print (1, 2, 3)\n (1, 2, 4)\n (1, 3, 4)\n (2, 3, 4)
for combopairs in itertools.combinations(list1234, 2):
	print(sum(combopairs)) #print 3\n 4\n 5\n 5\n 6\n 7
list12345 = [1, 2, 3, 4, 5]
for comboquads in itertools.combinations(list12345, 4):
	print(comboquads) #print (1, 2, 3, 4)\n (1, 2, 3, 5)\n (1, 2, 4, 5)\n (1, 3, 4, 5)\n (2, 3, 4, 5)\n
#combinations_with_replacement elements repeat
for comboquads in itertools.combinations_with_replacement(list12345, 4):
	print(comboquads) #print (1, 1, 1, 1)\n (1, 1, 1, 2)\n (1, 1, 1, 3)\n (1, 1, 1, 4)\n . . . (1, 1, 2, 2) . . . .
list1234 = [1, 2, 3, 4]
for productpairs in itertools.permutations(list1234, 2):
	print(productpairs,end=";") #print (1, 2);(1, 3);(1, 4);(2, 1);(2, 3);(2, 4);(3, 1);(3, 2);(3, 4);(4, 1);(4, 2);(4, 3);  RM:  prints 1,2 and 2,1
#product creates a cartesian products from a series of iterables
list1234 = [1, 2, 3, 4]
for productpairs in itertools.product(list1234, repeat=2):
	print(productpairs,end=",") #print (1, 1),(1, 2),(1, 3),(1, 4),(2, 1),(2, 2),(2, 3),(2, 4),(3, 1),(3, 2),(3, 3),(3, 4),(4, 1),(4, 2),(4, 3),(4, 4),  RM: prints all combinations such as 1,1; 1,2; 2,1
print("\n")

#product creates a cartesian products from a series of iterables  product(*iterables, repeat=1)
firstlist = [1,5,8]
secondlist = [0.5, 4]
thirdlist = [10,11,12]
print(list(itertools.product(firstlist, secondlist, thirdlist))) #print [(1, 0.5, 10), (1, 0.5, 11), (1, 0.5, 12), (1, 4, 10), (1, 4, 11), (1, 4, 12), (5, 0.5, 10), (5, 0.5, 11), (5, 0.5, 12), (5, 4, 10), (5, 4, 11), (5, 4, 12), (8, 0.5, 10), (8, 0.5, 11), (8, 0.5, 12), (8, 4, 10), (8, 4, 11), (8, 4, 12)]
print(list(itertools.product(firstlist, secondlist, thirdlist, repeat=3)))
threelist = list(itertools.product(firstlist, secondlist, thirdlist))
print(threelist)
for eachthreelist in threelist:
	print(sum(eachthreelist)) #print the sum for eachthreelist entry; e.g. (8,4,12) print 24
listone = [3]
listtwo = [7, 4]
listthree = [2, 4, 6]
listfour = [8, 5, 9, 3]
fourlist = list(itertools.product(listone, listtwo, listthree, listfour))
maxsum = 0
for eachfourlist in fourlist:
	#print(sum(eachfourlist))
	if sum(eachfourlist) > maxsum:
		maxsum = sum(eachfourlist)
print(maxsum) #print 25

print(itertools.chain("ABC","DEF")) #print <itertools.chain object at 0x7f0169a21198>
love = itertools.chain("ABC","DEF")
print("".join(map(str, love))) #print ABCDEF
love = itertools.chain("ABC","DEF")
print(list(map(str,love))) #print ['A', 'B', 'C', 'D', 'E', 'F']
love = itertools.chain("ABC","DEF")
print(" ".join(map(str, love))) #print A B C D E F

print(itertools.chain.from_iterable(["ABC","DEF"])) #print <itertools.chain object at 0x7f0d500351d0>
listlove = itertools.chain.from_iterable(["ABC","DEF"])
print("".join(map(str, listlove))) #print ABCDEF
listlove = itertools.chain.from_iterable(["ABC","DEF"])
print(list(map(str,listlove))) #print ['A', 'B', 'C', 'D', 'E', 'F']
listlove = itertools.chain.from_iterable(["ABC","DEF"])
print(" ".join(map(str, listlove))) #print A B C D E F

from itertools import combinations
p = {int((num * ((3 * num) - 1)) / 2) for num in range(1, 10)}
for x, y in combinations(p, 2):
	diff = abs(x - y)
	print(x,y,diff) #print 35 70 35\n 5 70 65\n 22 92 70\n examples
	_sum = x + y
	if diff in p and _sum in p:
		print(diff, _sum, x, y) #print 

#38. Write a Python program to change the position of every n-th value with the (n+1)th in a list. Sample list: [0,1,2,3,4,5].  Expected Output: [1, 0, 3, 2, 5, 4].  RM:  copied solution.  New functions from a module.
from itertools import zip_longest, chain, tee
def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0,1,2,3,4,5]
print(replace2copy(n)) #print [1, 0, 3, 2, 5, 4]

#https://www.blog.pythonlibrary.org/2016/04/20/python-201-an-intro-to-itertools/
#https://medium.com/@jasonrigden/a-guide-to-python-itertools-82e5a306cdf8
#https://realpython.com/python-itertools/
#The count iterator will return evenly spaced values starting with the number you pass in as its start parameter. Count also accept a step parameter.  count(start=0,step=1).  RM:  =number is default
from itertools import count
for i in count(10):
	if i > 12:
		break
	else:
		print(i) #print 10\n 11\n 12\n
for i in count(10,2):
	if i > 21:
		break
	else:
		print(i) #print 10\n 12\n 14\n 16\n 18\n 20\n
#Limit the output using islice.  islice(loop,end loop number of items iterated).
from itertools import count, islice
for i in islice(count(10),3):
	print(i) #print 10\n 11\n 12\n
for i in islice(count(10,2),6):
	print(i) #print 10\n 12\n 14\n 16\n 18\n 20\n

#The cycle iterator create an iterator that will cycle through a series of values infinitely.  cycle(iterable)
from itertools import cycle
count = 0
for eachletter in cycle("xyz"):
	if count > 7:
		break
	else:
		print(eachletter) #print x\n y\n z\n x\n y\n z\n x\n y\n
	count += 1
colors = ["red","orange","yellow","green","blue"]
stopper = len(colors)
counter = 0
for eachcolors in cycle(colors):
	#RM:  counter must be included to stop cycle making for loop infinite.  Obviously no need for cycle because for eachcolors in colors: iterates colors list once.
	if counter == stopper:
		break
	print(eachcolors)	
	counter += 1
shapes = ["triangle","square","pentagon","rectangle"]
iterator = cycle(shapes)
print(next(iterator)) #print triangle
print(next(iterator)) #print square
print(next(iterator)) #print pentagon
print(next(iterator)) #print rectangle
print(next(iterator)) #print square
print(next(iterator)) #print triangle

#The repeat iterators will return an object an object over and over again forever unless you set its times argument.  repeat(object[,times])  RM:  brackets means optional
from itertools import repeat
iterator = repeat(5,5)
print(next(iterator)) #print 5
print(next(iterator)) #print 5
print(next(iterator)) #print 5
print(next(iterator)) #print 5
print(next(iterator)) #print 5
print(next(iterator)) #error message StopIteration
from itertools import repeat
for i in repeat("spam",4):
	print(i) #print spam\n spam\n spam\n spam
print(repeat(1,5)) #print repeat(1,5)
repeatonefive = repeat(1,5)
print(repeatonefive) #print repeat(1,5)
for i in repeat(1,5):
	print(i) #print 1\n 1\n 1\n 1\n 1
for i in repeatonefive:
	print(i) #print 1\n 1\n 1\n 1\n 1

#The accumulate iterator will return accumulated sums or the accumulated results of a two argument function.  accumulate(iterable[,func]).  Default is sum or operator.add.
from itertools import accumulate
#addfromindexnumbers = [x ]
print(list(accumulate(range(0,10)))) #[0, 1, 3, 6, 10, 15, 21, 28, 36, 45]  RM:  adds the numbers from index position starting at 0 accumulating the sum.  0+0, 0+1, 1+2, 3+3, 6+4, 10+5, 15+6 . . . .  Default is sum.
import operator
print(list(accumulate(range(1,5), operator.mul))) #[1, 2, 6, 24] #operator.mul multiplies the numbers from index position.  Instructors says look at accumulate documentation.
data = [789, 10, 25, 54, 99]
result = accumulate(data,operator.mul)
print(list(result)) #print [789, 7890, 157800, 7890000, 781110000] or [789, 789*10, 789*10*25, 789*10*25*54, 789*10*25*54*99]
data = [1, 2, 3, 4, 5]
result = accumulate(data,operator.mul)
for eachresult in result:
	print(eachresult) #print 1\n 2\n 6\n 24\n 120\n
data = [5, 2, 6, 4, 5, 9, 1]
result = accumulate(data,max)
for eachresult in result:
	print(eachresult) #print 5\n 5\n 6\n 6\n 6\n 9\n 6\n
data = [5, 2, 6, 4, 5, 9, 1]
for eachresult in accumulate(data,min):
	print(eachresult) #print 5\n 2\n 2\n 2\n 2\n 2\n 1\n

#The chain iterator will take a series of iterables and basically flatten them down into one long iterable. chain(*iterables)  RM:  * means multiple objects
from itertools import chain
list1 = ["foo","bar"]
list2 = list(range(0,5))
list3 = ["ls","/some/dir"]
print(list1+list2+list3) #print ['foo', 'bar', 0, 1, 2, 3, 4, 'ls', '/some/dir']
print(chain(list1,list2,list3)) #print <itertools.chain object at 0x7f947c64df98>
list123 = chain(list1,list2,list3)
print(list123) #print <itertools.chain object at 0x7f367dd71780>
listlist123 = list(chain(list1,list2,list3))
print(listlist123) #print ['foo', 'bar', 0, 1, 2, 3, 4, 'ls', '/some/dir']
#You can also use a method of chain called from_iterable.  Pass in a nested list.  chain.from_iterable(iterable).
from itertools import chain
list1 = ["foo","bar"]
list2 = list(range(0,5))
list3 = ["ls","/some/dir"]
print(chain.from_iterable([list1,list2,list3])) #print <itertools.chain object at 0x7f8dcd5f4f98>
passnestedlist = chain.from_iterable([list1,list2,list3])
print(passnestedlist) #print <itertools.chain object at 0x7f72c0a21f60>
passnestedlistlist = list(chain.from_iterable([list1,list2,list3]))
print(passnestedlistlist) #print ['foo', 'bar', 0, 1, 2, 3, 4, 'ls', '/some/dir']

#The compress sub-module is useful for filtering the first iterable with the second. This works by making the second iterable a list of Booleans (or ones and zeroes which amounts to the same thing).  Filters one iterable with another.  compress(data, selectors)
from itertools import compress
letters1 = "abcdefg"
letters2 = "abcdefg"
letters3 = "afg"
truefalse = [True, False, True, True, False]
oneszeroes = [1, 0, 1, 1, 0]
print(list(compress(letters1,letters2))) #print ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(list(compress(letters1,letters3))) #print ['a', 'b', 'c']
print(list(compress(letters1,truefalse))) #print ['a', 'c', 'd'] #second list truefalse is Booleans
print(list(compress(letters1,oneszeroes))) #print ['a', 'c', 'd'] #second list oneszeroes is ones and zeroes

#Dropwhile will drop elements as long as the filter criteria is True. Because of this, you will not see any output from this iterator until the predicate becomes False. This can make the start-up time lengthy.  dropwhile(predicate, iterable).  RM:  I believe dropwhile drops all elements when True.  When False, dropwhile returns the rest of the elements.  Makes iterator drops elements from iterable as long as the predicate is true; otherwise, returns every rest of elements.
from itertools import dropwhile
def greaterthanfive(x):
	return x>5
print(list(dropwhile(greaterthanfive,[6, 7, 8, 9, 1, 2, 3, 10]))) #print [1, 2, 3, 10]

#The filterfalse function from itertools is very similar to dropwhile. However instead of dropping values that match True, filterfalse will only return those values that evaluated to False.  filterfalse(predicate,iterable)
from itertools import filterfalse
def greaterthanfive(x):
	return x>5
print(list(filterfalse(greaterthanfive,[6, 7, 8, 9, 1, 2, 3, 10]))) #print [1, 2, 3]

#The groupby iterator will return consecutive keys and groups from your iterable.  Groups things together.  groupby(iterable, key=None).  RM:  =None is default
from itertools import groupby
vehicles = [('Ford', 'Taurus'), ('Dodge', 'Durango'), ('Chevrolet', 'Cobalt'), ('Ford', 'F150'), ('Dodge', 'Charger'), ('Ford', 'GT')]
sortvehicles = sorted(vehicles)
for key, group in groupby(sortvehicles,lambda make: make[0]):
	print(key, group) #print Dodge <itertools._grouper object at 0x7fb77439a160>
	for make, rightsidetuple in group:
		print(make, rightsidetuple) #print Dodge Charger\n Dodge Durango

#islice is an iterator that returns selected elements from the iterable. islice take a slice by index of your iterable (the thing you iterate over) and returns the selected items as an iterator.  Allows you to cut out a piece of an iterable.  There are actually two implementations of islice. There’s itertools.islice(iterable, stop) and then there’s the version of islice that more closely matches regular Python slicing: islice(iterable, start, stop[, step]).
from itertools import islice, count
for i in islice(count(),3, 15):
	print(i) #print 3\n 4\n 5\n . . . 12\n 13\n 14
for i in islice(count(),3, 15,3):
	print(i) #print 3\n 6\n 9\n 12
n=45
for i in islice(count(),n,70,5):
	print(i) #print 45\n 50\n 55\n 60\n 65
colors = ["red","orange","yellow","green","blue"]
number = 3
fewercolors = islice(colors,number)
for eachfewercolors in fewercolors:
	print(eachfewercolors) #print red\n orange\n yellow

counter = count()
print(list(next(counter) for x in range(0, 5))) #print [0, 1, 2, 3, 4]
evens = count(step=2)
print(list(next(evens) for x in range(0, 5))) #print [0, 2, 4, 6, 8]
odds = count(start=1, step=2)
print(list(next(odds) for x in range(0, 5))) #print [1, 3, 5, 7, 9]
floats = count(start=.5, step=.75)
print(list(next(floats) for x in range(0, 5))) #print [0.5, 1.25, 2.0, 2.75, 3.5]
negatives = count(start=-1, step=-.5)
print(list(next(negatives) for x in range(0, 5))) #print [-1, -1.5, -2.0, -2.5, -3.0]
print(list(zip(count(),["a","b","c"]))) #print[(0, 'a'), (1, 'b'), (2, 'c')]
print(list(zip(count(start=1),["a","b","c"]))) #print[(1, 'a'), (2, 'b'), (3, 'c')]
ten = count(start=10, step=3)
for x in range(10,21):
	print(next(ten)) #print 10\n 13\n 16\n 19\n 22\n 25\n 28\n 31\n 34\n 37\n 40

#The starmap tool will create an iterator that can compute using the function and iterable provided.  Makes an iterator that computes the function using arguments obtained from the iterable.  starmap(function, iterable).
from itertools import starmap
def add(a,b):
	return a+b
for x in starmap(add,[(2,3),(4,5)]):
	print(x) #print 5\n 9
from itertools import starmap
import operator
data = [(2,6),(8,4),(7,3)]
result = starmap(operator.mul, data)
for eachresult in result:
	print(eachresult) #print 12\n 32\n 21

#The takewhile module is basically the opposite of the dropwhile iterator that we looked at earlier. takewhile will create an iterator that returns elements from the iterable only as long as our predicate or filter is True.  Makes an iterator and returns elements from the iterable as long as the predicate is true.  takewhile(predicate, iterable).
from itertools import takewhile
def lessthanfive(x):
	return x<5
print(list(takewhile(lessthanfive,[1, 4, 2, 3, 6, 4, 1, 0]))) #print [1, 4, 2, 3]

#The tee tool will create *n* iterators from a single iterable. What this means is that you can create multiple iterators from one iterable.  Returns n independent iterators from a single iterable.  tee(iterable,n=2).
from itertools import tee
data = "abcde"
iter1, iter2, iter3 = tee(data,3)
for eachiter1 in iter1:
	print(eachiter1) #print a\n b\n c\n d\n e
for eachiter2 in iter2:
	print(eachiter2) #print a\n b\n c\n d\n e
for eachiter3 in iter3:
	print(eachiter3) #print a\n b\n c\n d\n e
#we use multiple assignment to acquire the three iterators that are returned from tee. Finally we loop over each of the iterators and print out their contents. The content are the same.
colors = ["red","orange","yellow","green","blue"]
alphacolors1, betacolors2 = tee(colors,2)
for eachalphacolors1 in alphacolors1:
	print(eachalphacolors1) #print red\n orange\n yellow\n green\n blue
for eachbetacolors2 in betacolors2:
	print(eachbetacolors2) #print red\n orange\n yellow\n green\n blue

#The **zip_longest** iterator can be used to zip two iterables together. If the iterables don’t happen to be the same length, then you can also pass in a **fillvalue**.  Makes an iterator that aggregates elements from each of the iterables.  If the iterables are of uneven length, missing values are filled-in with fillvalue.  Iteration stops when the longest iterable is exhausted.  zip_longest(*iterables, fillvalue=None).
from itertools import zip_longest
for item in zip_longest("abcd","xy",fillvalue="blank"):
	print(item) #print ('a', 'x')\n ('b', 'y')\n ('c', 'blank')\n ('d', 'blank')
for item in zip_longest("abcdefg","vwxy", "quick",fillvalue="blank"):
	print(item) #print ('a', 'v', 'q')\n ('b', 'w', 'u')\n ('c', 'x', 'i')\n ('d', 'y', 'c')\n ('e', 'blank', 'k')\n ('f', 'blank', 'blank')\n ('g', 'blank', 'blank')
colors = ["red","orange","yellow","green","blue"]
data = [1,2,3,4,5,6,7,8,9,10]
for eachcolorsdata in zip_longest(colors, data, fillvalue=None):
	print(eachcolorsdata) #print ('red', 1)\n ('orange', 2)\n ('yellow', 3)\n ('green', 4)\n ('blue', 5)\n \n (None, 6)\n (None, 7)\n (None, 8)\n (None, 9)\n (None, 10)
print(list(zip(colors,data))) #print [('red', 1), ('orange', 2), ('yellow', 3), ('green', 4), ('blue', 5)]

#The built-in zip() function, which takes any number of iterables as arguments and returns an iterator over tuples of their corresponding elements.  Lists are iterables which means they can return their elements one at a time.  zip() function aggregates the results into tuples.
print(list(zip([1, 2, 3],["a","b","c"]))) #print [(1, 'a'), (2, 'b'), (3, 'c')]
print(list(map(len,["abc","de","fghi"]))) #print [3, 2, 4]
from itertools import zip_longest
x = [1, 2, 3, 4, 5]
y = ["a","b","c"]
print(list(zip(x,y))) #print [(1, 'a'), (2, 'b'), (3, 'c')]
print(list(zip_longest(x,y))) #print [(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]

def grouper(inputlist, n, fillvalue=None):
	print(inputlist) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	iters = [iter(inputlist)] * n
	print(iter(inputlist)) #print <list_iterator object at 0x7fc62ddb5780>
	print(iters) #print [<list_iterator object at 0x7f3168c5b7f0>, <list_iterator object at 0x7f3168c5b7f0>, <list_iterator object at 0x7f3168c5b7f0>, <list_iterator object at 0x7f3168c5b7f0>]
	print(list(iters)) #print [<list_iterator object at 0x7fbcb4c897f0>, <list_iterator object at 0x7fbcb4c897f0>, <list_iterator object at 0x7fbcb4c897f0>, <list_iterator object at 0x7fbcb4c897f0>]
	print([iter(inputlist)] * n) #print [<list_iterator object at 0x7fb99c9e6748>, <list_iterator object at 0x7fb99c9e6748>, <list_iterator object at 0x7fb99c9e6748>, <list_iterator object at 0x7fb99c9e6748>]
	print((inputlist)*n) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	return zip_longest(*iters, fillvalue=fillvalue)
numberlist = [1,2,3,4,5,6,7,8,9,10]
#print(grouper(numberlist,4)) #print <itertools.zip_longest object at 0x7f422d6b9d18>
print(list(grouper(numberlist,4))) #print [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, None, None)]