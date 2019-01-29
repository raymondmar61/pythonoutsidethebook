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

#https://pymotw.com/3/collections/counter.html#initializing

#https://data-flair.training/blogs/python-counter/


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