from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi, {user_name}, I am the {script} script.")
print("I would like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}? ")
lives = input(prompt)

print("What computer do you have?")
computer = input(prompt)

print(f""" Alright, so you said {likes} about liking me, 
you live in {lives} and you have a {computer} computer. Nice!""")