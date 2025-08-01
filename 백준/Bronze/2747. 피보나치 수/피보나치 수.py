def f(n) :
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    if n < 2:
        return dp[n]
    for i in range (2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

n = int(input())
print(f(n))