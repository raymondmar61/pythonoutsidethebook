#Iterate at least two lists at once. Use the zip function  zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
# lista = [3, 9, 17, 15, 19]
# listb = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
# for eachlista, eachlistb in zip(lista, listb):
# 	print(eachlista)
# 	print(eachlistb)
# 	print(eachlista, eachlistb)

#enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop, index will be one greater, and item will be the next item in the sequence. It's very similar to using a normal for loop with a list, except this gives us an easy way to count how many items we've seen so far.
choices = ["pizza","pasta","salad","nachos"]
print("Your choices are: ")
for index, eachchoices in enumerate(choices):
	print(index+1,eachchoices) #eachchoices should start at index 1.  #print 1 pizza\n 2 pasta\n 3 salad\n 4 machos

fruits = ['banana', 'apple', 'orange', 'pear', 'grape']
for eachfruits in fruits:
	if eachfruits == "tomato":
		print(eachfruits+" is not a fruit.  It actually is a fruit")
		break
	else:
		print(eachfruits)
else:
	print("A fine selection of fruits!")  #not printed because tomato broke the for eachfruits in fruits

fruits = ['banana', 'apple', 'tomato', 'orange', 'pear', 'grape']
for eachfruits in fruits:
	if eachfruits == "tomato":
		print(eachfruits+" is not a fruit.  It actually is a fruit")
		break
	else:
		print(eachfruits)
print("A fine selection of fruits!")  #printed because it's the next line after the for eachfruits in fruits loop

integerdecimal = 7.0
print(type(integerdecimal)) #print <class 'float'>
integerseven = 7
print(type(integerseven)) #print <class 'int'>
integerseven = integerseven + 0.0
print(integerseven) #print 7.0
print(type(integerseven)) #print <class 'float'>
