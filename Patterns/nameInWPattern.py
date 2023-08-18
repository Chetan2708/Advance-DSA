str = "Abhishek"
n = len(str)

for i in range(1, n+1):
    for space in range(i-1):
        print(" ", end="")
    print(str[i-1], end="")
    for space in range(2*(n-i)):
        print(" ", end="")
    print(str[i-1], end="")
    for space in range(2*(i-1)):
        print(" ", end="")
    print(str[i-1], end="")
    for space in range(2*(n-i)):
        print(" ", end="")
    print(str[i-1])
