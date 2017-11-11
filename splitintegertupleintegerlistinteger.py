#https://stackoverflow.com/questions/1906717/splitting-integer-in-python
from __future__ import division
number = 12345
for i in str(number):
	print(i) #print 1\n 2\n 3\n 4\n 5\n
splitnumber = []
for i in str(number):
	splitnumber.append(int(i))
print(splitnumber) #print [1, 2, 3, 4, 5]
#print(list(number)) #error message TypeError: 'int' object is not iterable
print(list(str(number))) #print ['1', '2', '3', '4', '5']
print((map(int,str(number)))) #print <map object at 0x7fd5ccf2e978>
print(list((map(int,str(number))))) #print [1, 2, 3, 4, 5]
integerlist = list(map(int,str(number)))
print(integerlist) #print [1, 2, 3, 4, 5]

#The function below "from __future__ import division" must be on top
#if do not want to use a list comprehension or you want to use a base different from 10
#for compatibility of // between Python 2 and 3
number = 12345
def digits(number, base=10):
	assert number >= 0
	if number == 0:
		return [0]
	l = []
	while number > 0:
		l.append(number % base)
		number = number // base
	return l
print(digits(number)) #print [5, 4, 3, 2, 1]

#https://stackoverflow.com/questions/10062673/python-convert-tuple-to-integer
import functools
input = (1, 3, 7)
print(functools.reduce(lambda rst, d: rst * 10 + d, (input))) #print 137
print(int("".join(map(str,input)))) #print 137
print(sum(n*10**i for (i,n) in enumerate(input[::-1]))) #print 137
output = int("{}{}{}".format(input[0],input[1],input[2]))
print(output) #print 137
print(type(output)) #print <class 'int'>

#https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
results = ["1","2","3"]
resultsinteger = list(map(int,results))
print(resultsinteger) #print [1, 2, 3]
resultsnew = []
for i in results:
	resultsnew.append(int(i))
print(resultsnew) #print [1, 2, 3]
resultsnew2 = [int(i) for i in results] #list comprehension
print(resultsnew2) #print [1, 2, 3]