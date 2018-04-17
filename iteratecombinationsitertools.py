#https://docs.python.org/3.5/library/itertools.html, https://stackoverflow.com/questions/41680388/how-do-i-iterate-through-combinations-of-a-list, https://stackoverflow.com/questions/16384109/iterate-over-all-combinations-of-values-in-multiple-lists-in-python
#RM:  there are more functions in itertools.  I selected the product(), combinations(), permutations(), chain(), chain.from_iterable().

import itertools
firstlist = [1,5,8]
secondlist = [0.5, 4]
print(list(itertools.product(firstlist, secondlist))) #print [(1, 0.5), (1, 4), (5, 0.5), (5, 4), (8, 0.5), (8, 4)]
print(list(itertools.product(firstlist, secondlist))) #print [(1, 0.5), (1, 4), (5, 0.5), (5, 4), (8, 0.5), (8, 4)]

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
list1234 = [1, 2, 3, 4]
for productpairs in itertools.permutations(list1234, 2):
	print(productpairs,end=";") #print (1, 2);(1, 3);(1, 4);(2, 1);(2, 3);(2, 4);(3, 1);(3, 2);(3, 4);(4, 1);(4, 2);(4, 3);  RM:  prints 1,2 and 2,1
list1234 = [1, 2, 3, 4]
for productpairs in itertools.product(list1234, repeat=2):
	print(productpairs,end=",") #print (1, 1),(1, 2),(1, 3),(1, 4),(2, 1),(2, 2),(2, 3),(2, 4),(3, 1),(3, 2),(3, 3),(3, 4),(4, 1),(4, 2),(4, 3),(4, 4),  RM: prints all combinations such as 1,1; 1,2; 2,1
print("\n")

firstlist = [1,5,8]
secondlist = [0.5, 4]
thirdlist = [10,11,12]
print(list(itertools.product(firstlist, secondlist, thirdlist))) #print [(1, 0.5, 10), (1, 0.5, 11), (1, 0.5, 12), (1, 4, 10), (1, 4, 11), (1, 4, 12), (5, 0.5, 10), (5, 0.5, 11), (5, 0.5, 12), (5, 4, 10), (5, 4, 11), (5, 4, 12), (8, 0.5, 10), (8, 0.5, 11), (8, 0.5, 12), (8, 4, 10), (8, 4, 11), (8, 4, 12)]
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