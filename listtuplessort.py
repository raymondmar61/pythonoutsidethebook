#https://www.w3resource.com/python-exercises/tuple/
#23. Write a Python program to sort a tuple by its float element. Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')].  Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
sampledata = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
secondnumber = lambda sampledata: sampledata[1]
sampledata.sort(key=secondnumber, reverse=True)
print(sampledata) #print [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

#https://stackoverflow.com/questions/22876410/how-to-sort-a-list-of-tuples-by-their-first-element
things = [("vehicle", "speed boat"), ("animal", "duck"), ("plant", "cactus"), ("animal", "bear"), ("vehicle", "school bus")]
print(things) #print [('vehicle', 'speed boat'), ('animal', 'duck'), ('plant', 'cactus'), ('animal', 'bear'), ('vehicle', 'school bus')]
things.sort()
print(things) #print [('animal', 'bear'), ('animal', 'duck'), ('plant', 'cactus'), ('vehicle', 'school bus'), ('vehicle', 'speed boat')]
things.sort(key=lambda x: x[0])
print(things) #print [('animal', 'bear'), ('animal', 'duck'), ('plant', 'cactus'), ('vehicle', 'school bus'), ('vehicle', 'speed boat')]
things.sort(key=lambda x: x[1])
print(things) #print [('animal', 'bear'), ('plant', 'cactus'), ('animal', 'duck'), ('vehicle', 'school bus'), ('vehicle', 'speed boat')]
things.sort(key=lambda x: x[1], reverse=True)
print(things) #print [('vehicle', 'speed boat'), ('vehicle', 'school bus'), ('animal', 'duck'), ('plant', 'cactus'), ('animal', 'bear')]
#sort function pass each element in the list to the lambda function as key.  It uses the value it returns to compare two objects in the list.  data = [(1,3), (1, 2)].  Sort by second element or index 1.  First, it passes (1,3) which returns the element 3 which represents the tuple during comparison.  Likewise (1,2) which returns the element 2 which represents the tuple during comparison.

#https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
numbertuples = [(1, 2, 3), (1, 6, -4), (5000, 5, 57), (4, 5, 6), (1, 100, 500), (7, 8, 9), (0, 7, -5), (100, 212, 555), (45, 46, 47), (0, 6, -4), (1, 3, 5), (1, 2, 4), (-100, -200, 3), (3, 3, 5)]
print(numbertuples) #print [(1, 2, 3), (1, 6, -4), (5000, 5, 57), (4, 5, 6), (1, 100, 500), (7, 8, 9), (0, 7, -5), (100, 212, 555), (45, 46, 47), (0, 6, -4), (1, 3, 5), (1, 2, 4), (-100, -200, 3), (3, 3, 5)]
twosorts = lambda numbertuples: (numbertuples[2], numbertuples[0])
numbertuples.sort(key=twosorts)
print(numbertuples) #print [(0, 7, -5), (0, 6, -4), (1, 6, -4), (-100, -200, 3), (1, 2, 3), (1, 2, 4), (1, 3, 5), (3, 3, 5), (4, 5, 6), (7, 8, 9), (45, 46, 47), (5000, 5, 57), (1, 100, 500), (100, 212, 555)]
numbertuples.sort(key=lambda x: (x[2], x[0]), reverse=False)
print(numbertuples) #print [(0, 7, -5), (0, 6, -4), (1, 6, -4), (-100, -200, 3), (1, 2, 3), (1, 2, 4), (1, 3, 5), (3, 3, 5), (4, 5, 6), (7, 8, 9), (45, 46, 47), (5000, 5, 57), (1, 100, 500), (100, 212, 555)]

import operator
listoflists = [[12, 'tall', 'blue', 1], [2, 'short', 'red', 9], [4, 'tall', 'blue', 13]]
print(listoflists) #print [[12, 'tall', 'blue', 1], [2, 'short', 'red', 9], [4, 'tall', 'blue', 13]]
print(sorted(listoflists)) #print [[2, 'short', 'red', 9], [4, 'tall', 'blue', 13], [12, 'tall', 'blue', 1]]
listoflistsfirstsort = sorted(listoflists, key=operator.itemgetter(1))
print(listoflistsfirstsort) #print [[2, 'short', 'red', 9], [12, 'tall', 'blue', 1], [4, 'tall', 'blue', 13]]
listoflistssecondsort = sorted(listoflistsfirstsort, key=operator.itemgetter(0))
print(listoflistssecondsort) #print [[2, 'short', 'red', 9], [4, 'tall', 'blue', 13], [12, 'tall', 'blue', 1]]
listoflists = [[12, 'tall', 'blue', 1], [2, 'short', 'red', 9], [4, 'tall', 'blue', 13]]
print(listoflists) #print [[12, 'tall', 'blue', 1], [2, 'short', 'red', 9], [4, 'tall', 'blue', 13]]
listofliststwosorts = sorted(listoflists, key=lambda x: (x[1], x[0]))
print(listofliststwosorts) #print [[2, 'short', 'red', 9], [4, 'tall', 'blue', 13], [12, 'tall', 'blue', 1]]
listoflistsitemgetter = sorted(listoflists, key=operator.itemgetter(0,1))
print(listoflistsitemgetter) #print [[2, 'short', 'red', 9], [4, 'tall', 'blue', 13], [12, 'tall', 'blue', 1]]
listoflists.sort(key=operator.itemgetter(0,1))
print(listoflists) #print [[2, 'short', 'red', 9], [4, 'tall', 'blue', 13], [12, 'tall', 'blue', 1]]
listoflistsnegative = sorted(listoflists, key=lambda x: (x[1]*-1, x[0]))  #RM:  index 1 is string.  multiply negative one no effect
#listoflistsnegative = sorted(listoflists, key=lambda x: (-x[1], x[0]))  #RM:  index 1 is string.  -x is error message
print(listoflistsnegative) #print [[2, 'short', 'red', 9], [4, 'tall', 'blue', 13], [12, 'tall', 'blue', 1]]
print("\n")

#to reverse to only one attribute, you can sort twice: first by the secondary s = sorted(s, key = operator.itemgetter(2)) then by the primary s = sorted(s, key = operator.itemgetter(1), reverse=True) Not ideal, but works.
numbertuples = [(1, 2, 3), (1, 6, -4), (5000, 5, 57), (4, 5, 6), (1, 100, 500), (7, 8, 9), (0, 7, -5), (100, 212, 555), (45, 46, 47), (0, 6, -4), (1, 3, 5), (1, 2, 4), (-100, -200, 3), (3, 3, 5)]
print(numbertuples) #print [(1, 2, 3), (1, 6, -4), (5000, 5, 57), (4, 5, 6), (1, 100, 500), (7, 8, 9), (0, 7, -5), (100, 212, 555), (45, 46, 47), (0, 6, -4), (1, 3, 5), (1, 2, 4), (-100, -200, 3), (3, 3, 5)]
numbertupleszeroascending = sorted(numbertuples, key = lambda x: x[0], reverse=False)
print(numbertupleszeroascending) #print [(-100, -200, 3), (0, 7, -5), (0, 6, -4), (1, 2, 3), (1, 6, -4), (1, 100, 500), (1, 3, 5), (1, 2, 4), (3, 3, 5), (4, 5, 6), (7, 8, 9), (45, 46, 47), (100, 212, 555), (5000, 5, 57)]
numbertuplestwodescending = sorted(numbertupleszeroascending, key = lambda x: x[2], reverse=True)
print(numbertuplestwodescending) #print [(-100, -200, 3), (0, 7, -5), (0, 6, -4), (1, 2, 3), (1, 6, -4), (1, 100, 500), (1, 3, 5), (1, 2, 4), (3, 3, 5), (4, 5, 6), (7, 8, 9), (45, 46, 47), (100, 212, 555), (5000, 5, 57)]

#another option, if key is number, to make it reverse, you can multiple it by -1.  RM:  multiplying by -1 invalid for strings
numbertuples = [(1, 2, 3), (1, 6, -4), (5000, 5, 57), (4, 5, 6), (1, 100, 500), (7, 8, 9), (0, 7, -5), (100, 212, 555), (45, 46, 47), (0, 6, -4), (1, 3, 5), (1, 2, 4), (-100, -200, 3), (3, 3, 5)]
print(numbertuples) #print [(1, 2, 3), (1, 6, -4), (5000, 5, 57), (4, 5, 6), (1, 100, 500), (7, 8, 9), (0, 7, -5), (100, 212, 555), (45, 46, 47), (0, 6, -4), (1, 3, 5), (1, 2, 4), (-100, -200, 3), (3, 3, 5)]
twosortspositiveone = lambda numbertuples: (numbertuples[2], numbertuples[0]*1)
numbertuples.sort(key=twosortspositiveone)
print(numbertuples) #print [(0, 7, -5), (0, 6, -4), (1, 6, -4), (-100, -200, 3), (1, 2, 3), (1, 2, 4), (1, 3, 5), (3, 3, 5), (4, 5, 6), (7, 8, 9), (45, 46, 47), (5000, 5, 57), (1, 100, 500), (100, 212, 555)]
twosortsnegativeone = lambda numbertuples: (numbertuples[2], numbertuples[0]*-1)
numbertuples.sort(key=twosortsnegativeone)
print(numbertuples) #print [(0, 7, -5), (1, 6, -4), (0, 6, -4), (1, 2, 3), (-100, -200, 3), (1, 2, 4), (3, 3, 5), (1, 3, 5), (4, 5, 6), (7, 8, 9), (45, 46, 47), (5000, 5, 57), (1, 100, 500), (100, 212, 555)]
twosortsnegativesign = lambda numbertuples: (numbertuples[2], -numbertuples[0])
numbertuples.sort(key=twosortsnegativesign) #print [(0, 7, -5), (1, 6, -4), (0, 6, -4), (1, 2, 3), (-100, -200, 3), (1, 2, 4), (3, 3, 5), (1, 3, 5), (4, 5, 6), (7, 8, 9), (45, 46, 47), (5000, 5, 57), (1, 100, 500), (100, 212, 555)]
print(numbertuples.sort(key=twosortsnegativesign)==numbertuples.sort(key=twosortsnegativeone)) #print True

a = [("Al", 2),("Bill", 1),("Carol", 2), ("Abel", 3), ("Zeke", 2), ("Chris", 1)]
print(a) #print [('Al', 2), ('Bill', 1), ('Carol', 2), ('Abel', 3), ('Zeke', 2), ('Chris', 1)]
b = sorted(sorted(a, key = lambda x : x[0]), key = lambda x : x[1], reverse = True)
print(b) #print [('Abel', 3), ('Al', 2), ('Carol', 2), ('Zeke', 2), ('Bill', 1), ('Chris', 1)]
c = sorted(a, key = lambda x: (-x[1], x[0]))
print(c) #print [('Abel', 3), ('Al', 2), ('Carol', 2), ('Zeke', 2), ('Bill', 1), ('Chris', 1)]

things = [("vehicle", "speed boat"), ("animal", "duck"), ("plant", "cactus"), ("animal", "bear"), ("vehicle", "school bus")]
print(things) #print [('vehicle', 'speed boat'), ('animal', 'duck'), ('plant', 'cactus'), ('animal', 'bear'), ('vehicle', 'school bus')]
things.sort() #data must be sorted first.
print(things) #print [('animal', 'bear'), ('animal', 'duck'), ('plant', 'cactus'), ('vehicle', 'school bus'), ('vehicle', 'speed boat')]

letters = ["AAAABBBCCDAABBB"]
print(letters) #print ['AAAABBBCCDAABBB']
lettersstring = "".join(letters)
print(lettersstring) #print AAAABBBCCDAABBB
print(type(lettersstring)) #print <class 'str'>
letterslist = [x for x in lettersstring]
print(letterslist) #print ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D', 'A', 'A', 'B', 'B', 'B']
letterslist.sort()
print(letterslist) #print ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'D']