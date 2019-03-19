x = int(input(""))
y = ""
while x>0:
	a = x%2
	y = y+str(a)
	x = x//2
	
print(y[::-1])

