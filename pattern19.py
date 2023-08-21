str = 'Abhishek'
n =len(str)



# Z like pattern 



for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == (n-i)-1 :
            print(str[j] ,end=" ")
        else:
            print(" " , end= " ")
    print()

    