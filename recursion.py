#Source codecademyalllessons.py
"""
RM:  is this recursion.  No need for break statement in if statements.
def clinic(n):
	print("Today's number is",n)
	if n == 50:
		print("Number 50")
		break  <-- error message appears
	elif n == 10:
		print("Number 10")
	elif n == 0:
		print("We're done",n)		
	else:
		print("Let's subtract 1")
		clinic(n-1)
clinic(55)
"""
#3 Conditionals and Control Flow
def clinic(n):
	print("Today's number is",n)
	if n == 50:
		print("Number 50")
	elif n == 10:
		print("Number 10")
	elif n == 0:
		print("We're done",n)		
	else:
		print("Let's subtract 1")
		clinic(n-1)
clinic(55)  #clinic(55) function stopped at Number 50.  Today's number is 55\n Let's subtract 1\n Toda's number is 54\n Let's subtract 1\n . . . Today's number is 50\n Number 50

#3 Conditionals and Control Flow
def clinic(n):
	print("Today's number is",n)
	if n == 50:
		print("Number 50")
	elif n == 10:
		print("Number 10")
	elif n == 0:
		print("We're done",n)		
	else:
		print("Let's subtract 1")
		clinic(n-1)
clinic(40)  #clinic(40) function stopped at Number 10.  Today's number is 40\n Let's subtract 1\n Toda's number is 39\n Let's subtract 1\n . . . Today's number is 10\n Number 10