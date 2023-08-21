str = 'Chetan'
n = len(str)



# X like pattern 




for i in range(n):
    for j in range(n):
        if i == j or j == (n - i) - 1:
            print(str[j], end=" ")
        else:
            print(" ", end=" ")
    print()