class MinHeap:
    
    def __init__(self):
        self.v = []
        self.v.append(-1)

    def push(self, data):

        # add data to last
        self.v.append(data)
        index = len(self.v) - 1
        parent = index//2

        # keep swapping element with its parent until element < parent data
        while index > 1 and self.v[parent] > self.v[index]:
            self.v[index], self.v[parent] = self.v[parent], self.v[index]
            index = parent
            parent = parent//2 

    def getMin(self):
        # first element is minimum element
        return self.v[1] if len(self.v) > 1 else -1
    
    def __heapify(self, index):
        
        # find left and right child
        leftchild = 2*index
        rightchild = leftchild+1

        min_index = index
        # find min index among parent and its 2 children
        if leftchild < len(self.v) and self.v[leftchild] < self.v[index]:
            min_index = leftchild
        if rightchild < len(self.v) and self.v[rightchild] < self.v[min_index]:
            min_index = rightchild
        
        # if parent is smaller means heap is build
        # else swap parent and child and call on rest 
        if min_index != index:
            self.v[index], self.v[min_index] = self.v[min_index], self.v[index]
            self.__heapify(min_index)

    def pop(self):
        
        # swap first and last 
        last = len(self.v) - 1
        self.v[1], self.v[last] = self.v[last], self.v[1]
        # delete last element which is actually minimum element
        self.v.pop()
        # call heapify to build heap again
        self.__heapify(1)

    def isEmpty(self):
        return len(self.v) == 1

h = MinHeap()
arr = [1, 4, 3, 2, 6, 0, 10, 12]

for num in arr:
    h.push(num)

while not h.isEmpty():
    print(h.getMin(), end = " ")
    h.pop()