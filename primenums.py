def is_prime(num):
	num = input()
	for i in range(1, num):
		if num % i == 1:
			return False
			print("This not a prime number")
			
    elif num % i == 0:
      return True
		  print("This is a prime number")