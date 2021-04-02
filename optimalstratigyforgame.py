#F(i, j) represents the maximum value the user
#can collect from i'th coin to j'th coin
#F(i, j) = Max(Vi + min(F(i+2, j), F(i+1, j-1) ), 
#              Vj + min(F(i+1, j-1), F(i, j-2) ))
#As user wants to maximise the number of coins. 
#Base Cases
#    F(i, j) = Vi           If j == i
#    F(i, j) = max(Vi, Vj)  If j == i + 1.
def optimalStrategyOfGame(arr, i, j , dp):
    if i + 1 == j:#when array size is one the simply choose one from the arr
        return max(arr[i], arr[j])
    if dp[i][j] != -1:#if the point is already visited
        return dp[i][j]
    dp[i][j] = max(arr[i] + min(optimalStrategyOfGame(arr, i+2, j, dp), optimalStrategyOfGame(arr, i+1, j-1, dp)), arr[j] + min(optimalStrategyOfGame(arr, i+1, j-1, dp), optimalStrategyOfGame(arr, i, j-2, dp)))
    return dp[i][j]
arr1 = [ 8, 15, 3, 7 ]
n = len(arr1)
dp = [[-1 for i in range(n)]for i in range(n)]
print(optimalStrategyOfGame(arr1, 0, n-1, dp))
  
arr2 = [ 2, 2, 2, 2 ]
n = len(arr2)
dp = [[-1 for i in range(n)]for i in range(n)]
print(optimalStrategyOfGame(arr2, 0, n-1, dp))
  
arr3 = [ 20, 30, 2, 2, 2, 10]
n = len(arr3)
dp = [[-1 for i in range(n)]for i in range(n)]
print(optimalStrategyOfGame(arr3, 0, n-1, dp))
