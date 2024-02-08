import random

def roll_dice(num_dice):
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        total += roll
    return total

num_dice = int(input("How many dice would you like to roll? "))
result = roll_dice(num_dice)
print("The sum of the dice rolls is:", result)