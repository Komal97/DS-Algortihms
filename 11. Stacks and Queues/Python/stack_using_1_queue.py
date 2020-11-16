from collections import deque
class StackUsingQueue:
    def __init__(self):
        self.q1 = deque()
    
    def push(self, x):
        self.q1.append(x)        # O(1)
    
    def pop(self):
        n = len(self.q1)
        # transfer n-1 elements at back of q1
        for i in range(n-1):
            self.q1.append(self.q1.popleft())
        if len(self.q1) > 0:
            self.q1.popleft()
        print(self.q1)

    def top(self):
        n = len(self.q1)
        # transfer n-1 elements at back of q1
        for i in range(n-1):
            self.q1.append(self.q1.popleft())
            
        if len(q) > 0:
            top_val = self.q[0]
            self.q1.append(self.q1.popleft())
        return top_val

    def empty(self):
        return len(self.q1) == 0

if __name__ == '__main__':
    n = int(input())
    s = StackUsingQueue()
    for i in range(5):
        s.push(i)
    
    while not s.empty():
        print(s.top())
        s.pop()
