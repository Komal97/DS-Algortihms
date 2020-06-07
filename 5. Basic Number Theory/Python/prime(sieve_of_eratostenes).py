'''
Input a number
Ouput all prime numbers less than a given number
'''
def prime_sieve(n):
    p = [0 for _ in range(n+1)]

    for i in range(3, len(p)+1, 2):
        p[i] = 1

    p[2] = 1
    
    for i in range(3, n+1, 2):
        if p[i]:
            #for j in range(2*i, n+1, i):
            for j in range(i*i, n+1, 2*i):
                p[j] = 0

    for i in range(len(p)):
        if p[i]:
            print(i, end = " ")

def main():
    n = int(input())
    prime_sieve(n)
    
main()