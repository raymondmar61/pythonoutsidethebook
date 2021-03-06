#https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-math

#https://www.hackerrank.com/challenges/polar-coordinates/problem
'''
z = x+yj x is real, y is imaginary, j is imaginary unit.
A polar coordinate(r,yy) is determined by modulus r and phase angle yy.
Convert z to its polar coordinate, r=distance from z to origin or (x^2+y^2)^.5.
yy is counter clockwise angle measured from the positive x-axis to the line segment that joins z to the origin.
'''
from cmath import phase
print(phase(complex(-1.0,0.0))) #print 3.141592653589793 which is z
print(abs(complex(-1.0,0.0))) #print 1.0 which is the modulus or absolute value of z
rvariable = 1
yyvariable = 2
print(abs(complex(rvariable,yyvariable))) #print 1.0 which is the modulus or absolute value of z
print(phase(complex(rvariable,yyvariable))) #print 3.141592653589793 which is z

#https://www.hackerrank.com/challenges/find-angle/problem
'''
Triangle ABC is a right triangle.  90 degrees at B.
M is the midpoint of hypotenuse AC.
Given AB and BC lengths both between 0 and 100 inclusive.  AB is first line.  BC is second line.  AC is hypotenuse third line.
Find the angle MBC.  M is on the hypotenuse AC.
'''
from math import cos, degrees, sqrt
ab = 10
bc = 10
ac = sqrt(((ab**2)+(bc**2)))
print(ac) #print 14.142135623730951 to get the hypotenuse
cosa = ((ab**2) + (bc**2) - ac)/(2*ac*bc) #calculate the angle between ab and bc
print(cos(cosa)) #print 0.7917628038359196 calculate the angle between bc and bc
print(degrees(cos(cosa))) #print 45.3646670352427 convert cos(cosa) to degrees

#https://www.hackerrank.com/challenges/triangle-quest-2/problem
#https://stackoverflow.com/questions/34494247/solving-palindromic-triangle-quest-puzzle-in-python
'''
You are given a positive integer N.  Your task is to print a palindromic triangle of size N.
For example, a palindromic triangle of size 5 is:
1
121
12321
1234321
123454321
'''
n = 10
for n in range(1,n+1):
	print((111111111//(10**(9-n)))**2)
#No two line Python code
n = 1
while n < 20:	
	beginninglist = []
	if n == 1:
		print(n)
	else:
		for n in range(1,n+1):
			beginninglist.append(str(n))
		beginningpart = ("".join(beginninglist))
		endingpart = ("".join(beginninglist[len(beginninglist)-2::-1]))
		print(beginningpart+""+endingpart)
	n += 1

#https://www.hackerrank.com/challenges/python-mod-divmod/problem
#The first line is the integer division
#The second line is the result of the modulo operator.
#The third line prints the divmod
print(divmod(177,10)) #print (17, 7).  177/10=17 remainder 7 or 177/10=>17 177%10=>7
a=177
b=10
print((a//b)) #print 17
print(a%b) #print 7
print(divmod(a,b)) #print (17, 7)

#https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
#integers a, b, c, d.  Print (a^b)+(c^d)
a=9
b=29
c=7
d=27
print((a**b)+(c**d)) #print 4710194409608608369201743232

#https://www.hackerrank.com/challenges/python-quest-1/problem
#https://stackoverflow.com/questions/30336222/python-triangle-quest-arithmetical-operation-inside-print
#You are given a positive integer . Print a numerical triangle of height  like the one below:
'''
1
22
333
4444
55555
......
'''
for i in range(1,9):
	print((i*(10**i - 1))//9)
for i in range(1,10):
	print(str(i)*i)