def longestpath(matrix, cache, n, i, j):
    if (i<0 or i>= n or j<0 or j>= n):
        return 0
    if cache[i][j] != -1:
        return cache[i][j]
    m = 1
    longest = 0
    if j<n-1 < n and matrix[i][j]+1 == matrix[i][j+1]:
        longest = longestpath(matrix, cache, n, i, j+1)
        m = max(longest, m)
    if j>0 and matrix[i][j]+1 == matrix[i][j-1]:
        longest = longestpath(matrix, cache, n, i, j-1)
        m = max(longest, m)
    if i>0 and matrix[i][j]+1 == matrix[i-1][j]:
        longest = longestpath(matrix, cache, n, i-1, j)
        m = max(longest, m)
    if i<n-1 and matrix[i][j]+1 == matrix[i+1][j]:
        longest = longestpath(matrix, cache, n, i+1, j)
        m = max(longest, m)
    cache[i][j] = m + 1
    return cache[i][j]
def main(matrix, n, cache):
    if matrix == None or n == 0:
        return 0
    longest = 0
    m = 0
    for i in range(n):
        for j in range(n):
            if cache[i][j] == -1:
                longest = longestpath(matrix, cache, n, i, j)
            m = max(cache[i][j], m)

    return m

matrix = [[1, 2, 9], 
    [5, 3, 8],
    [4, 6, 7]]
n = len(matrix)
cache = [[-1]*n]*n
print(cache)
print(main(matrix, n, cache))
