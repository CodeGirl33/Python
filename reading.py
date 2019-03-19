import sys
from sys import argv
script, filename = argv

txt = open(filename)

print("This script is called: " + sys.argv[0])
print("Here's your filename " + sys.argv[1])
print(txt.read())

print("Type the filename again: ")
file_again = input("~~ ")

txt_again = open(file_again)

print(txt_again.read())
