#String repeated characters
#https://stackoverflow.com/questions/32090058/testing-whether-a-string-has-repeated-characters
#Custom function and set comprehensions are much faster than Counter.
numberstring = "12348546478"

from collections import Counter
for i, j in Counter(numberstring).items():
	if j>1:
		print("String "+i+" printed "+str(j)+" times.") #print String 4 printed 3 times.\n String 8 printed 2 times.

#custom function
def finder(s):
	seen,yields=set(),set()
	for i in s:
		if i in seen:
			if i not in yields:
				yield i
				yields.add(i)
			else:
				yields.add(i)
		else:
			seen.add(i)
print(list(finder(numberstring))) #print ['4', '8']

returnsetlist = []
for eachnumberstring in numberstring:
	if numberstring.count(eachnumberstring) > 1:
		print(eachnumberstring) #print 4\n8\n4\n4\n8.  Printed all of the duplicates or repeats
		returnsetlist.append(eachnumberstring)
print(set(returnsetlist)) #print {'8', '4'}
print(list(set(returnsetlist))) #print ['8', '4']
print(list(map(int,set(returnsetlist)))) #print [8, 4]

print(len(set(numberstring)) == len(numberstring)) #print False because numberstring has repeated characters.

from collections import defaultdict
countlist = defaultdict(int)
for eachnumberstring in numberstring:
	countlist[eachnumberstring] += 1
print(countlist) #print defaultdict(<class 'int'>, {'2': 1, '6': 1, '4': 3, '7': 1, '3': 1, '8': 2, '1': 1, '5': 1})
print(dict(countlist)) #print {'7': 1, '2': 1, '5': 1, '6': 1, '1': 1, '4': 3, '3': 1, '8': 2}
print(max(zip(countlist.values(), countlist.keys()))) #print (3,'4')

