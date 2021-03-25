def mainFunc(arr, l):
    dp = [1] * l
    for i in range(1, l):
        for j in range(i):
            if(arr[i] > arr[j]) and (dp[i] < dp[j]+1):#is condition is to save the highest dp value in the dp[i] so that it wont change after some  by smaller dp value that may come after highest dp value
                dp[i] = dp[j] + 1
            print(dp)
    return max(dp)
arr = [10, 22, 9, 33, 21, 50, 41, 60]
l = len(arr)
print(mainFunc(arr, l))
