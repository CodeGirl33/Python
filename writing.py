import sys
from sys import argv
script, filename = argv
print("We are going to erase " + sys.argv[1])
print("If you don't want that, hit ctrl-c.")
print("If you want to erase it, press enter.")
input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these three lines to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it!")
target.close()
