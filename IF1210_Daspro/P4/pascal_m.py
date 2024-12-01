# Input
n = int(input())
m = int(input())

# Proses
dp = [[0 for i in range(n)] for i in range(n+1)]
dp[0][0] = m

for i in range(n):
    for j in range(i+1):
        endd = "" if j == i else " "
        print(dp[i][j], end=endd) if dp[i][j] > 0 else 0
    print()
    for j in range(n):
        if j == 0:
            dp[i+1][j] = dp[i][j] 
        else:
            dp[i+1][j] = dp[i][j] + dp[i][j-1]