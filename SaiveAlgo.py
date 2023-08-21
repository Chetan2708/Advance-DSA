
n = 75 
arr = [True]*(n+1)
p  = 2


while p*p <= n:
    if arr[p] :
        for i in range(p*p , n+1 , p ):
            arr[i]= False
    p = p+1

for i in range(2, n+1):
    if arr[i]:
        print('Prime number ---->',i)
    
