#https://stackoverflow.com/questions/5584586/find-the-division-remainder-of-a-number
#https://www.youtube.com/watch?v=b5cb_nfDyyM
#https://www.youtube.com/watch?v=5PWU_KFHP54
#Modulo is a remainder operator

print(26/7) #print 3.7142857142857144
print(26%7) #print 5
print(-26%7) #print 2.  Note that the modulo operator always returns a positive number, so for negative numbers it might not be what you would expect when talking about the remainder: -10 % 3 == 2.
print(10%3) #print 1, modulo are positive integers
print(-10%3) #print 2, here's modulo with a negative integer
print((26/7)*7 + 26%7) #print 31.0.  (a/b)*b + a%b == a
print("\n")

num = 26
div = 13
while num >= div:
	num -= div  #num >=0 and div > 0
print(num) #print 0
print(num, div, sep=":") #print 0:13
#modulo, divmod
print(2%10) #print 2
print(3%99) #print 3
print(16%770) #print 16
print(67.9%4) #print 3.9000000000000057
print(67.9//4) #print 16.0
print(16*4) #print 64
print(64+3.9000000000000057) #print 67.9
x, y = 55, 44
print(x,y, sep="--") #print 55--44
print("johnson","operator", sep="--") #print johnson--operator
print(1482//60) #print 24
print(1482%60) #print 42
print(divmod(1482,60)) #print (24, 42)
check = divmod(1482,60)
print(check[0]) #print 24
print(check[1]) #print 42
print(10//5) #print 2
print(10%5) #print 0
print(divmod(10,5)) #print (2, 0)
ten, five = divmod(10,5)
print(ten) #print 2
print(five) #print 0
print(137%60) #print 17
seconds = 137
minutes, seconds = divmod(seconds, 60)
print(minutes) #print 2
print(seconds) #print 17
print(26-26//7*7) #print 5