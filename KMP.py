def compute_table(pat, m, table):
    j = 0
    i = 1
    table[0] = 0
    for i in range(1, 6):
        if (pat[i] == pat[j]):
            j += 1
            table[i] = j
        else:
            if (j != 0):
                j = table[j - 1]
                i -= 1
            else:
                table[i] = 0
        
def KMPsearch(pat, txt):
    n = len(txt)
    m = len(pat)
    table = [0]*m
    j = 0
    compute_table(pat, m, table)
    i = 0
    while(i < n):
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == m:
            print(f"Found at index {i - j}")
            j = table[j - 1]
        elif(i < n and pat[j] != txt[i]):
            if j != 0:
                j = table[j-1]
            else:
                i += 1


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPsearch(pat, txt) 