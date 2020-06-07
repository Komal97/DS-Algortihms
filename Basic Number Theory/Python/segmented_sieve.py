def prime_sieve(n):
    arr = [0 for _ in range(n+1)]
    
    arr[2] = 1
    for i in range(3, n+1, 2):
        arr[i] = 1

    for i in range(3, n+1, 2): 
        if(arr[i]):
            for j in range(i*i, n+1, 2*i):
                arr[j] = 0
    print(arr)
    return arr

def segmented_sieve(a, b):
    arr = [1 for _ in range(b-a+1)]
    sieve_arr = prime_sieve(int(b**0.5))
    
    for i in range(2, len(sieve_arr)):
        if sieve_arr[i]:
            for j in range(a, b+1):
                if j == i:
                    continue
                if j%i == 0:
                    arr[j-a] = 0

    for i in range(len(arr)):
        if arr[i]:
            print(i+a)
a = 2
b = 40
segmented_sieve(a, b)