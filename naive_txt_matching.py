
def searching(txt, pat):
    n = len(txt)
    m = len(pat)
    
    for i in range(n - m + 1):
        j = 0
        while(j < m):
            if (pat[j] != txt[i + j]):
                break
            j += 1
        if j == m:
            print(f'match found at index : {i}')
searching(input(), input())