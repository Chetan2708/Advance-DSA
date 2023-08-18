str = "Abhishek"
n = len(str)

for i in range(1, n+1):
    if i <= n/2+1:
        for k in range(i-1):
            print(" ", end="")
    else:
        for k in range(n-(i-1)):
            print(" ", end="")
    print(str[i-1], end="")
    if (i <= n/2+1):
        for j in range(n-2*(i-1)):
            print(" ", end="")
    else:
        for j in range(2*(i-int(n/2)-1)):
            print(" ", end="")
    print(str[i-1])
