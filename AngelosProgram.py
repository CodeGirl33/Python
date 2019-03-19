

#count coins of each type

from collections import defaultdict

def count_coins(amount, coin, counter):
	while(amount >= coin):
		counter += 1
		amount = amount - coin
	return amount, counter
	
def main():
	coins = [50, 20, 10, 1]
	counters =[0] * len(coins)
	by_coin = defaultdict(int)
	amount = input("Enter amount in Pounds: ")
	#Convert Pounds to Pence
	amount = float(amount) * 100
	for coin, counter in zip(coins, counters):
		amount, counter = count_coins(amount, coin, counter)
		by_coin[coin] = counter
	print("FiftyPence:{0:d}, TwentyPence:{1:d}, TenPence:{2:d}, and Pennies:{3:d}.".format(*by_coin.values()))
	print("Total number of coins owed:  {0:d}.".format(sum(by_coin.values())))
	
if __name__ == "__main__":
	main()
	
