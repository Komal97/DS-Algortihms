'''
reverse queue using recursion
Input: 1,2,3,4,5
Output: 5,4,3,2,1
'''
from collections import deque
def reverse_queue(q):
    stack = deque()
    while len(q) != 0:
        stack.append(q.popleft())
    while len(stack) != 0:
        q.append(stack.pop())
    print(q)

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    q = deque(arr)
    print(q)
    reverse_queue(q)