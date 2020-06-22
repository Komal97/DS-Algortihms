from collections import deque
class StackUsingQueue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x):
        self.q1.append(x)        # O(1)
    
    def pop(self):
        n = len(self.q1)
        # transfer n-1 elements from q1 to q2
        for i in range(n-1):
            self.q2.append(self.q1.popleft())
        if len(self.q1) > 0:
            self.q1.popleft()
            self.q1, self.q2 = self.q2, self.q1  # maintain definition that q2 is always empty
        print(self.q1, self.q2)

    def top(self):
        n = len(self.q1)
        # transfer n-1 elements from q1 to q2
        for i in range(n-1):
            self.q2.append(self.q1.popleft())
        if len(self.q1) > 0:
            x = self.q1.popleft()
            self.q1, self.q2 = self.q2, self.q1  # maintain definition that q2 is always empty
            self.q1.append(x)
        return x
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
