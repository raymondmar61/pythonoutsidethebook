# counter = 1
# for a in range(1,6):
# 	print(counter,"a in a for loop",a)
# 	counter +=1
# 	for b in range(1,6):
# 		print(counter,"a in b for loop "+str(a)+". b in b for loop",b)
# 		counter +=1

# counter = 1
# for a in range(1,6):
# 	print(counter,"a in a for loop",a)
# 	#print(counter,"a in a for loop "+str(a)+". b in a for loop",b,"sum is",(a+b)) #NameError: name 'b' is not defined
# 	#print(b) #NameError: name 'b' is not defined
# 	counter +=1
# 	for b in range(1,6):
# 		print(counter,"a in b for loop "+str(a)+". b in b for loop",b,"sum is",(a+b))
# 		if a+b >= 5:
# 			break #ends for loop b when a+b>=5 is True
# 		counter +=1

# counter = 1
# for a in range(1,6):
# 	print(counter,"a in a for loop",a)
# 	counter +=1
# 	for b in range(1,6):
# 		if a+b >= 5:
# 			continue #continues for loop b ignoring the rest of the for loop b code below
# 		print(counter,"a in b for loop "+str(a)+". b in b for loop",b,"sum is",(a+b))
# 		counter +=1

# counter = 1
# for a in range(1,6):
# 	print(counter,"a in a for loop",a)
# 	counter +=1
# 	for b in range(1,6):
# 		print(counter,"a in b for loop "+str(a)+". b in b for loop",b,"sum is",(a+b))
# 		if a+b >= 5:
# 			continue
# 		counter +=1 #continues for loop b ignoring the rest of the for loop b code below.  In this case, counter didn't add one at for b loop

# counter = 1
# for a in range(1,6):
# 	print(counter,"a in a for loop",a)
# 	counter +=1
# 	for b in range(1,6):
# 		print(counter,"a in b for loop "+str(a)+". b in b for loop",b,"sum is",(a+b))
# 		counter +=1
# 		for c in range(1,6):
# 			print(counter,"a in c for loop "+str(a)+". b in c for loop "+str(b)+". c in c for loop",c,"sum is",(a+b+c))
# 			counter +=1

# counter = 1
# for a in range(1,6):
# 	print(counter,"a in a for loop",a)
# 	counter +=1
# 	for b in range(1,6):
# 		print(counter,"a in b for loop "+str(a)+". b in b for loop",b,"sum is",(a+b))
# 		counter +=1
# 		for c in range(1,6):
# 			# if a+b+c >=5:
# 			# 	continue
# 			print(counter,"a in c for loop "+str(a)+". b in c for loop "+str(b)+". c in c for loop",c,"sum is",(a+b+c))
# 			counter +=1

counter = 1
for a in range(1,6):
	print(counter,"a in a for loop",a)
	counter +=1
	for b in range(1,6):
		if a+b >=5:
			continue
		print(counter,"a in b for loop "+str(a)+". b in b for loop",b,"sum is",(a+b))
		counter +=1
		for c in range(1,6):
			if a+b+c >=5:
				continue
			print(counter,"a in c for loop "+str(a)+". b in c for loop "+str(b)+". c in c for loop",c,"sum is",(a+b+c))
			counter +=1
			counter +=1
