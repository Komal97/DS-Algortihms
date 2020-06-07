def sum_of_digits(n):
    
    if n==0 or n==1:
        return n
    
    return (n%10) + sum_of_digits(int(n/10))

def main():
    n = int(input())
    print(sum_of_digits(n))

main()