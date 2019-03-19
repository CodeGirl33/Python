from os import sys 
from sys import exit
from random import choice 
import time

#options_england = ['lbw', 'boundaries', 'SIX!', 'OUT!']
#options_india = ['dropped', 'caught', 'yorker', 'maiden']
# print("India lost the toss, and has been put into batting / fielding")
# print("""England have won the toss, you are the Captain and must choose 
# whether to bat or to field. Enter batting / fielding """)


def cricketODI():
	print("""It's England v India at Lord's. Choose who you play for. 
	Enter England / India """)

	squad = input('> ')
	
	
	if squad == "India":
		India_squad()
		
	elif squad == "England":
		England_squad()
		
	else:
		print("You must be an Ozzie!")
		
if __main__ == "__name__":
	cricketODI()
		

	
 		
 			
 			
# If batting, various possible options: boundaries, a six, OUT, run OUT, no run.
# If fielding, other options: Catch, dropped, yorker, wicket, lbw, a maidem.
# if a maiden, some sledging will occur.
# Score will be given.
# if out, commentators will comment. Choose who to hear: Boycott, Aggers.
# Disturbances: pidgeons on the pitch, Strickers, rain stop play - these as 
#unexpected random options. To continue press enter.
# Drinks, lunch, tea as random interruptions, to continue press enter.
