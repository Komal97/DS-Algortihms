'''
Input a number
Check it is prime or not
'''
def check_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    if n%2 == 0:
        return False
    i = 3
    sqrt = int(n**0.5)
    while(i <= sqrt):
        if n%i == 0:
            return False
        i += 2
    return True

def main():
    n = int(input())
    res = check_prime(n)
    if res == True:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")
main()