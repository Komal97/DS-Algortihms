'''
Input:
abbabababbbabacdbaba
aba
Output:
pattern found at  3
pattern found at  5
pattern found at  11
pattern found at  17
'''

def kmp_precompute(pattern, lps):
    
    n = len(pattern)
    i = 0                              # behaving as pattern ptr
    j = 1                              # behaving as text ptr

    while j < n:
        if pattern[i] == pattern[j]:
            lps[j] = i+1               # saving length 
            i += 1
            j += 1
        else:
            if i != 0:                 # it is not starting, means at prv index, index of prefix is saved whiich is repeated
                i = lps[i-1]
            else:
                lps[j] = 0             # if at starting, means no match
                j += 1

def kmp_search(string, pattern):

    n = len(string)
    m = len(pattern)
    lps = [0]*n
    kmp_precompute(pattern, lps)
    i = 0
    j = 0
    while i < n:

        if string[i] == pattern[j]:     #.if character matches
            i += 1
            j += 1
        else:
            if j != 0:                  # if character doesn't match, then go to index without overlapping which is stored on prv index
                j = lps[j-1]
            else:
                i += 1                  # if first character dosnt match then increment string ptr
        
        if j == m:
            print('pattern found at ', i-j)
            j = lps[j-1]

string = input()
pattern = input()
kmp_search(string, pattern)