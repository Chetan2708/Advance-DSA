str = 'Chetan'
n = len(str)


# W like pattern 


for i in range(1, n+1):
    for k in range(1,  i+1):
        print(" ", end="")
    print(str[i-1], end="")
    for j in range(1, 2*(n-i)+1):
        print(" ", end="")
    print(str[i-1],end="")
    for f in range(4,  2*(i+1)+1):
        print(" ", end="")
    print(str[i-1],end="")
    for a in range(1, 2*(n-i)+1):
        print(" ", end="")
    print(str[i-1])
