def every_two(x):
	return x+2
	
nums = [0,1,2,3,4,5,6,7,8,9]
result = list(map(every_two, nums))
print(result)

