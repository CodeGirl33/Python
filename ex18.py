def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
	print(f"arg1: {arg1}")

def print_none():
	print("I got nofink!")

print_two("giulia", "bollocks!")
print_one("cheppalle!")
print_none()