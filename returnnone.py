#https://stackoverflow.com/questions/15300550/return-return-none-and-no-return-at-all

def functionone():
	#print("return none")
	#print("Use when function returns a value for later use")
	return None
def functiontwo():
	#print("return")
	return
def functionthree():
	print("no return")
print(functionone()) #print None
print(functiontwo()) #print None
functionthree() #print no return
print(functionthree()) #print no return\n None
#basically, they're all the same.