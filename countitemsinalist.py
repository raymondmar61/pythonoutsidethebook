from collections import Counter
colorlist = ["green","white","blue","blue","white","blue","green","white","green","yellow","white","blue","white","yellow","white","green","blue","red","red","white","blue","red","yellow","green","blue"]
print(len(colorlist)) #print 25
print(Counter(colorlist)) #print Counter({'blue': 7, 'white': 7, 'green': 5, 'red': 3, 'yellow': 3})
print(colorlist.count("white")) #print 7
print(colorlist.count("green")) #print 5

#count() works for tuple
t=tuple("aabbbbffffff")
print(t.count("a")) #print 2
print(t.count("f")) #print 6
print()

"""
def duplicateencode(word):
	newword = ""
	word = word.lower()
	counter = Counter(word)
	for c in word:
		print(c, counter[c]) #duh, it's a dictionary.  print the key and its value.
		if counter[c] == 1:
			print("(")
			newword += "("
		else:
			print(")")
			newword += ")"
	print(newword)	
duplicateencode("dldwwTwe())") #print )()))()(())
"""

#https://www.programiz.com/python-programming/methods/string/count
string = "Python is awesome, isn't it?"
countword = "is"
count = string.count(countword)
print(countword+" counter is",count) #print is counter is 2
countword = "i"
startandendcount = string.count(countword, 8, 25) #start at index 8 and end at index 25 exclusive.  Count number of countword i between 8 and 25
print(countword+" counter is",startandendcount) #print i counter is 1

#https://docs.python.org/3/library/collections.html#collections.Counter
colorcounter = Counter()
colorlist = ['red', 'blue', 'red', 'green', 'blue', 'blue']
for eachcolorlist in colorlist:
	colorcounter[eachcolorlist] += 1
print(colorcounter) #print Counter({'blue': 3, 'red': 2, 'green': 1})
print(Counter(colorlist)) #print Counter({'blue': 3, 'red': 2, 'green': 1})  RM:  no need for the for eachcolorlist in colorlist for loop
words = "The late Steve Jobs said, \"You can\'t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.\" There are sayings regarding a person living a bad life. It can\'t get worse; it can only get better. Everyone must experience hell before heaven. Frustrations, mistakes, and pain are part of growing up. Be prepared for failures before success. Everyone has bad years and everyone has good years. You win some and you lose some. Sometimes bad years are nobody\'s fault--it\'s life. The bottom line is everything we do today affects tomorrow; in particular, if life is bad today, then do something for a good life tomorrow. Trust hard work intelligently, good luck, and favorable timing everything goes well soon. There is a light at the end of the tunnel. Hope for the best.I share my past bad years which became future good years.  I hope my past history dictates what happens for the rest of 2017 and beyond because I\'m unemployed and I live with my parents. <b>2000.</b> The Y2K catastrophe never happened. My company moved to a new building for which everyone settled in slowly. The dot-com stock market crashed creating a recession.  Most people didn\'t know how to handle the uncertainty beginning a new millennium which included myself. Fanime Con 2000 which took place at a convention center and held for four days both for the first time was bad. Anime Expo 2000 which took place at Disneyland could be considered one of the worse big anime conventions in anime convention history."
print(Counter(words).most_common(5)) #print [(' ', 288), ('e', 153), ('o', 114), ('t', 95), ('n', 94)]
wordslist = words.split()
print(wordslist) #print words string in a list each item is a word
print(Counter(wordslist).most_common(5)) #print [('the', 9), ('a', 8), ('and', 7), ('for', 7), ('bad', 5)]
print(Counter(wordslist).most_common()[:-4-1:-1]) #[('history.', 1), ('conventions', 1), ('big', 1), ('worse', 1)].  The 4 least common elements.
c = Counter() # a new, empty counter
c = Counter('gallahad') #a new counter from an iterable
c = Counter({'red': 4, 'blue': 2}) # a new counter from a mapping
c = Counter(cats=4, dogs=8) #a new counter from keyword args
breakfastc = Counter(["eggs","ham","cheese","cheese","sausage"])
print(breakfastc["eggs"]) #print 1
print(breakfastc["bacon"]) #print 0
print(breakfastc["cheese"]) #print 2
print(breakfastc["sausage"]) #print 1
breakfastc["sausage"] = 0 #Setting a count to zero does not remove an element from a counter. Use del to remove it entirely.
print(breakfastc) #Counter({'cheese': 2, 'eggs': 1, 'ham': 1, 'sausage': 0})
del breakfastc["sausage"]
print(breakfastc) #Counter({'cheese': 2, 'eggs': 1, 'ham': 1})
lettersc = Counter(a=4, b=2, c=0, d=-2)
print(lettersc)  #print Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2})
iwantletters = sorted(lettersc.elements()) #Return an iterator over elements repeating each as many times as its count. Elements are returned in arbitrary order. If an element’s count is less than one, elements() will ignore it.
print(iwantletters) #print ['a', 'a', 'a', 'a', 'b', 'b']
print(lettersc.most_common(1)) #print [('a', 4)]
lettersc = Counter(a=4, b=2, c=0, d=-2)
lettersd = Counter(a=1, b=2, c=3, d=4)
lettersc.subtract(lettersd)
print(lettersc) #print Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
print(lettersc.most_common(2)) #print [('a', 3), ('b', 0)]
print(sum(lettersc.values())) #print -6, sum the counts
lettersc.clear() #reset all counts
print(sum(lettersc.values())) #print 0
lettersc = Counter(a=4, b=2, c=0, d=-2)
print(list(lettersc)) #print ['a', 'b', 'c', 'd']
print(set(lettersc)) #print {'b', 'a', 'c', 'd'}
print(dict(lettersc)) #print {'a': 4, 'b': 2, 'c': 0, 'd': -2}
print(lettersc.items()) #print dict_items([('a', 4), ('b', 2), ('c', 0), ('d', -2)])
listofpairs = lettersc.items()
print(Counter(dict(listofpairs))) #print Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2})
lettersc = Counter(a=4, b=2, c=0, d=-2)
print(lettersc) #print Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
print(+lettersc) #print Counter({'a': 4, 'b': 2}).  Remove zero and negative counts
c2 = Counter(a=3, b=1)
d2 = Counter(a=1, b=2)
print(c2 + d2) #print Counter({'a': 4, 'b': 3}) add two counters together:  c[x] + d[x]
print(c2 - d2) #print Counter({'a': 2}) subtract (keeping only positive counts)
print(c2 & d2) #print Counter({'a': 1, 'b': 1}) intersection:  min(c[x], d[x]) # doctest: +SKIP
print(c2 | d2) #print Counter({'a': 3, 'b': 2}) union:  max(c[x], d[x])
c3 = Counter(a=2, b=-4)
print(+c3) #print Counter({'a': 2})
print(-c3) #print Counter({'b': 4})

#https://www.dotnetperls.com/counter-python
from random import randint
numberslist = []
counter = 0
counterstop = randint(20,25)
while counter <= counterstop:
	numberslist.append(randint(5,15))
	counter +=1
print(numberslist)
print(Counter(numberslist))
countbirds = Counter()
countbirds["birds"] += 1
countbirds["birds"] += 1
countbirds["birds"] += 1
print(countbirds) #print Counter({'birds': 3})
countbirds["birds"] += 1
print(countbirds) #print Counter({'birds': 4})
countbirds["birds"] -= 1
print(countbirds) #print Counter({'birds': 3})
countbirds["birds"] = 100
print(countbirds) #print Counter({'birds': 100})

#https://pymotw.com/3/collections/counter.html#initializing
print(Counter(["a","b","c","a","b","c"])) #print Counter({'a': 2, 'b': 2, 'c': 2})
print(Counter({"a":2, "b":3, "c":1})) #print Counter({'b': 3, 'a': 2, 'c': 1})
print(Counter(a=2, b=3, c=1)) #print Counter({'b': 3, 'a': 2, 'c': 1})
#An empty Counter can be constructed with no arguments and populated via the update() method
emptycountervariable = Counter()
print("Empty variable no counts",emptycountervariable) #print Empty variable no counts Counter()
emptycountervariable.update("abcdaab")
print("First count from emptycountervariable variable is now non-empty", emptycountervariable) #print First count from empty variable no counts now non-empty Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
emptycountervariable.update("ad")
print("Second count from emptycountervariable variable add a and add d", emptycountervariable) #print Second count from emptycountervariable variable is now non-empty Counter({'a': 4, 'b': 2, 'd': 2, 'c': 1})
#A populated Counter values can be retrieved using the dictionary API.
accessvalues = Counter("abcdaab")
print(accessvalues) #print Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
for eachletter in "abcd":
	print("{}:{}".format(eachletter, accessvalues[eachletter])) #print a:3\n b:2\n c:1\n d:1
for key, value in accessvalues.items():
	print(key, value) #print a 3\n b 2\n c 1\n d 1
#addinum to #A populated Counter values can be retrieved using the dictionary API.
countthestring = "abcdaab"
accessvalues = Counter(countthestring)
print(accessvalues) #print Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
for eachletter in "abcd":
	print("{}:{}".format(eachletter, accessvalues[eachletter])) #print a:3\n b:2\n c:1\n d:1
for key, value in accessvalues.items():
	print(key, value) #print a 3\n b 2\n c 1\n d 1
for eachcountthestring in countthestring:
	print(eachcountthestring, accessvalues[eachcountthestring]) #print a 3\n b 2\n c 1\n d 1\n a 3\n a 3\ b 2
#The elements() method returns an iterator that produces all of the items in Counter.
elementsvariable = Counter("extremely")
print(elementsvariable) #print Counter({'e': 3, 'x': 1, 't': 1, 'r': 1, 'm': 1, 'l': 1, 'y': 1})
print(elementsvariable["e"]) #print 3
print(elementsvariable["z"]) #print 0
print(list(elementsvariable.elements())) #print ['e', 'e', 'e', 'x', 't', 'r', 'm', 'l', 'y']
#Use most_common() to produce a sequence of the n most frequently encountered input values and their respective counts
words2 = "The late Steve Jobs said, \"You can\'t connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future.\" There are sayings regarding a person living a bad life. It can\'t get worse; it can only get better. Everyone must experience hell before heaven. Frustrations, mistakes, and pain are part of growing up. Be prepared for failures before success. Everyone has bad years and everyone has good years. You win some and you lose some. Sometimes bad years are nobody\'s fault--it\'s life. The bottom line is everything we do today affects tomorrow; in particular, if life is bad today, then do something for a good life tomorrow. Trust hard work intelligently, good luck, and favorable timing everything goes well soon. There is a light at the end of the tunnel. Hope for the best.I share my past bad years which became future good years.  I hope my past history dictates what happens for the rest of 2017 and beyond because I\'m unemployed and I live with my parents. <b>2000.</b> The Y2K catastrophe never happened. My company moved to a new building for which everyone settled in slowly. The dot-com stock market crashed creating a recession.  Most people didn\'t know how to handle the uncertainty beginning a new millennium which included myself. Fanime Con 2000 which took place at a convention center and held for four days both for the first time was bad. Anime Expo 2000 which took place at Disneyland could be considered one of the worse big anime conventions in anime convention history."
counterletters = Counter(words2)
for letters, count in counterletters.most_common(5):
	print(letters, count) #print ' ' 270\n e 153\n o 114\n t 95\n n 94
wordslist2 = words2.split()
print(wordslist2) #print counterwords string in a list each item is a word
counterwordslist2 = Counter(wordslist2)
for words, count in counterwordslist2.most_common(5):
	print(words, count) #print the 9\n a 8\n and 7\n for 7\n bad 5
for words, count in counterwordslist2.most_common()[:-5-1:-1]:
	print(words, count) #print history. 1\n conventions 1\n big 1\n worse 1\n one 1 Five least common words
#Arithmetic add, subtract, intersect, union Counter
collection1 = Counter(["a","b","c","a","b","b"])
collection2 = Counter("alphabet")
print(collection1) #print Counter({'b': 3, 'a': 2, 'c': 1})
print(collection2) #print Counter({'a': 2, 'l': 1, 'p': 1, 'h': 1, 'b': 1, 'e': 1, 't': 1})
print("Add collection1 and collection2", collection1+collection2) #print Add collection1 and collection2 Counter({'a': 4, 'b': 4, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})
print("Subtract collection1 and collection2", collection1-collection2) #print Subtract collection1 and collection2 Counter({'b': 2, 'c': 1})
print("Intersection takes positive minimums collection1 and collection2", collection1 & collection2) #print Intersection takes positive minimums collection1 and collection2 Counter({'a': 2, 'b': 1})
print("Union takes maximums collection1 and collection2", collection1 | collection2) #print Union takes maximums collection1 and collection2 Counter({'b': 3, 'a': 2, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})

#https://data-flair.training/blogs/python-counter/
lettercounter = Counter(["a","b","c","a","b","a"])
print(lettercounter) #print Counter({'a': 3, 'b': 2, 'c': 1})
print(lettercounter["a"]) #print 3
lettercounterlist = Counter(["a","b","c","a","b","a"])
print(lettercounterlist) #print Counter({'a': 3, 'b': 2, 'c': 1})
print(lettercounterlist["a"]) #print 3
lettercountertuple = Counter(("a","b","c","a","b","a"))
print(lettercountertuple) #print Counter({'a': 3, 'b': 2, 'c': 1})
print(lettercountertuple["a"]) #print 3
letterstring = Counter("Hello")
print(letterstring) #print Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
print(letterstring["l"]) #print 2
lettercounterset = Counter({"a","b","c","a","b","a"})
print(lettercounterset) #print Counter({'b': 1, 'a': 1, 'c': 1})
print(lettercounterset["a"]) #print 1
lettercounterdictionary = Counter({"a":3, "b":2, "c":1})
print(lettercounterdictionary) #print Counter({'a': 3, 'b': 2, 'c': 1})
print(lettercounterdictionary["a"]) #print 3
lettercounterkeywordarguments = Counter(a=3, b=2, c=1)
print(lettercounterkeywordarguments) #print Counter({'a': 3, 'b': 2, 'c': 1})
print(lettercounterkeywordarguments["a"]) #print 3
hellocounter = Counter()
print(hellocounter) #print Counter()
hellocounter.update("Hello")
print(hellocounter) #print Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
hellocounter.update("Goodbye")
print(hellocounter) #print Counter({'o': 3, 'e': 2, 'l': 2, 'H': 1, 'G': 1, 'd': 1, 'b': 1, 'y': 1})
hellocounter.update({"z":50})
print(hellocounter) #print Counter({'z': 50, 'o': 3, 'e': 2, 'l': 2, 'H': 1, 'G': 1, 'd': 1, 'b': 1, 'y': 1})
print(hellocounter["o"]) #print 3
print(hellocounter["w"]) #print 0
for key, value in hellocounter.items():
	print(key, value) #print H 1\n e 2\n l 2\n o 3\n G 1\n d 1\n b 1\n y 1\n z 50
print(hellocounter.most_common(3)) #print [('z', 50), ('o', 3), ('e', 2)]
print(hellocounter.most_common(5)) #print [('z', 50), ('o', 3), ('e', 2), ('l', 2), ('H', 1)]
print(hellocounter.most_common()) #print [('z', 50), ('o', 3), ('e', 2), ('l', 2), ('H', 1), ('G', 1), ('d', 1), ('b', 1), ('y', 1)]
valuescount = Counter("Hello")
for n in valuescount.elements():
	print(n, valuescount[n]) #print H 1\n e 1\n l 2\n l 2\n o 1.  The elements() method returns an iterator object for the values in the Counter.  Note l 2 is printed twice because there are two l's.
for n in "Help":
	print(n, valuescount[n]) #print H 1\n e 1\n l 2\n p 0
print(valuescount.most_common()) #print [('l', 2), ('H', 1), ('e', 1), ('o', 1)]
valuescount["H"]=234
print(valuescount.most_common()) #print [('H', 234), ('l', 2), ('e', 1), ('o', 1)]
valuescount.clear()
print(valuescount.most_common()) #print []
mathcounter1 = Counter({"a":3, "b":2, "c":1})
mathcounter2 = Counter({"c":3, "d":2, "e":1})
print(mathcounter1+mathcounter2) #print Counter({'c': 4, 'a': 3, 'b': 2, 'd': 2, 'e': 1})
print(mathcounter1-mathcounter2) #print Counter({'a': 3, 'b': 2}) mathcounter1-mathcounter2 doesn't have c because 1-3=-2.  Negative counts mean nothing.
print(mathcounter2-mathcounter1) #print Counter({'c': 2, 'd': 2, 'e': 1}) mathcounter2-mathcounter1 doesn't have a and b.  c is 3-1 or 2.
#print(mathcounter1.subtract(mathcounter2))
mathcounter1.subtract(mathcounter2)
print(mathcounter1) #print Counter({'a': 3, 'b': 2, 'e': -1, 'c': -2, 'd': -2})
mathcounter1 = Counter({"a":3, "b":2, "c":1})
mathcounter2 = Counter({"c":3, "d":2, "e":1})
mathcounter2.subtract(mathcounter1)
print(mathcounter2) #print Counter({'c': 2, 'd': 2, 'e': 1, 'b': -2, 'a': -3})
print("\n")
mathcounter1 = Counter({"a":3, "b":2, "c":1})
mathcounter2 = Counter({"c":3, "d":2, "e":1})
print(mathcounter1&mathcounter2) #print Counter({'c': 1}) & and
print(mathcounter2&mathcounter1) #print Counter({'c': 1}) & and
print(mathcounter1|mathcounter2) #print Counter({'a': 3, 'c': 3, 'b': 2, 'd': 2, 'e': 1}) | or
print(mathcounter2|mathcounter1) #print Counter({'c': 3, 'a': 3, 'd': 2, 'b': 2, 'e': 1}) | or

#Stack Overflow get a count of dictionary keys with values greater than some integer in python
nouns = {"house":2, "water":41, "Joey":409, "boy":3, "girl":1}
for key, value in nouns.items():
	if value > 50:
		print(key+" is greater than 50")
	elif value > 20:
		print(key+" is greater than 20")
	elif value > 2:
		print(key+" is greater than 2")
	elif value > 0:
		print(key+" is greater than 0")
	else:
		print(key+" is nothing")
valuescount = Counter(nouns)
for n in valuescount.elements():
	print(n) #prints elements number of times; e.g. house\n house\n . . . boy\n boy\n boy\n girl
for n in valuescount.values():
	print(n) #prints 2\n 41\n 409\n 3\n 1
tallylist = []
for key, value in nouns.items():
	if value > 50:
		tallylist.append(">50")
	elif value > 20:
		tallylist.append(">20")
	elif value > 2:
		tallylist.append(">2")
	elif value > 0:
		tallylist.append(">0")
	else:
		tallylist.append("nothing")
tallylistcounter = Counter(tallylist)
print(tallylistcounter) #print Counter({'>0': 2, '>20': 1, '>50': 1, '>2': 1})