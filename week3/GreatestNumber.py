def GreatestNumber(arr):
    arr2 = []
    max = 0
    while arr:
        for i in arr:
            i = int(i)
            if i > max:
                max = i
        arr2.append(max)
        arr.remove(str(max))
        max = 0

    str1 = ' '.join(map(str, arr2))
    return str1


number = input('please enter a number: ')
arr = list(number)
Greatestnum = GreatestNumber(arr)

print(Greatestnum)
