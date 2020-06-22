class Stack:
    def __init__(self):
        self.l = []
    
    def push(self, data):
        self.l.append(data)
    
    def pop(self):
        if self.empty():
            return
        self.l.pop()
    
    def top(self):
        if self.empty():
            return -1
        return self.l[-1]

    def size(self):
        return len(self.l)
    
    def empty(self):
        return len(self.l) == 0

if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(4)
    s.push(1)
    print(s.top())
    s.pop()
    print(s.size())
    print(s.top())
    print(s.empty())