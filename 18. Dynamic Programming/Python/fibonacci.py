# recursion
def fib(n):
    if n == 0 or n == 1:
        return n
    
    return fib(n-1) + fib(n-2)

# memoization
def fibMemoized(n, memo):
    if n == 0 or n == 1:
        return n
    
    if memo[n] != 0:
        return memo[n]

    first =  fibMemoized(n-1, memo) 
    second = fibMemoized(n-2, memo)

    memo[n] = first + second
    return memo[n]

print(fib(5))

memo = [0] *6
print(fibMemoized(5, memo))
print(memo)