#idea is to incude the partiular weight or not 
#formaula in dp table to calculate the optimal weith at a particular dp[i][w] = max(v[i-1][w], v[i-1][w-weight[i-1]] + profit[i])
# i is row which represents the weight of a particlar bag
# w is comumn which represents the maxmimim weight
val = [96, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
t = [[-1 for i in range(W+1)]for j in range(n+1)]
def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:#if it is alrady calculated
        return t[n][W]
    #choice to include or not
    if wt[n-1] <= W:
        t[n][W] = max(val[n-1] + knapsack(wt, val, W - wt[n-1], n-1),knapsack(wt, val, W, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W, n-1)
        return t[n][W]
print(knapsack(wt, val, W, n))