def sumOfDigits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def NeonReturn(n):
    square = n * n
    sum_digits = sumOfDigits(square)
    return sum_digits == n


for i in range(1, 100):
    if NeonReturn(i):
        print(i)
