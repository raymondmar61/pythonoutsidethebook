salesreplist = ["Joe", "Jo", "Sioux", "Sue", "Mo", "Moe", "Jan", "Luong", "Chin", "Pham", "Phil", "Shelia", "Dawn", "Greg", "John", "Tina", "Christina"]
import itertools
#salesreplist all combinations sample size four
salesreplistfour = list(itertools.combinations(salesreplist,4))
print(salesreplistfour)
print(len(salesreplistfour)) #print 2380

#create text file salesreplistfour.txt and write the combinations to salesreplistfour.txt
saveFile = open("salesreplistfour.txt","w")
for eachsalesreplistfour in salesreplistfour:
	print((",".join(eachsalesreplistfour)))
	#separate the four salesreplist by a comma and each combination on its own line
	salesreplistfourstring = (",".join(eachsalesreplistfour)+"\n") 
	saveFile.write(salesreplistfourstring)
saveFile.close()