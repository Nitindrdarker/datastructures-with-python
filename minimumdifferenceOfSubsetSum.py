#https://youtu.be/-GtpxG6l_Mc?t=1958
def findmin(arr, n):
    s = 0
    s = sum(arr)
    dp = [[None for i in range(s+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True#first column is zero sum is possible with any elememt
    for j in range(1, s + 1):
        dp[0][j] = False#no sum is possible with zero element
    for i in range(1, n+1):
        for j in range(1, s + 1):#https://youtu.be/BT_ACNC47Os?t=684
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j] = dp[i][j]|dp[i-1][j-arr[i-1]]
    diff = 99999
    for j in range(s//2, -1, -1):
        if dp[n][j] == True:
            diff = s - (2*j)
            break
    return diff

arr = [ 3, 1, 4, 2, 2, 1 ]
n = len(arr)
print("The minimum difference between "
      "2 sets is ", findmin(arr, n))
 