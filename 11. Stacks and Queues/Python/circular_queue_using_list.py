class Queue:
    def __init__(self, max_size = 4):
        self.max_size = max_size
        self.cur_size = 0
        self.front = 0
        self.rear = max_size - 1
        self.l = [0]*max_size
    
    def enque(self, data):
        if not self.isFull():
            self.rear = (self.rear+1)%self.max_size
            self.l[self.rear] = data
            self.cur_size += 1
    
    def deque(self):
        if not self.empty():
            self.front = (self.front+1)%self.max_size
            self.cur_size -= 1
    
    def getFront(self):
        return self.l[self.front]
    
    def isFull(self):
        return self.cur_size == self.max_size
    
    def empty(self):
        return self.cur_size == 0
    
    def size(self):
        return self.cur_size
        
if __name__ == '__main__':
    q = Queue()
    
    for i in range(6):
        q.enque(i)
    q.deque()
    q.enque(8)
    while not q.empty():
        print(q.getFront(), end = " ")
        q.deque()
