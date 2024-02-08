numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    else:
        numbers.append(int(user_input))

numbers.sort(reverse=True)
greatest_numbers = numbers[:5]

print("The five greatest numbers are:")
for number in greatest_numbers:
    print(number)