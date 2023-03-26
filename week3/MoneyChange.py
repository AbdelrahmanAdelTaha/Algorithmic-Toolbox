num = int(input("please enter a number "))
min_number_of_coins = 0

if num == 1:
    min_number_of_coins = 1
else:
    while (num > 10):
        num = num - 10
        min_number_of_coins += 1

    while (num > 5):
        num = num - 5
        min_number_of_coins += 1

    while (num > 0):
        num = num - 1
        min_number_of_coins += 1


print(min_number_of_coins)
