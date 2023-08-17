def lcs(str, m, n):
    revstr = str[::-1]
    print(revstr)
    L = [[None]*(n+1) for i in range(m+1)]
 
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif str[i-1] == revstr[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m][n]

a = 'abdadc'
print(lcs(a, len(a),len(a)))