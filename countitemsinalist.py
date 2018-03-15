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