def Brute_force_Stringmatching(txt, pat):
    n = len(txt)
    m = len(pat)
    for i in range(n - m + 1):
        j = 0
        while(j < m):
            if (txt[i + j] != pat[j]):
                break
            j += 1
        if (j == m):
            print(f"pattern found at index {i}")
Brute_force_Stringmatching(input(), input())
                

