#https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
a = []
if not a:  #recommended in Programing Recommendations section of PEP 8
	print("List is empty") #print List is empty
if a:
	print("List is full")
b = ["occupied"]
if b:  #recommended in Programing Recommendations section of PEP 8
	print("List is full") #print List is full
else:
	print("List is emtpy")

a = []
b = ["occupied"]
if len(a) == 0:
	print("List is empty 0") #print List is empty 0
if len(b) == 0:
	print("List is empty 0")
else:
	print("List is full 1") #print List is full 1

a = []
if a == []:  #don't do this
	print("a is an empty list") #print a is an empty list

a = []
print(bool(a)) #print False
b = ["occupied"]
print(bool(b)) #print True
if (all(bool(b) for eachb in b)):
	print("love") #print love
if (any(bool(b) for eachb in b)):
	print("love") #print love
# williamfiset any and all
# print(any([True, False, 0, 1 < 0])) #print True
# print(any([False])) #print False
# print(any([])) #print False
# print(all([True, True])) #print True
# print(all([True, 34<5])) #print False

#https://stackoverflow.com/questions/21191259/returning-boolean-if-set-is-empty
numberset = {1, 3, 5, 7}
print(type(numberset)) #print <class 'set'>
print(bool(numberset)) #print True
if numberset:
	print("There are numbers") #print There are numbers
blanknumberset = set()
print(type(blanknumberset)) #print <class 'set'>
print(bool(blanknumberset)) #print False
if not blanknumberset:
	print("There are no numbers") #print There are no numbers
#error message
# blanknumbersetfake = {}
# print(type(blanknumbrsetfake)) #print name 'blanknumbrsetfake' is not defined

#https://www.pythoncentral.io/how-to-check-if-a-list-tuple-or-dictionary-is-empty-in-python/
#function check if empty
def isempty(anystructure):
	if not anystructure:
		print("Structure is empty.")
		return True
	elif anystructure:
		print("Structure is full.")
		return False
	else:
		print("I don't know.")
		return False
dictionarycheck = {}
listcheck = []
setcheck = set()
stringcheck = ""
tuplecheck = ()
isempty(dictionarycheck) #print Structure is empty
isempty(listcheck) #print Structure is empty
isempty(setcheck) #print Structure is empty
isempty(stringcheck) #print Structure is empty
isempty(tuplecheck) #print Structure is empty
dictionarycheck = {"Raymond": 5}
listcheck = ["Posey","Bumgarner"]
setcheck = set([5, 4, 3, 2, 5])
stringcheck = "thequick"
tuplecheck = (7, 5)
isempty(dictionarycheck) #print Structure is full
isempty(listcheck) #print Structure is full
isempty(setcheck) #print Structure is full
isempty(stringcheck) #print Structure is full
isempty(tuplecheck) #print Structure is full

listempty = []
if len(listempty) == 0:
	print("Don't check lists this way") #print Don't check lists this way

#bonus while loop from ch7userinputandwhileloopstaketwo.py Python Crash Course
active = True
while active:
	message = input(prompt3)
	if message == 'quit':
		active = False
	else:
		print(message)
promptcities = "Please enter the name of a city you have visited:"
promptcities += "\n(Enter \"quit\" when you are finished.) "
while True:
	city = input(promptcities)
	if city == "quit":
		break
	else:
		print("Id love to go to " +city.title()+ "!")
#moving items from one list to another list
unconfirmedusers = ["Alice","Brian","Candace"]
confirmedusers = []
print(unconfirmedusers)
while unconfirmedusers: #while loop runs unconfirmedusers is not empty
	verifyinguser = unconfirmedusers.pop()
	print("Verifying user or moving unconfirmeduser to confirmeruser " +verifyinguser.title())
	confirmedusers.append(verifyinguser)
print(confirmedusers)
#Fill a dictionary with user input
responses = {}
pollingactive = True
while pollingactive:
	name = input("What is your name? ")
	mountain = input("Which mountain do you want to climb someday? ")
	responses[name] = mountain #store name and mountain in responses dictionary
	repeat = input("Do you want to enter another name? y or n ")
	if repeat == "n":
		pollingactive = False
print(responses)
for name, mountain in responses.items():
	print(name+ " wants to climb " +mountain)

#middle_name argument is optional with an empty default value
def getformattedname(firstname, lastname, middlename=""):
	if middlename: #Python interprets non-empty strings as True
		fullname = firstname+ " " +middlename+ " " +lastname
	else:
		fullname = firstname+ " " +lastname
	return fullname.title()
musician = getformattedname("jimi","hendrix")
print(musician) #print Jimi Hendrix