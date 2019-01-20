#https://stackoverflow.com/questions/3505831/in-python-how-do-i-convert-a-single-digit-number-into-a-double-digits-string
for i in range(9,0,-1):
	print("{0:0=2d} single digit numbers printed double digits or with a zero in front".format(i))
a = ["%02d" % x for x in range(0,10)]
print(a) #print ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']

#https://stackoverflow.com/questions/134934/display-number-with-leading-zeros
print("{:02d}".format(1)) #print 01
for i in range(9,-1,-1):
	print("{:02d}".format(i)) #print 09\n 08\n 07\n 06\n 05\n 04\n 03\n 02\n 01\n 00
#For Python 3.6+ the same behavior can be achieved with f-strings:
print(f"{1:02d}") #print 01

print(str(1).zfill(2)) #print 01
print(str(10).zfill(2)) #print 10
print(str(100).zfill(2)) #print 100
print('{:02}'.format(1)) #print 01
print('{:02}'.format(10)) #print 10
print('{:02}'.format(100)) #print 100

a, b, c = 1, 10, 100
for val in [a, b, c]:
    print(f'{val:02}') #print 01\n 10\n 100

x = [1, 10, 100]
for i in x:
    print('%02d' % i) #print 01\n 10\n 100