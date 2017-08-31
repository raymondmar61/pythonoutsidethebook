#YouTube channel apmonitor.com.  Arrays in Python Numpy, Numpy and Loops in Python videos.
#vector arrays are one dimensional.  matrices arrays are two or more dimensional

import numpy as np

x = [1, 2, 3.5, 10, 20]
print(x) #print [1, 2, 3.5, 10, 20]
print(x[2]) #print 3.5
print(x[-1]) #print 20, the last element
print(x[-2]) #print 10, the second to the last element
print(x[0:2]) #print [1, 2], remember, subtract one from the right of colon
print(x[3:]) #print [10, 20]
xcar = [1, 2, "car", 10, 20]
print(xcar) #print [1, 2, 'car', 10, 20]
print(xcar[2]) #print ca
print(xcar[2][1]) #print a
print(xcar[2][0:2]) #print ca

y = np.array([1, 2, 3, 10, 20])
print(y) #print [ 1  2  3 10 20] treats all numbers as integers
y = np.array([1, 2, 3.5, 10, 20])
print(y) #print [  1.    2.    3.5  10.   20. ] treats all numbers as floats
print(np.mean(y)) #print 7.3
print(np.max(y)) #print 20.0
print(np.min(y)) #print 1.0
t = np.empty(5) #create a new array which is "blank" or five "blank" elements.  np.zeros(number of blanks) and np.ones(number of blanks) work
print(t) #print [ 0.  0.  0.  0.  0.]
t = np.linspace(0,1,5) #five elements between 0 and 1 evenly spaced
print(t) #print [ 0.    0.25  0.5   0.75  1.  ]
t = np.linspace(0,1,6) #six elements between 0 and 1 evenly spaced
print(t) #print [ 0.   0.2  0.4  0.6  0.8  1. ]

import matplotlib.pyplot as plt
t = np.linspace(0,1,5) #five elements between 0 and 1 evenly spaced
y = np.array([1, 2, 3.5, 10, 20])
plt.plot(t,y,"ro") #red circles t is x-axis, y is y-axis
plt.show()

#create an array of 50 ones called x
x = np.ones(50)
print(x) #print [ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
print(len(x)) #print 50

#create an array from 1-20 with 50 equally-spaced elements two different ways (using a loop and a single command).  Call the two arrays y and z.
y = np.linspace(1,20,50) #linear spaced
print(y) #print [  1.           1.3877551    1.7755102    2.16326531   2.55102041   2.93877551   3.32653061   3.71428571   4.10204082   4.48979592   4.87755102   5.26530612   5.65306122   6.04081633   6.42857143   6.81632653   7.20408163   7.59183673   7.97959184   8.36734694   8.75510204   9.14285714   9.53061224   9.91836735  10.30612245  10.69387755  11.08163265  11.46938776  11.85714286  12.24489796  12.63265306  13.02040816  13.40816327  13.79591837  14.18367347  14.57142857  14.95918367  15.34693878  15.73469388  16.12244898  16.51020408  16.89795918  17.28571429  17.67346939  18.06122449  18.44897959  18.83673469  19.2244898   19.6122449   20.        ]
#print(help(np.linspace)) #shows the help and the defaults for linspace
z = np.empty(50)
print(z) #print [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
z = np.empty(50)
for i in range(50):
	z[i] = i * ((20-1)/49) + 1
print(z) #print [  1.           1.3877551    1.7755102    2.16326531   2.55102041   2.93877551   3.32653061   3.71428571   4.10204082   4.48979592   4.87755102   5.26530612   5.65306122   6.04081633   6.42857143   6.81632653   7.20408163   7.59183673   7.97959184   8.36734694   8.75510204   9.14285714   9.53061224   9.91836735  10.30612245  10.69387755  11.08163265  11.46938776  11.85714286  12.24489796  12.63265306  13.02040816  13.40816327  13.79591837  14.18367347  14.57142857  14.95918367  15.34693878  15.73469388  16.12244898  16.51020408  16.89795918  17.28571429  17.67346939  18.06122449  18.44897959 18.83673469  19.2244898   19.6122449   20.        ]
print(z-y) #print [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]

#create a matrix, m, as a 1x1 numpy array of value 1.  Using a while loop, append a random integer between 1 and 10 to the end of matrix m until the last element is a 7.  Report the number of elements in m and the mean value of the elements after the loop. . . . create a variable i to keep track of how many times you have gone through the while loop.  If i exceeds 30, exit the while loop.  Don't report the matrix size using i.
import random
m = np.ones(1)
print(m) #print [ 1.]
i = 1
# instructor set i = 0 with while loop below.  My while loop is more accurate.
# while m[-1] != 7:
# 	m = np.append(m,random.randint(1,100))
# 	i = i + 1
# 	if i > 30:
# 		break
while i < 30:
	m = np.append(m,random.randint(1,10))
	i = i + 1
	if m[-1] == 7:
		break
print(m)
print(len(m))
print(sum(m))
print(np.mean(m))

#Reshape the array to a 5x5 matrix.  Loop through each element of the array.  If the element value is 5 or 8, print the element index.  Keep track of how many 5s and 8s there are with variable k.  Print k.  If the element value is a 1, print "You win!"
array5x5 = np.array([])
print(array5x5) #print []
for eachnumber in range(0,25):
	#np.append(array5x5,random.randint(1,10)) itself doesn't work.  Must set equal to the array array5x5.
	array5x5 = np.append(array5x5,random.randint(1,10))
print(array5x5)
array5x5 = array5x5.reshape(5,5)
print(array5x5)
#print(help(np.size))
print("look here 0 gives number of rows",(np.size(array5x5,0)))
print("look here 1 gives number of columns",(np.size(array5x5,1)))
print("look here gives number of elements",(np.size(array5x5)))
k = 0
for i in np.arange(np.size(array5x5,0)):
	for j in np.arange(np.size(array5x5,1)):
		if array5x5[i,j] == 5 or array5x5[i,j] == 8:
			print("Index:["+str(i)+","+str(j)+"]")
			k += 1
		elif array5x5[i,j] == 1:
			print("You win!")
print("k="+str(k))
print("\n")

#matrices a, matrices b and vectors x
"""
a = [1 2 3
     4 5 6
     7 8 9]

x = [1
     3
     4]

b = [-0.1 -0.2 -0.3
       3    10   2
       4     2  0.5]
"""
#Perform the following operations:  a. a*b element-wise multiplication.  b. a*b dot product multiplication.  c. a*b cross product multiplication.  d.  a*x dot product multiplication.  e.  a^-1*b dot product multiplication
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a) #print [[1 2 3]\n [4 5 6]\n [7 8 9]]
x = np.array([[1],[3],[4]])
print(x) #print [[1]\n [3]\n [4]]
b = np.array([[-0.1, -0.2, -0.3], [3, 10, 2], [4, 2, 0.5]])
print(b) #print [[ -0.1  -0.2  -0.3]\n [  3.   10.    2. ]\n [  4.    2.    0.5]]
#a. a*b element-wise multiplication.
print(a*b) #print [[ -0.1  -0.4  -0.9]\n [ 12.   50.   12. ]\n [ 28.   16.    4.5]]
#b. a*b dot product multiplication.
print(np.dot(a,b)) #print [[ 17.9  25.8   5.2]\n [ 38.6  61.2  11.8]\n [ 59.3  96.6  18.4]]
#c. a*b cross product multiplication.
print(np.cross(a,b)) #print [[  1.11022302e-16  -5.55111512e-17   0.00000000e+00]\n [ -5.00000000e+01   1.00000000e+01   2.50000000e+01]\n [ -1.40000000e+01   3.25000000e+01  -1.80000000e+01]]
#d.  a*x dot product multiplication.
print(np.dot(a,x)) #print [[19]\n [43]\n [67]]
#e.  a^-1*b dot product multiplication
# error message appeared
# from numpy.linalg import inv
# print(np.dot(inv(a),b))
