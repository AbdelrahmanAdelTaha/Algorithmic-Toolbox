def MaxPairwiseProduct(length, arr):
    max = 0
    for i in range(length):
        if arr[max] < arr[i]:
            max = i
    max2 = 0
    for i in range(length):
        if (arr[i] < arr[max]) and (arr[max2] < arr[i]):
            max2 = i

    return arr[max], arr[max2]


length = int(input("please input the length of arr "))
arr = []
for i in range(length):
    x = input("please input a num ")
    if x.isdigit():
        x = int(x)
        arr.append(x)
    else:
        continue

print(MaxPairwiseProduct(length, arr))
