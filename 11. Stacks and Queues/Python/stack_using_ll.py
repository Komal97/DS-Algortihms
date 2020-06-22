class Stack:
    def __init__(self):
        self.head = None
        self.length = 0
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next =  None
    
    def push(self, data):
        n = self.Node(data)
        n.next = self.head
        self.head = n
        self.length += 1
    
    def pop(self):
        if self.empty():
            return
        temp = self.head
        self.head = self.head.next
        temp = None
        self.length -= 1
    
    def top(self):
        if self.empty():
            return -1
        return self.head.data

    def size(self):
        return self.length
    
    def empty(self):
        return self.head == None

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