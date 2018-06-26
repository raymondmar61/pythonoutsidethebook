#threeintegers = input("Enter three integers separated by a space ")
threeintegers = "5 7 45"
print(threeintegers) #print 5 7 45
threeintegers = threeintegers.split(" ")
print(threeintegers) #print ['5', '7', '45']
threeintegers = list(map(int,threeintegers)) #convert list string to list integers
print(threeintegers) #print [5, 7, 45]
threeintegers.sort()
print(str(threeintegers).strip("[]")) #print 5, 7, 45.  Extract integers out of list to string with commas

p = [x for x in range(1,11)]
print(p) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pp = {n for n in range(1,11)}
print(pp) #print {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

numberlist = []
for n in range(1,21):
	numberlist.append(n)
print(numberlist) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for x in numberlist[-2::-1]:
	print(x) #print 19\n 18\n 17\n , , , 3\n 2\n, 1\n