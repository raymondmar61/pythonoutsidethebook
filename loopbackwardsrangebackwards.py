#Loop Backwards or Range Count Backwards
#https://stackoverflow.com/questions/3476732/how-to-loop-backwards-in-python
for number in range(10,0,-1):
	print(number) #print 10 9 8 . .  3 2 1 each letter a separate line
for x in reversed("abcxyz"):
	print(x) #print zyxcba each letter a separate line.


letters = "abcxyz"
print(letters[::-1]) #print zyxcba
print("".join(reversed(letters))) #print zyxcba
def reversetext(text):
	result = ""
	for i in range(len(text)-1,0,-1):
		result = result + text[i]
	return result
print(reversetext(letters)) #print zyxcba

def reverse(text):
	reversed = ''
	for i in range(len(text)-1, -1, -1):
		reversed += text[i]
	return reversed
print("reverse({}): {}".format("abcd", reverse("abcd"))) #print reverse(abcd): dcba