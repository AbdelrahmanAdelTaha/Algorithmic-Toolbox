def MoneyChange(num):
    # min_number_of_coins = 0

    # if num == 1:
    #     min_number_of_coins = 1
    # else:

    #     while (num > 0):
    #         if num > 10:
    #             num = num - 10
    #             min_number_of_coins += 1
    #         elif num > 5:
    #             num = num - 5
    #             min_number_of_coins += 1
    #         else:
    #             num = num - 1
    #             min_number_of_coins += 1

    # return min_number_of_coins
    b = int(num/10)
    f = num % 10
    if f >= 5:
        b += 1
        c = f - 5
        b = b + c
    else:
        b = b + f

    return b


num = int(input())

x = MoneyChange(num)
print(x)
