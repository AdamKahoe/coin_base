# Generate Coin Change
# Change is inevitable (especially when breaking a twenty).
# Make generateCoinChange(cents). Accept a number of American cents,
# compute and print how to represent that amount with the smallest number of coins.
# Common American coins are pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents).

# Example output, given (94):

# change = 20 - input

# from tkinter import Variable


# print(coinchange(67))

# def generateCoinChange(cents)

# c=int(input('Please enter an amount between 0-99:'))
# print(c//25, "quarters")
# c = c%25
# print(c//10, "dimes")
# c = c%10
# print(c//5, "nickles")
# c = c%5
# print(c//1, "pennies")

# print(coinchange(67))

# amount = input("Enter the amount of change owed: ")
# amount = int(amount)

# coins = [25, 10, 5, 1]
# results = []

# for coin in coins:
#     results.append(amount // coin) # The // sign is used to avoid fractions

# print("Quarters: {}".format(results[0]))
# print("Dimes: {}".format(results[1]))
# print("Nickels: {}".format(results[2]))
# print("Pennies: {}".format(results[3]))

from tkinter import Variable


def coin_change(amount):
    quarters = 0
    dimes = 0
    pennies = 0
    nickels = 0

    while amount >= 25:
        quarters += 1
        amount -= 25
    while amount >= 10:
        dimes += 1
        amount -= 10
    while amount >= 5:
        nickels += 1
        amount -= 5
    pennies = amount

    return(f'Quarters: {quarters}, Dimes: {dimes}, Nickels: {nickels}, Pennies: {pennies}')

print(coin_change(67))