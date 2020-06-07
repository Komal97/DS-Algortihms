'''
There are n stairs, a person standing at the bottom wants to reach the top.
The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top.
'''

def count_ways(n):
    if n==0 or n==1:
        return 1
    
    return count_ways(n-1) + count_ways(n-2)
    
def main():
    t = int(input())
    while(t):
        n = int(input())
        print(count_ways(n))
        t -= 1
    
main()