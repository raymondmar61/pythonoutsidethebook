#Socratica Video 22 List Comprehension
#list comprehension [expression for variable in collection if test1 and test2]  
#list comprehension [expression for variable1 in collection1 and variable2 in collection2]
squares = []
for i in range(1, 11):
	squares.append(i**2)
print(squares) #print [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares2 = [i**2 for i in range(1,11)]
print(squares2) #print [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story" "Gone With The Wind", "Citizen Kane", "It's A Wonderful Life", "The Wizard Of Oz", "Gattaca", "Rear Window", "Ghostbusters", "To Kill A Mockingbird", "Good Will Hunting", "2001: A Space Odyssey", "Raiders Of The Lost Ark", 
"Groundhog Day", "Close Encounters Of The Third Kind"]
gmovies = []
for title in movies:
	if title.startswith("G"):
		gmovies.append(title)
print(gmovies) #print ['Gandhi', 'Gattaca', 'Ghostbusters', 'Good Will Hunting', 'Groundhog Day']
gmovies2 = [title for title in movies if title.startswith("G")]
print(gmovies2) #print ['Gandhi', 'Gattaca', 'Ghostbusters', 'Good Will Hunting', 'Groundhog Day']

movies2 = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's A Wonderful Life", 1946), ("Gattaca", 1997), ("No Country For Old Men", 2007), ("Rear Window", 1954), ("The Lord Of The Rings:  The Fellowship Of The Ring", 2001), ("Groundhog Day", 1993), ("Close Encounters Of The Third Kind", 1977), 
("The Royal Tenenbaums", 2001), ("The Aviator", 2004), ("Raiders Of The Lost Ark", 1981)]
movies2001 = []
for key, value in movies2:
	if value > 2000:
		movies2001.append(key)
print(movies2001) #print ['Spirited Away', 'No Country For Old Men', 'The Lord Of The Rings:  The Fellowship Of The Ring', 'The Royal Tenenbaums', 'The Aviator']
movies20012 = [title for (title, year) in movies2 if year > 2000]
print(movies20012) #print ['Spirited Away', 'No Country For Old Men', 'The Lord Of The Rings:  The Fellowship Of The Ring', 'The Royal Tenenbaums', 'The Aviator']

vectorlist = [2, -3, 1]
print(4*vectorlist) #print [2, -3, 1, 2, -3, 1, 2, -3, 1, 2, -3, 1] or vectorlist+vectorlist+vectorlist+vectorlist.  Adding lists concatenates them.
wvectorlist = [4*x for x in vectorlist]
print(wvectorlist) #print [8, -12, 4]

#Cartesian product a={1,3} b={x,y} a*b={(1,x), (1,y), (3,x), (3,y)}
oddlist = [1, 3, 5, 7]
evenlist = [2, 4, 6, 8]
cartesianproduct = [(a,b) for a in oddlist for b in evenlist]
print(cartesianproduct) #print [(1, 2), (1, 4), (1, 6), (1, 8), (3, 2), (3, 4), (3, 6), (3, 8), (5, 2), (5, 4), (5, 6), (5, 8), (7, 2), (7, 4), (7, 6), (7, 8)]
cartesianproductproduct = [a*b for a in oddlist for b in evenlist]
print(cartesianproductproduct) #print [2, 4, 6, 8, 6, 12, 18, 24, 10, 20, 30, 40, 14, 28, 42, 56]
print(max(cartesianproductproduct)) #print 56

list1 = [1]
list2 = [2, 3]
list3 = [4, 5, 6]
list123 = [a*b*c for a in list1 for b in list2 for c in list3]
print(list123) #print [8, 10, 12, 12, 15, 18]
listall = [[1], [2, 3], [4, 5, 6]]
listallproduct = [a for a in listall]
print(listallproduct) #print [[1], [2, 3], [4, 5, 6]]

#RM 018maximumpathsumi.py Project Euler
# lista = [3]
# listb = [7, 4]
# listc = [2, 4, 6]
# listd = [8, 5, 9, 3]
# listabcd = [print(a, b, c, d) for a in lista for b in listb for c in listc for d in listd if a+b+c+d==23] #print 3 7 6 9 which is incorrect.  Want 3 7 4 9

#https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
#result = [transform for iteration if filter]
result = [evennumber for evennumber in range(0,6) if evennumber % 2 == 0]
print(result) #print [0, 2, 4]
x = [i for i in range(0,11)]
print(x) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listofwords = ["this","is","a","list","of","words"]
firstletters = [eachlistofwords[0] for eachlistofwords in listofwords]
print(firstletters) #print ['t', 'i', 'a', 'l', 'o', 'w']
print(x.upper() for x in ["a","b","c"]) #print <generator object <genexpr> at 0x7facced5c360>
print([x.upper() for x in ["a","b","c"]]) #print ["A","B","C"]
extractnumbersinstring = "Hello 12345 World"
numbersasstring = [x for x in extractnumbersinstring if x.isdigit()]
print(numbersasstring) #print ['1', '2', '3', '4', '5']
stringasstring = [x for x in extractnumbersinstring if x.isalpha()]
print(stringasstring) #print ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
def double(x):
	return x*2
print([double(x) for x in range(0,11)]) #print [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print([double(x) for x in range(0,11) if x % 2 == 0]) #print [0, 4, 8, 12, 16, 20]

#https://hackernoon.com/list-comprehension-in-python-8895a785550b
lista = [1, 2, 3, 4]
listb = [2, 3, 4, 5]
matchnumbers = [a for a in lista for b in listb if a == b]
print(matchnumbers) #print [2, 3, 4]

#https://docs.python.org/3.5/tutorial/datastructures.html
listx = [1, 2, 3]
listy = [3, 1, 4]
xandytuple = [(x,y) for x in listx for y in listy if x!= y]
print(xandytuple) #print [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
#long way
xandytuple = []
for x in listx:
	for y in listy:
		if x != y:
			xandytuple.append((x,y))
print(xandytuple) #print [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
vector = [-4, -2, 0, 2, 4]
absolutevector = [abs(eachvector) for eachvector in vector]
print(absolutevector) #print [4, 2, 0, 2, 4]
from math import pi
pinumbers = [str(round(pi, i)) for i in range(1,7)]
print(pinumbers) #print ['3.1', '3.14', '3.142', '3.1416', '3.14159', '3.141593']

#continue 5.1.4 Nested List Comprehensions 07/17/18
a1 = [[3, 0, 0], [7, 4, 0], [2, 4, 6]]
transpose = [[row[i] for row in a1] for i in range(0,3)]
print(transpose) #print [[3, 7, 2], [0, 4, 4], [0, 0, 6]]
transpose = [[row[i] for row in a1 for i in range(0,3)]]
print(transpose) #print [[3, 0, 0, 7, 4, 0, 2, 4, 6]]

#3x4 matrix 3 lists length 4
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
onelist = []
for i in range(0,3):
	for j in range(0,3):		
		print(matrix[i][j]) #print 1\n 2\n 3\n 5\n 6\n 7\n \n 10\n 11
		onelist.append(matrix[i][j])
print(onelist) #print [1, 2, 3, 5, 6, 7, 9, 10, 11]
print([row[i] for row in matrix for i in range(0,3)]) #print [1, 2, 3, 5, 6, 7, 9, 10, 11]
#3x4 matrix 3 lists length 4
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
onelist = []
for i in range(0,3):
	for j in range(0,4):		
		print(matrix[i][j]) #print 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10\n 11\n 12
		onelist.append(matrix[i][j])
print(onelist) #print [1, 2, 3, 5, 6, 7, 9, 10, 11, 12]
print([row[i] for row in matrix for i in range(0,4)]) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#3x4 matrix 3 lists length 4
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposed = []
for i in range(0,3):
	transposedrow = []
	for eachlist in matrix:
		print(eachlist[i]) #print 1\n 5\n 9\n 2\n 6\n 10\n 3\n 7\n 11
		transposedrow.append(eachlist[i])
	transposed.append(transposedrow)
print(transposed) #print [[1, 5, 9], [2, 6, 10], [3, 7, 11]]
print([[row[i] for row in matrix] for i in range(0,3)]) #print [[1, 5, 9], [2, 6, 10], [3, 7, 11]]
#3x4 matrix 3 lists length 4
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposed = []
for i in range(0,4):
	transposedrow = []
	for eachlist in matrix:
		print(eachlist[i]) #print 1\n 5\n 9\n 2\n 6\n 10\n 3\n 7\n 11\n 4\n 8
		transposedrow.append(eachlist[i])
	transposed.append(transposedrow)
print(transposed) #print [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print([[row[i] for row in matrix] for i in range(0,4)]) #print [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

#zip() function creates a list of tuples
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(list(zip(*matrix))) #print [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
print(zip(*matrix)) #print <zip object at 0x7ff55d585f88>

letterhundreds = [("a",232), ("b",343), ("c", 543), ("d",23)]
print(letterhundreds) #print [('a', 232), ('b', 343), ('c', 543), ('d', 23)]
pivotletterhundreds = list(zip(*letterhundreds))
print(pivotletterhundreds) #print [('a', 'b', 'c', 'd'), (232, 343, 543, 23)]
print(pivotletterhundreds[0]) #print ('a', 'b', 'c', 'd')
print(list(pivotletterhundreds[0])) #print ['a', 'b', 'c', 'd']

#Python Implementing _zip_ with list comprehensions — Reuven Lerner.pdf https://lerner.co.il/2016/08/30/implementing-zip-list-comprehensions/
#Python 2’s “zip” returns a list, but Python 3’s “zip” returns an iterator object or <zip object at . . . >
#Use zip for string and tuples
sletters = "abcde"
tnumbers = (1, 2, 3, 4, 5)
tnumbersoneless = (1, 2, 3, 4)
umore = ("jack","sack","tack","back","pack")
print(zip(sletters, tnumbers)) #print <zip object at 0x7f66c7048b08>
print(list(zip(sletters, tnumbers))) #print [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
print(list(zip(sletters, tnumbersoneless))) #print [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print(list(zip(sletters, tnumbers, umore))) #print [('a', 1, 'jack'), ('b', 2, 'sack'), ('c', 3, 'tack'), ('d', 4, 'back'), ('e', 5, 'pack')]
#Lists to dictionaries
names = ["Tom", "Dick", "Harry"]
ages = [50, 35, 60]
print(dict(zip(names, ages))) #print {'Tom': 50, 'Dick': 35, 'Harry': 60}
from itertools import repeat
def zip_longest(*args, fillvalue="put fillvalue here"):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue) #repeat() function is from the itertools module
                value = fillvalue
            values.append(value)
        yield tuple(values)
print(zip_longest(sletters, tnumbersoneless)) #print <generator object zip_longest at 0x7fe1faac9a98>
print(zip(zip_longest(sletters, tnumbersoneless))) #print <zip object at 0x7f6a2b8e64c8>
print(list(zip_longest(sletters, tnumbersoneless))) #print [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 'put fillvalue here')]
#Zip in list comprehension
sletterstnumbers = [(sletters[i], tnumbers[i]) for i in range(0,len(sletters))]
print(sletterstnumbers) #print [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
#Author wanted to create a function to clean things up
def shortest_sequence_range(*args):
	return range(len(sorted(args, key=len)[0]))
print([(sletters[i], tnumbers[i]) for i in shortest_sequence_range(sletters, tnumbers)]) #print [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]