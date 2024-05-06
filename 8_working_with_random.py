from random import choice, randint, shuffle

lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Randomly select a number from the list
print(choice(lottery_numbers))

# Randomly select a number between 1 and 10
print(randint(1, 10))

# Shuffle the list
shuffle(lottery_numbers)
print(lottery_numbers)
