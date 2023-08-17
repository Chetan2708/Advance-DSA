def lcs (a , b ):
    m = len(a)
    n = len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]

    ans = 0 


    for i in range(1, len(a)+1): 
        for j in range(1, len(b)+1): 
            if a[i-1] == b[j -1]:  
                dp[i][j]=dp[i-1][j-1]+1
                ans = max(ans , dp[i][j])
            else:
                dp[i][j] = 0
    return ans

print(lcs('abcde' ,'abcfe'))
