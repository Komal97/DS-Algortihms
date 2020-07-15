'''
Find number of unique BST's with N nodes and nodes are numbered from 1 to N
This can be find out using catalan's number
'''
# using recursion
def find_catalan(num):
    if num == 0:
        return 1
    
    ans = 0
    for i in range(1, num+1):
        ans += find_catalan(i-1)*find_catalan(num-i)
    
    return ans 

# using memoization
dp = [0]*100
def find_catalan_memoization(num):
    if num == 0:
        return 1
    
    # if catalan of number is already computed
    if dp[num] != 0:
        return dp[num]

    ans = 0
    for i in range(1, num+1):
        ans += find_catalan(i-1)*find_catalan(num-i)
    
    # if catalan of number is computed first time
    dp[num] = ans
    return ans 

# using formula - 2nCn/(n+1)
def factorial(n):
    if n==0 or n==1:
        return 1
    prod = 1

    for i in range(1, n+1):
        prod *= i 
    return prod 

def catalan_using_formula(num):

    numerator = factorial(2*num)//(factorial(num)*factorial(num))
    denominator = num+1
    return numerator//denominator

if __name__ == '__main__':

    for i in range(6):
        print(find_catalan(i), end = ", ")
    
    print()
    for i in range(6):
        print(find_catalan_memoization(i), end = ", ")
    
    print()
    for i in range(6):
        print(catalan_using_formula(i), end = ", ")