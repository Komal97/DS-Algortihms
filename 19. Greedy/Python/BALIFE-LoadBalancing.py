'''
https://www.spoj.com/problems/BALIFE/
Given the number of jobs initially assigned to each processor, you are asked to determine the minimal number of rounds needed to achieve the state when every processor has the same number of jobs, 
or to determine that such rebalancing is not possible.

Input 1:
3
0 99 3
Output: 34

Input 2:
2
49 50
Output: -1

Input 3:
8
16 17 15 0 20 1 1 2
Output: 23

Input 4:
10
0 0 100 0 0 0 0 0 0 0
Output: 70
'''

def findMinRounds(arr, n):

    cs = [arr[0]]
    for i in range(1, n):
        cs.append(cs[i-1] + arr[i])
    
    if (cs[n-1] % n) != 0:
        return -1 
    
    average = cs[n-1]//n
    maxsum = -1
    for i in range(n-1):
        # partition at each index
        c = average * (i+1)
        
        # transfer load from first partition to next and find max of all those
        maxsum = max(maxsum, abs(c - cs[i]))
    
    return maxsum if maxsum != 0 else -1

n = int(input())
arr = list(map(int, input().split()))

ans = findMinRounds(arr, n)
print(ans)
    