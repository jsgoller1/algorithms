#!/usr/bin/python

def make_change(coins, amount):

  if min(coins) > amount:
    return 0
  elif min(coins) == amount:
    return 1

  ways = 0

  for coin in coins:
    while(amount > coin):
      ways += make_change(coins, amount - coin)
      amount -= coin

  return ways


if __name__ == '__main__':
  print(make_change([1, 5, 10], 15))
