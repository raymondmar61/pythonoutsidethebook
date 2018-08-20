def checkifprime(n): #n must be greater than one
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	i = 3
	while i * i <= n:
		if n % i == 0:
			return False
		i += 2
	return True

def isprime(n):
	if n == 1:
		return False #1 is not a prime number
	for d in range(2, n):
		if n % d == 0:
			return False
	return True

import time
startime = time.time()

#n must be greater than one
primenumberlistcheckifprime=[]
for number in range(2,101):
	if checkifprime(number) == True:
		primenumberlistcheckifprime.append(number)
print(primenumberlistcheckifprime)
endtime = time.time()
print((endtime-startime),"seconds") #print 0.00018835067749023438

startime2 = time.time()
primenumberlistisprime=[]
for number in range(1,101):
	if isprime(number) == True:
		primenumberlistisprime.append(number)
print(primenumberlistisprime)
endtime2 = time.time()
print((endtime2-startime2),"seconds") #print 0.00029540061950683594

#https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-34.php
def prime_eratosthenes(n):
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            print (i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)
print(prime_eratosthenes(100))

#soufianekiller
def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n<2:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True

#rtng
def is_prime(a):
    if a == 1:
        return False
    for b in range(2, round(a ** 0.5) + 1):
        if a % b == 0:
            return False
    return True

from math import sqrt

#luisbenedict
from math import sqrt
def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        else:
            return True