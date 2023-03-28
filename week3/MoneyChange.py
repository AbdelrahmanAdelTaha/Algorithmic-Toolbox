def MoneyChange(num):
    min_number_of_coins = 0

    if num == 1:
        min_number_of_coins = 1
    else:

        while (num > 0):
            if num > 10:
                num = num - 10
                min_number_of_coins += 1
            if num > 5:
                num = num - 5
                min_number_of_coins += 1
            else:
                num = num - 1
                min_number_of_coins += 1

    return min_number_of_coins


num = int(input())

x = MoneyChange(num)
print(x)
