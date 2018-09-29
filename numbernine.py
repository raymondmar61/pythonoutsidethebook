#Ask Marilyn Parade Sep 23, 2018
#Multiply nine by any whole number except zero.  Then repeatedly add the digits of the answer until you get a single digit, and that digit will always be the number nine.
maxcounter = 0
n = 0
for n in range(8640,8651):
	productnine = n*9
	#convert the productnine into digits
	productninelist = list(str(productnine))
	productninelist = list(map(int,(productninelist)))	
	isitanine = 0
	counter = 0
	#while loop add the productnine digits to get the single digit 9
	while True:
		counter += 1
		isitanine = sum(productninelist)
		if isitanine != 9:
			print(n, productninelist, counter)
			productninelist = list(str(isitanine))
			productninelist = list(map(int,(productninelist)))
		if isitanine == 9:			
			print(n, productninelist, counter)
			if counter > maxcounter:
				maxcounter = counter
				maxcountern = n
			break
print(maxcountern,maxcounter)


	
