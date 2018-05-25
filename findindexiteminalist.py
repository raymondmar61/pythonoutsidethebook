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
print("\n")

#05/24/2018 take two
animallist = ["dog","cat","cow","bird","mouse","bear","rabbit"]
findanimal = "bear"
if findanimal in animallist:
	print(findanimal+" exists") #print bear exists
	print(animallist.index(findanimal)) #print 5
else:
	print(None)

def findindexes(value, indexlist):
	indicesinindexlist = []
	indexnumber = -1
	while True:
		try:
			print("value before: ",value)
			print("indexnumber before: ",indexnumber)
			print(indicesinindexlist)
			indexnumber = indexlist.index(value, indexnumber+1) #.index(value, [start, [stop]])
			print("value after: ",value)
			print("indexnumber after: ",indexnumber)
			indicesinindexlist.append(indexnumber) #appending the indexnumber to list indicesinindexlist
			print(indicesinindexlist)
		except ValueError:
			print("Let's break")
			break
	return indicesinindexlist
print(findindexes("mouse",["dog","cat","cow","bird","mouse","bear","rabbit"]))
print(findindexes("cat",["dog","cat","cow","bird","mouse","bear","rabbit"]))
print(findindexes("cow",["cow","cat","cow","bird","mouse","cow","rabbit"])) #print [0, 2, 5]
print("\n")

#side note on .index()
thelist = []
templist = ["baseball","basketball","football","hockey"]
indexnumber = templist.index("football",2) #start search index position 2
thelist.append(indexnumber) #appending the indexnumber to list thelist
print(thelist) #print [2]

def findindexes2(value, indexlist):
	try:
		indexelement = indexlist.index(value)
		return indexelement
	except ValueError:
		print(None)
print(findindexes2("mouse",["dog","cat","cow","bird","mouse","bear","rabbit"])) #print 4
print(findindexes2("cow",["dog","cat","cow","bird","mouse","bear","rabbit"])) #print 2
print(findindexes2("cow",["cow","cat","cow","bird","mouse","cow","rabbit"])) #print 0  #findindexes2 function doesn't work multiple items
print("\n")

approvedsums = [5, 11, 19]
for eachnumber in range(5,20):
	try:
		print(isinstance(approvedsums.index(eachnumber),int) == True)
		print(eachnumber,"in list")
	except ValueError:
		print(eachnumber,"not in list")
		continue
for eachnumber in range(5,20):
	sums = eachnumber + 1
	try:
		print(isinstance(approvedsums.index(sums),int) == True)
		print(sums,"sums in list")
	except ValueError:
		print(sums,"sums not in list")
		continue
print("\n")

mylist = ["blue","black","white","red","brown","orange","yellow"]
myterm = "white"
#get the index position for myterm
for i in range(0,len(mylist)):
	if mylist[i]==myterm:
		print(i) #print 2
#get the value or item from mylist
for eachmylist in mylist:
	if eachmylist==myterm:
		print(eachmylist) #print white
#get the first value or item from mylist only
print(mylist.index(myterm)) #print 2
#also
if myterm in mylist:
	print(mylist.index(myterm)) #print 2
else:
	None
