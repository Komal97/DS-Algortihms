'''
reverse stack using one extra stack
Input: 1,2,3,4,5
Output: 5,4,3,2,1
'''

from collections import deque
def transfer(s1, s2, n):
    for i in range(n):
        s2.append(s1.pop())

def reverse_stack(arr, n):
    s1 = deque(arr)
    s2 = deque()
    print(s1)
    print(s2)
    for i in range(n):
        x = s1.pop()
        transfer(s1, s2, n-i-1)
        s1.append(x)
        transfer(s2, s1, n-i-1)
    print(s1)
    print(s2)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    reverse_stack(arr, n)