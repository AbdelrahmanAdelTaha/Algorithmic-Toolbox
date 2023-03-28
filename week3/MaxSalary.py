def GreatestNumber(arr):
    if len(arr) == 1:
        return arr[0]

    else:
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j]+arr[i] > arr[i]+arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

        str1 = ''.join(arr)
        return str1


number_of_digits = int(input('please enter a number digits : '))
arr = []
for i in range(number_of_digits):
    x = input()
    arr.append(x)
# arr = list(number)
Greatestnum = GreatestNumber(arr)

print(Greatestnum)
