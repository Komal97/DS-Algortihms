'''
reverse stack using recursion
Input: 1,2,3,4,5
Output: 5,4,3,2,1
'''
from collections import deque
def insert_at_bottom(s, x):
    if len(s) == 0:
        s.append(x)
        return
    y = s.pop()
    insert_at_bottom(s, x)
    s.append(y)
def reverse_stack(s):
    if len(s) == 0:
        return
    x = s.pop()
    reverse_stack(s)
    insert_at_bottom(s, x)

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    s = deque(arr)
    print(s)
    reverse_stack(s)
    print(s)