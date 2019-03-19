print("""You enter a dark room with two doors. Do you want to enter
	door No 1 or door No 2?""")

door = input("> ")

if door == "1":
	print("there is a giant bear there eating a cake")
	print("what do you do?")
	print("1. take the cake")
	print("2. Scream at the bear")

	bear = input("> ")

	if bear == "1":
		print("The bear ate your face off. Good job!")
	elif bear == "2":
		print("The bear eats your legs. Good job!")
	else:
		print(f"Well, doing {bear} is probably better")
		print("Bear runs aaway")


elif door == "2":
	print("You stare into the abyss")
	print("1. Blueberries")
	print("2. Yallow jacket")
	print("3. understanding melodies")

	insanity = input("> ")

	if insanity == "1":
		print("Your body survives")
		print("Good job")
	else:
		print("You stumble across and fall on a knife and die")