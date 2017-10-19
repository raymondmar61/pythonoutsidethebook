print(help(max))

def sumdigit(num):
	sum = 0
	print("number entered",num)
	while(num):
		sum = sum + (num%10)
		print("sum",sum)
		num = int(num/10)
		print("num",num)
	print("\n")
	return sum
num = [15,300,2700,821,52,10,6]
print("Maximum is:",max(num,key=sumdigit)) #print Maximum is: 821

num1 = [15,300,2700,821,9876854]
num2 = [12,2]
num3 = [24,567,78]
print(max(num1,num2,num3,key=len)) #print [15, 300, 2700, 821, 987654]