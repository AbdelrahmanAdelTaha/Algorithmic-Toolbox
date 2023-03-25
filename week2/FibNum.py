def FibonacciNumber(num):
    pass


num = int(input("please input a number "))
arr = []
arr.append(0)
arr.append(1)

for i in range(2, num+1):
    arr.append(arr[i-1]+arr[i-2])

print(arr[-1])

# to get the last digit of fib number
print(int(arr[-1] % 10))
