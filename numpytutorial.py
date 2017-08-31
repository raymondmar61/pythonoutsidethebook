#YouTube channel codebasics.  numpy tutorial - introduction, numpy tutorial - basic array operations, numpy tutorial - slicingstacking arrays, indexing with boolean arrays
#numpy's most useful feature is n dimensions array object or ndarray.  numpy array uses less memory, faster, convenient to list.
#You [have] a file called numpy.py in your working directory which shadows the real numpy module. Rename that file and remove its numpy.pyc file.  In other words, don't name the python file nympy.py.  https://stackoverflow.com/questions/36530726/using-numpy-module-object-has-no-attribute-array

import numpy as np
# import time
# import sys
# size = 10000000
# l1 = range(size)
# l2 = range(size)
# a1=np.arange(size)
# a2=np.arange(size)
# #python list add numbers from two identical lists
# start=time.time()
# result = [(x+y) for x,y in zip(l1,l2)]
# print("python list took: ",(time.time()-start)*1000)
# #python array add numbers from two identical lists
# start=time.time()
# result = a1 + a2
# print("numpy took: ", (time.time()-start)*1000)

array1 = np.array([1,2,3])
print(array1.ndim) #print 1.  ndim is the array's dimensions.
print(array1.itemsize) #print 8.  itemsize is memorysize of array
print(array1.size) #print 3.  size is number of elements
print(array1.shape) #print (3,).  shape is dimensions
print(array1) #print [1 2 3]
print(array1[0]) #print 1
print(array1[1]) #print 2
a1 = np.arange(10) #arange stands for array range?
print(a1) #print list starting at 0 and ending at 9
a2 = np.arange(11,21)
print(a2) #print list starting at 11 and ending at 12
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1 + array2) #print [5, 7, 9]
print(array1 - array2) #print [-3, -3, -3]
print(array1 * array2) #print [ 4, 10, 18]
print(array1 / array2) #print [ 0.25, 0.4, 0.5 ]
print("\n")

list1 = [1,2,3]
list2 = [4,5,6]
print(list1 + list2) #print [1, 2, 3, 4, 5, 6]
#print(list1 - list2) #error message
fakearray = []
for eachlist1, eachlist2 in zip(list1,list2):
	print(eachlist1+eachlist2) #print 5\n 7\n 9
	fakearray.append(eachlist1+eachlist2)
print(fakearray) #print [5, 7, 9]
print("\n")

array3 = np.array([[1,2], [3,4], [5,6]])
print(array3.ndim) #print 2.  ndim is the array's dimensions.
print(array3.itemsize) #print 8.  itemsize is memorysize of array
print(array3.size) #print 6.  size is number of elements
print(array3.shape) #print (3,2).  shape is dimensions.  3 rows, 2 columns
print(array3.dtype) #print int64.  dtype is data type
print(array3[1][0]) #print 3
print("also works",array3[1,0]) #print 3
array3 = np.array([[1,2], [3,4], [5,6]], dtype=np.float64) #change data type
print(array3.itemsize) #print 8.  itemsize is memorysize of array
print(array3.dtype) #print float64.  dtype is data type
print(array3) #print [[ 1.  2.]\n [ 3.  4.]\n [ 5.  6.]]
array3 = np.array([[1,2], [3,4], [5,6]], dtype=complex) #change data type
print(array3) #print [[ 1.+0.j  2.+0.j]\n [ 3.+0.j  4.+0.j]\n [ 5.+0.j  6.+0.j]]
print("\n")

array0 = np.zeros( (3,4) )
print(array0) #print an array of 0. [[ 0.  0.  0.  0.]\n [ 0.  0.  0.  0.]\n [ 0.  0.  0.  0.]]
array1 = np.ones( (3,4) )
print(array1) #print an array of 1. [[ 1.  1.  1.  1.]\n [ 1.  1.  1.  1.]\n [ 1.  1.  1.  1.]]
print(np.arange(1,5)) #print [1 2 3 4]
print(np.arange(1,10,2)) #print [1 3 5 7 9]
print(np.linspace(1,5,10)) #print [ 1.          1.44444444  1.88888889  2.33333333  2.77777778  3.22222222  3.66666667  4.11111111  4.55555556  5.        ] generate ten numbers between 1 and 5 equally spaced linear spaced
print(np.linspace(1,10,19)) #print [  1.    1.5   2.    2.5   3.    3.5   4.    4.5   5.    5.5   6.    6.5   7.    7.5   8.    8.5   9.    9.5  10. ]
print(list(np.linspace(1,10,19))) #print [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
print("\n")

array3 = np.array([[1,2], [3,4], [5,6]])
print(array3.shape) #print (3,2).  shape is dimensions.  3 rows, 2 columns
array3 = array3.reshape(2,3) #change dimensions
print(array3) #print [[1 2 3]\n [4 5 6]]
print(array3.shape) #print (2,3).  shape is dimensions.  2 rows, 3 columns
array3 = array3.reshape(6,1) #change dimensions
print(array3) #print [[1]\n [2]\n [3]\n [4]\n\n [5]\n [6]]
print(array3.shape) #print (6,1).  shape is dimensions.  6 rows, 1 column
array3 = array3.ravel() #flatten an array to one dimension
print(array3) #print [1 2 3 4 5 6]
print(array3.shape) #print (6,).  shape is dimensions.  6 rows, 1 column
array3 = np.array([[1,2], [3,4], [5,6]])
print(array3.min()) #print 1
print(array3.max()) #print 6
print(array3.sum()) #print 21
print(array3.sum(axis = 0)) #print [ 9 12] or 1+3+5 2+4+6
print(array3.sum(axis = 1)) #print [ 3 7 11] or 1+2 3+4 5+6
print(np.sqrt(array3)) #print [[ 1.          1.41421356]\n [ 1.73205081  2.        ]\n [ 2.23606798  2.44948974]]
print(np.std(array3)) #print 1.70782512766
array4 = np.array([[1,2], [3,4]])
array5 = np.array([[5,6], [7,8]])
print(array4.dot(array5)) #print [[ 19  22]\n [43 50]]
print("\n")

array6 = np.array([6,7,8])
print(array6[0:2]) #print [6 7]
print(array6[-1]) #print 8
array7 = np.array([[6,7,8], [1,2,3], [9,3,2]])
print(array7[1][2]) #print 3
print(array7[1,2]) #print 3
print(array7[0:2,2]) #print [8 3] take array 0 and array 1's second indexes
print(array7[-1]) #print [9 3 2]
print(array7[-1,0:2]) #print [9 3]
print(array7[:,1:3]) #print [[7 8]\n [2 3]\n [3 2]] take all arrays first indexes and second indexes
print(array7) #print [[6 7 8]\n [1 2 3]\n [9 3 2]]
for eacharray7 in array7:
	print(eacharray7) #print [6 7 8]\n [1 2 3]\n [9 3 2]
for eachentry in array7.flat:
	print(eachentry) #print each number in its own line starting with 6 and ending with 2
print("\n")

array8 = np.arange(6).reshape(3,2)
print(array8) #print [[0 1]\n [2 3]\n [4 5]]
array9 = np.arange(6,12).reshape(3,2)
print(array9) #print [[6 7]\n [8 9]\n [10 11]]
print(np.vstack((array8,array9))) #print [[ 0  1]\n [ 2  3]\n [ 4  5]\n [ 6  7]\n [ 8  9]\n [10 11]] #vertically stack vertical stack arrays
print(np.hstack((array8,array9))) #print[[ 0  1  6  7]\n [ 2  3  8  9]\n [ 4  5 10 11]] #horizontally stack horizontal stack arrays
print("\n")

array10 = np.arange(0,30).reshape(2,15)
print(array10) #print [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]\n [15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]]
print(np.hsplit(array10,3)) #print [array([[ 0,  1,  2,  3,  4], [15, 16, 17, 18, 19]]), array([[ 5,  6,  7,  8,  9], [20, 21, 22, 23, 24]]), array([[10, 11, 12, 13, 14], [25, 26, 27, 28, 29]])] divide array into three 
result = (np.hsplit(array10,3))
print(result[0]) #print [[ 0  1  2  3  4]\n [15 16 17 18 19]]
print(result[1]) #print [[ 5  6  7  8  9]\n [20 21 22 23 24]]
print(result[2]) #print [[10 11 12 13 14]\n [25 26 27 28 29]]
print(np.vsplit(array10,2)) #[array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]]), array([[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])]
result2 = (np.vsplit(array10,2))
print(result2[0]) #print [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]]
print(result2[1]) #print [[15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]]
print("\n")

array11 = np.arange(0,12).reshape(3,4)
print(array11) #print [[ 0  1  2  3]\n [ 4  5  6  7]\n [ 8  9 10 11]]
#print(np.arange(0,13).reshape(3,4)) #error ValueError: cannot reshape array of size 13 into shape (3,4)
b = array11 > 4
print(b) #print [[False False False False]\n [False  True  True  True]\n [ True  True  True  True]]
print(array11[b]) #print [ 5  6  7  8  9 10 11]
array11[b] = -1
print(array11) #print [[ 0  1  2  3]\n [ 4 -1 -1 -1]\n [-1 -1 -1 -1]]
print("\n")