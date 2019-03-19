from os import system
from random import choice

options = ["It's a four!!!'","What a yorker!", "OUT!!!", "You are at silly mid off", "My dear old thing, it's the end of the Over!'","You could have hit that with a rhubarb stick!!",]

def Ashes():
	
	print("""You are at Lord's, choose a number from 1 to 7 to see in what role you play""")
			
	role = input('> ')
		
	if role == "1":
		print(choice(options))
			
	elif role == "2":
		print(choice(options))
		
			
	elif role == "3":
		print(choice(options))
			
			
	elif role == "4":
		print(choice(options))
		
			
	elif role == "5":
		print(choice(options))
			
			
	elif role == "6":
		print(choice(options))
		
	
	else:
		print("You cannot count, go rub sugar on the ball!!")
			

system("clear")	
Ashes()