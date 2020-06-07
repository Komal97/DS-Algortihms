def factorial(n):
    if n==0:
        return 1
    
    return n*factorial(n-1)

def fibonacci(n):
    if n==0 or n==1:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    print(factorial(6))
    print(fibonacci(6))

if __name__ == '__main__':
    main()