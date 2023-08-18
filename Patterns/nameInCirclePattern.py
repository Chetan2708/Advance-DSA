str = "Radhika"
n = len(str)

for i in range(1, n+1):
    if (i < 3):
        for space in range(3-i):
            print(" ", end="")
    elif (i > n-2):
        for space in range(i-int(n/2)-1):
            print(" ", end="")
    print("A", end="")
    if (i == int(n/2)+1 or i == int(n/2) or i == int(n/2)+2):
        for space in range(int(n/2)+1):
            print(" ", end="")
    else:
        if (i < n/2):
            for space in range(2*(i-1)):
                print(" ", end="")
        else:
            for space in range(n-i+1):
                print(" ", end="")
    print("A")
