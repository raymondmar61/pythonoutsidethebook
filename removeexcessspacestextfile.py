#open primenumbers1000000.txt file to remove excess spaces three spaces and two spaces
with open("primenumbers1000000.txt","r") as fileobject:	
	contents = fileobject.read()
	contents = contents.replace("   "," ")
	contents = contents.replace("  "," ")
	primenumbers = list((map(int,contents.split(" "))))
cdv = str(primenumbers).strip("[]")
print(cdv)

#write fixed primenumbers1000000.txt to new file primenumbers1000000fixed.txt
filename = "primenumbers1000000fixed.txt"
with open (filename, "w") as fileobject:
	fileobject.write(cdv)