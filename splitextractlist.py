ad = ("123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432,"
  "54 Holy Grail Street Niagara Town ZP 32908,3200 Main Rd. Bern AE 56210,1 Gordon St. Atlanta RE 13000,"
  "10 Pussy Cat Rd. Chicago EX 34342,10 Gordon St. Atlanta RE 13000,58 Gordon Road Atlanta RE 13000,"
  "22 Tokyo Av. Tedmondville SW 43098,674 Paris bd. Abbeville AA 45521,10 Surta Alley Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32908,320 Main Al. Bern AE 56210,14 Gordon Park Atlanta RE 13000,"
  "100 Pussy Cat Rd. Chicago EX 34342,2 Gordon St. Atlanta RE 13000,5 Gordon Road Atlanta RE 13000,"
  "2200 Tokyo Av. Tedmondville SW 43098,67 Paris St. Abbeville AA 45521,11 Surta Avenue Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32918,320 Main Al. Bern AE 56215,14 Gordon Park Atlanta RE 13200,"
  "100 Pussy Cat Rd. Chicago EX 34345,2 Gordon St. Atlanta RE 13222,5 Gordon Road Atlanta RE 13001,"
  "2200 Tokyo Av. Tedmondville SW 43198,67 Paris St. Abbeville AA 45522,11 Surta Avenue Goodville GG 30655,"
  "2222 Tokyo Av. Tedmondville SW 43198,670 Paris St. Abbeville AA 45522,114 Surta Avenue Goodville GG 30655,"
  "2 Holy Grail Street Niagara Town ZP 32908,3 Main Rd. Bern AE 56210,77 Gordon St. Atlanta RE 13000,786 High Street Pollocksville NY 5643")

def travelba(r, zipcode):
	streets = []
	nums = []
	#create a list of addresses
	addresses = r.split(',')
	for address in addresses:		
		#split each address to separate.  Extract and check state code and zip code match variable zipcode 
		if ' '.join(address.split()[-2:]) == zipcode:
			#Extract street name append to streets list
			streets.append(' '.join(address.split()[1:-2]))
			#Extract street number as a single string append to nums list using +=
			nums += address.split()[:1]
			print(nums) #print #['123']\n '123', '432']
	return '{}:{}/{}'.format(zipcode, ','.join(streets), ','.join(nums))
print(travelba(ad, "OH 43071")) #print OH 43071:Main Street St. Louisville,Main Long Road St. Louisville/123,432

#separate a tuple by comma creates a list
datuple = ("123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432,"
  "54 Holy Grail Street Niagara Town ZP 32908,3200 Main Rd. Bern AE 56210,1 Gordon St. Atlanta RE 13000,"
  "10 Pussy Cat Rd. Chicago EX 34342,10 Gordon St. Atlanta RE 13000,58 Gordon Road Atlanta RE 13000")
dasplit = datuple.split(",")
print(dasplit) #print ['123 Main Street St. Louisville OH 43071', '432 Main Long Road St. Louisville OH 43071', '786 High Street Pollocksville NY 56432', '54 Holy Grail Street Niagara Town ZP 32908', '3200 Main Rd. Bern AE 56210', '1 Gordon St. Atlanta RE 13000', '10 Pussy Cat Rd. Chicago EX 34342', '10 Gordon St. Atlanta RE 13000', '58 Gordon Road Atlanta RE 13000']

dastring = ["123 Main Street St. Louisville OH 43071","432 Main Long Road St. Louisville OH 43071","786 High Street Pollocksville NY 56432","54 Holy Grail Street Niagara Town ZP 32908","3200 Main Rd. Bern AE 56210","1 Gordon St. Atlanta RE 13000","10 Pussy Cat Rd. Chicago EX 34342","10 Gordon St. Atlanta RE 13000","58 Gordon Road Atlanta RE 13000"]
#RM, no need to split because a list the contents are already split.
#dasplit = dastring.split(",")
#print(dasplit) #AttributeError: 'list' object has no attribute 'split'
dastring = ["123 Main Street St. Louisville OH 43071","432 Main Long Road St. Louisville OH 43071"]
for eachdastring in dastring:
	print(eachdastring.split())
	print(eachdastring.split()[-2:])
	print(" ".join(eachdastring.split()[-2:]))
	print(eachdastring.split()[1:4])
	print(" ".join(eachdastring.split()[1:4]))
"""
['123', 'Main', 'Street', 'St.', 'Louisville', 'OH', '43071']
['OH', '43071']
OH 43071
['Main', 'Street', 'St.']
Main Street St.
['432', 'Main', 'Long', 'Road', 'St.', 'Louisville', 'OH', '43071']
['OH', '43071']
OH 43071
['Main', 'Long', 'Road']
Main Long Road
"""

numbers = [123, 432, 789, 456, 321]
finalnumbers = []
finalnumbersstring = []
for eachnumbers in numbers:
	finalnumbers.append(eachnumbers)
	finalnumbersstring.append(str(eachnumbers))	
print(finalnumbers) #print [123, 432, 789, 456, 321]
print(finalnumbersstring) #print ['123', '432', '789', '456', '321']
print("numberslist is {}".format(finalnumbers)) #print numberslist is [123, 432, 789, 456, 321]
print("numberslist is {}".format(", ".join(finalnumbersstring))) #print numberslist is 123, 432, 789, 456, 321

lookaddresses = ["2 Holy Grail Street Niagara Town ZP 32908","3 Main Rd. Bern AE 56210","77 Gordon St. Atlanta RE 13000","786 High Street Pollocksville NY 5643"]
zipcodes = []
for eachlookaddresses in lookaddresses:
	print(eachlookaddresses.split()[-1]) #printed the numbers 32908, 56210, 13000, 5643
	print(type(eachlookaddresses.split()[-1])) #print <class 'str'>
	zipcodes.append(eachlookaddresses.split()[-1])
print("Your zipcodes are {}".format(", ".join(zipcodes))) #print Your zipcodes are 32908, 56210, 13000, 5643






