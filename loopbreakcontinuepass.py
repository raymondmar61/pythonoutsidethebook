#Sources http://www.tutorialspoint.com/python/python_loop_control.htm, https://stackoverflow.com/questions/3295938/else-clause-on-python-while-statement, https://www.tutorialspoint.com/python/python_while_loop.htm

#Break
#The break statement terminates the current loop and resumes execution at the next statement.  The most common use is when some external condition is triggered requiring a hasty exit from a loop. The break statement can be used in both while and for loops.
for letter in "python":
	if letter == "h":
		print("the h letter breaks the for loop")
		break
	print("Current letter %s" %letter)
print("For loop break completed")
print("\n")
counter = 1
while counter < 10:
	print("counter is %d" %counter)
	counter += 1
	if counter == 5:
		print("counter is",counter,"breaks the while loop")
		break
print("While loop break completed")
print("\n")
counter = 1
while counter < 10:
	print("counter is %d" %counter)
	counter += 1
	if counter == 5:
		print("counter is",counter,"breaks the while loop")
		break
	for letter in "python":
		if letter == "h":
			print("the h letter breaks the for loop")
			break
		print("Current letter %s" %letter)
print("While and for loops break completed")
print("\n")

#Continue
#The continue statement returns the control to the beginning of the while loop. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.
#The continue statement can be used in both while and for loops.
for letter in "python":
	if letter == "h":
		print("don't print the h letter.  Continue the for loop back at the top")
		continue
	print("Current letter %s" %letter)
print("For loop continue completed")
print("\n")
counter = 0
while counter < 10:
	counter += 1
	if counter == 5:
		print("don't print",counter,"continuing the while loop back at the top")
		continue
	print("counter is %d" %counter)
print("While loop continue completed")
print("\n")
counter = 0
while counter < 10:
	counter += 1
	if counter == 5:
		print("don't print",counter,"continuing the while loop back at the top")
		continue
	print("counter is %d" %counter)
	for letter in "python":
		if letter == "h":
			print("don't print the h letter.  Continue the for loop back at the top")
			continue
		print("Current letter %s" %letter)
print("While and for loops continue completed")
print("\n")

#Else for loop
#The else statement is executed when the loop has exhausted iterating the list.
for eachnumber in range(1,11):
	for nnumber in range(5,11):
		print(eachnumber,nnumber)
		if eachnumber == nnumber:
			print(eachnumber,nnumber,"are a match.  End the for loop nnumber",nnumber)
			break	
		print(eachnumber,nnumber,"is the last number in for loop eachnumber with the for loop nnumber.  There is no match for eachnumber and nnumber",nnumber,"continue for loop")
print("\n")
for eachnumber in range(1,11):
	for nnumber in range(5,11):
		print(eachnumber,nnumber)
		if eachnumber == nnumber:
			print(eachnumber,nnumber,"are a match.  End the for loop nnumber",nnumber)
			break		
	else:
		print(eachnumber,nnumber,"is the last number in for loop eachnumber with the for loop nnumber.  There is no match for eachnumber and nnumber",nnumber,"else")
print("\n")

#Else while loop
#If the else statement is used with a while loop, the else statement is executed when the condition becomes false.  If you break out of the loop or if an exception is raised, the else clause is not executed.
counterout = 1
while counterout < 10:
	print(counterout,"out")
	counterin = 1
	while counterin < 5:
		print(counterin,"in")
		counterin += 1
	counterout += 1
print("We're done.  I don't need the else: statement.")

n = 5
while n != 0:
	print(n)
	n-=1
else:
	print("What the heck.  I don't need the else: statement.")
print("\n")

n = 5
while n != 0:
	print(n)
	n-=1
print("What the heck.  I don't need the else: statement here, too.")
print("\n")

x = 1
while x < 10:
	print("x=",x)
	if x == 6:
		print("x while loop pretend something went wrong x=6.") 
		break
	x += 1
	print("Did I succeed?")
print("\n")

#If I enter a 6, the if statement is executed.  If I enter a 10 or greater, the else statement did I succeed statement is executed.
x2 = 1
while x2 < 10:
	print("x=",x2)
	if x2 == 6:
		print("x2 while loop pretend something went wrong typed a 6.") 
		break
	x2 = int(input("Enter a number "))
else:
	print("Did I succeed?  Yes, you entered a number 10 or greater")
print("\n")

#pass
#The pass statement is used when a statement is required syntactically but you do not want any command or code to execute.
#The pass statement is a null operation; nothing happens when it executes.  The pass is also useful in places where your code will eventually go, but has not been written yet.
for letter in "Python":
	if letter == "h":
		pass
		print("pass") #No executed statement or code if the value of letter is 'h'.  statement is helpful when you have created a code block but it is no longer required.
	print("Current letter pass:",letter)