num1 = int(input("Please Enter First Number "))
num2 = int(input("Please Enter Second Number "))

if (num1 % 2 != 0) and (num2 % 2 != 0):
    GCD = 1

if num2 > num1:
    temp = num2
    num2 = num1
    num1 = temp

# This is the faster algorithm

# A list for the first number - B list for the second number - Q list for the Quotient - R list for the Reminder
A = []
B = []
Q = []
R = []

A.append(num1)
B.append(num2)

while B[-1] != 0:
    Q.append(int(A[-1] / B[-1]))
    R.append(A[-1] - (B[-1]*Q[-1]))
    A.append(B[-1])
    B.append(R[-1])

GCD = A[-1]

print(GCD)


# This is slow algorithm

# GCD = 0
# for d in range(1, (num1+num2)):
#     if (num1 % d == 0) and (num2 % d == 0):
#         GCD = d


# print(GCD)
