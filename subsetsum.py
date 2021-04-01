def issubsetsum(s, n ,sums):
    subset = [[False for i in range(sums + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        subset[i][0] = True
    for i in range(1, sums + 1):
        subset[0][i] = False
    for i in range(1, n + 1):
        for j in range(1, sums + 1):
            if j < s[i-1]:
                subset[i][j] = subset[i-1][j]
            if j >= s[i-1]:
                subset[i][j] = (subset[i-1][j] or subset[i - 1][j-s[i-1]])
    return subset[n][sums]
s = [3, 34, 4, 12, 5, 2]
sums = 81
n = len(s)
if (issubsetsum(s, n, sums) == True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")