from os import system
from random import choice
import time

options = ["It's a four!!!'", "What a yorker!", "OUT!!!", "You are at silly mid off", "My dear old thing, it's the end of the Over!'", "You could have hit that with a rhubarb stick!!"]

def Ashes():
    counter = 1
    while counter < 10:
        print("""You are at Lord's, choose a number from 1 to 6 to see in what role you play""")
        role = int(input('> '))
        if (role >= 1 and role <= len(options)):
            print(choice(options))
        else:
            print("You cannot count, go rub sugar on the ball!!")
        counter += 1
        time.sleep(1.5)
        system("clear")

if __name__ == "__main__":
    Ashes()
