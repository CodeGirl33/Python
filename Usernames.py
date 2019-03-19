#define userb=names dict

usernames = {'Shelley': 'grumpy', 'Yvette': 'AnnaUK'}

#Set up while loop to iterate

while True:
	print('Enter a name:')
	name = input() #assign to name variable
	
	if name in usernames:
		print(usernames[name] + "is the username of" + name)
	else:
		print("I do not have" + name + username, "what is it?")
# takes input of new username
	username = input()
  #assigns username to name key
	usernames[name] = username
  #provides feedback of update
	print("Data updated")
	print(usernames)
