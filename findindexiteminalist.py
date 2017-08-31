#Finding the index of an item given a list
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python

thelist = ["foo","bar","baz","bar"]
print(thelist.index("bar")) #print 1.  .index() returns only the first element which matches in the list.  ValueError appears if the target is not found.  .index(value, [start, [stop]])
thelist2 = ["foo","bar","baz","bar","bear","cat","nat","bar"]
print(thelist2.index("bar", 4,len(thelist2))) #print 7
thelist3 = ["foo","bar","baz","bar","bear","cat","nat","bar","pin","fan"]
for i, j in enumerate(thelist3): #Useful than index if there are duplicates.  index() only returns the first occurrence, while enumerate returns all occurrences.
	if j == "bar":
		print(i) #print 1\n 3\n 7\n 

#it appears numpy works, too.
import numpy as np
array = [1,2,1,3,4,5,1]
item = 1
nparray = np.array(array)
itemindex = np.where(nparray==item)
print(itemindex) #print (array([0, 2, 6]),)

thelist4 = ["foo","bar","baz","bar","bear","cat","nat","bar","pin","fan"]
item = "bar"
nparray = np.array(thelist4)
itemindex = np.where(nparray==item)
print(itemindex) #print (array([1, 3, 7]),)
print(itemindex[0]) #print [1, 3, 7]
print(itemindex[0][1]) #print 3
foritemindex = itemindex[0]
for n in range(0,len(foritemindex)):
	print(foritemindex[n]) #print 1\n 3\n 7\n
