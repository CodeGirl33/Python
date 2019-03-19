#list comprehension powers

pow2 = [2 ** x for x in range(10)]
print(pow2)

#equivqlent to

pow2 = []
for x in range(10):
	pow2.append(x**2)
		
		
#the key-value pair of dictionaries

Shelley ={'username': 'grumpy', 'socialm': 'Facebook', 'Online': True, 'FriendsNo':542}
Yvette = {'username': 'AnnaUK', 'socialm': 'Instagram', 'Online': False, 'Followers': 1345}
for common_key in Shelley.keys() & Yvette.keys():
	print(Shelley[common_key], Yvette[common_key])
print(Shelley.items())
print(Yvette.items()) 

for key, value in Shelley.items():
	print(key, "is the key for value", value)
	
#adding to dictionaries with the DICT['KEY'] = 'VALUE' synthax

usernames ={'Shelley':'grumpy', 'Yvette':'AnnaUK'}
usernames['MarkD']='DarkM'
print(usernames)
