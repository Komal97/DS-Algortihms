class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next =  None
    
    def enque(self, data):
        if self.empty():
            self.head = self.Node(data)
            self.tail = self.head
        else:
            n = self.Node(data)
            n.next = None
            self.tail.next = n
            self.tail = n
        self.length += 1
    
    def deque(self):
        if self.empty():
            return
        temp = self.head
        self.head = self.head.next
        temp = None
        self.length -= 1
    
    def front(self):
        if self.empty():
            return -1
        return self.head.data

    def size(self):
        return self.length
    
    def empty(self):
        return self.head == None

if __name__ == '__main__':
    q = Queue()
    q.enque(5)
    q.enque(4)
    q.enque(1)
    print(q.front())
    q.deque()
    print(q.front())
    print(q.size())
    print(q.empty())