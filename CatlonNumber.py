# 1 1 2 5 14 42
def fun(n):
    l = [0]*(n+1)
    l[0] =1
    l[1] =1
    for i in range(2 , n+1):
        for j in range(i):
            l[i] += l[j] * l[i-j-1]

    return l[n] 


print(fun(4))