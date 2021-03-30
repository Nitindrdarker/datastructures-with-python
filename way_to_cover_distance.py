def main(dist):
    dp = [0]*(dist+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    if dist == 1 or dist == 0:
        dp[1]
    elif dist == 2:
        dp[2]
    else:
        for i in range(3, dist+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[dist]
print(main(4))