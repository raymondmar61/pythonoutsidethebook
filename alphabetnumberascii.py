#Python code for calculating number of an alphabet
#https://stackoverflow.com/questions/4319392/python-code-for-calculating-number-of-an-alphabet

letter = "r"
print(ord(letter)) #print 114
number = 114
print(chr(number)) #print r

lettera = "a"
print(ord(lettera)) #print 97
print(ord(lettera)%32) #print 1
letterA = "A"
print(ord(letterA)) #print 65
print(ord(letterA)%32) #print 1
#I believe %32 starts the letter a and letter A count at 1

for eachnumber in range(97,97+26):
	print(chr(eachnumber)) #print a-z in it's separate line
for eachnumber in range(65,65+26):
	print(chr(eachnumber)) #print A-Z in it's separate line

startoneeachlettertest = "eciwlckpqzAEIOUZ"
for eachstartoneeachlettertest in startoneeachlettertest:
	print("{}:{}".format(eachstartoneeachlettertest, ord(eachstartoneeachlettertest)%32),end=", ") #print e:5, c:3, i:9, w:23, l:12, c:3, k:11, p:16, q:17, z:26, A:1, E:5, I:9, O:15, U:21, Z:26


