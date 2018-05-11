#threeintegers = input("Enter three integers separated by a space ")
threeintegers = "5 7 45"
print(threeintegers) #print 5 7 45
threeintegers = threeintegers.split(" ")
print(threeintegers) #print ['5', '7', '45']
threeintegers = list(map(int,threeintegers)) #convert list string to list integers
print(threeintegers) #print [5, 7, 45]
threeintegers.sort()
print(str(threeintegers).strip("[]")) #print 5, 7, 45.  Extract integers out of list to string with commas
