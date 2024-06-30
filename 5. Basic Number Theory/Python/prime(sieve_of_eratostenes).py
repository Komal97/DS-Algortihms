'''
Input a number
Ouput all prime numbers less than a given number
'''
def prime_sieve(n):
    p = [0 for _ in range(n+1)] # mark all number as non-prime

    for i in range(3, len(p)+1, 2): # mark odd number as prime
        p[i] = 1

    p[2] = 1
    
    #iterate over only odd numbers
    for i in range(3, n+1, 2):
        if p[i]:    
            #for j in range(2*i, n+1, i):
            for j in range(i*i, n+1, 2*i): # mark all multiples that are not prime, and take jump of 2 because (odd i*i + odd i becomes even) 
                p[j] = 0

    for i in range(len(p)):
        if p[i]:
            print(i, end = " ")

def main():
    n = int(input())
    prime_sieve(n)
    
main()