def rabin_karp_algorithm(txt, pat):
    d = 256
    h = 1
    p = 0
    t = 0
    q = 101
    n = len(txt)
    m = len(pat)
    for i in range(m - 1):
        h = (h*d)%q
    print(h)
    #hash value of pattern and real text in window of text
    for i in range(m):
        p = (d*p + ord(pat[i]))%q 
        t = (d*t + ord(txt[i]))%q 
    print(p, t)
    for i in range(n - m + 1):
        
        if (p == t):
            j = 0
            while(j < m):
                if (txt[i+j] != pat[j]):
                    break
                j += 1
            if(j == m):
                print(f"match found at {i} index")
    # Calculate hash value for next window of text: Remove 
    # leading digit, add trailing digit 
        if i < n - m:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+m]))%q #https://www.youtube.com/watch?v=qQ8vS2btsxI&t=545s
            if t < 0:
                t = t + q
rabin_karp_algorithm(input(), input())
