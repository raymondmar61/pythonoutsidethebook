from random import randint
from math import sqrt, ceil, floor
computernumber = randint(1,1000000)
computernumbersquareroot = sqrt(computernumber)
print("What is the square root of",computernumber)
print("cheat",computernumbersquareroot)
userguesses = input("Enter two whole numbers to estimate the square root separated by a space ")
userguesses = userguesses.split(" ")
# print(userguesses)
# print(int(userguesses[0]))
# print(int(userguesses[1]))
if (int(userguesses[0]) <= computernumbersquareroot) and (int(userguesses[1]) >= computernumbersquareroot):
	print("Correct  The square root is",computernumbersquareroot)
else:
	print("Sorry.  The answers are",floor(computernumbersquareroot),"and",ceil(computernumbersquareroot),".")