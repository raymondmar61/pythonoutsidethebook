#How to easily convert a list to a string for display
#https://www.decalage.info/en/python/print_list

mylist = ["spam","ham","eggs"]
print(", ".join(mylist)) #print spam, ham, eggs
print("\n".join(mylist)) #print spam\n ham\n eggs
print(" is from the cat in the hat\n".join(mylist)) #print spam is from the cat in the hat\n ham is from the cat in the hat\n eggs

#to obtain a comma-separated string
integerslist = [80, 443, 8080, 8081]
print(integerslist) #print [80, 443, 8080, 8081]
print(str(integerslist).strip("[]")) #print 80, 443, 8080, 8081
print(str(integerslist)[1:-1]) #print 80, 443, 8080, 8081
whatisthis = str(integerslist).strip("[]")
print(type(whatisthis)) #print string
print(whatisthis) #print 80, 443, 8080, 8081
print("\n")

#you may use map() to convert each item in the list to a string, and then join them
integerslist = [80, 443, 8080, 8081]
print(", ".join(map(str, integerslist))) #print 80, 443, 8080, 8081
print("\n".join(map(str, integerslist))) #print 80\n 443\n 8080\n 8081