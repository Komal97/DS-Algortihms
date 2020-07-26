class MaxHeap:
    
    def __init__(self):
        self.v = []
        self.v.append(-1)

    def push(self, data):
        
        self.v.append(data)
        index = len(self.v) - 1
        parent = index//2
        
        # keep swapping element with its parent until element > parent data
        while index > 1 and self.v[parent] < self.v[index]:
            self.v[parent], self.v[index] = self.v[index], self.v[parent]
            index = parent
            parent = parent//2

    def getMax(self):
        # first element is maximum element
        return self.v[1]
    
    def __heapify(self, index):
        
        left = 2*index
        right = left + 1
        maxindex = index

        if left < len(self.v) and self.v[left] > self.v[maxindex]:
            maxindex = left

        if right < len(self.v) and self.v[right] > self.v[maxindex]:
            maxindex = right
        
        # if parent is greater means heap is build
        # else swap parent and child and call on rest 
        if maxindex != index:
            self.v[index], self.v[maxindex] = self.v[maxindex], self.v[index]
            self.__heapify(maxindex)

    def pop(self):
        last = len(self.v) - 1
        self.v[last], self.v[1] = self.v[1], self.v[last]
        # delete last element which is actually maximum element
        self.v.pop()
        # call heapify to build heap again
        self.__heapify(1)

    def isEmpty(self):
        return len(self.v) == 1

h = MaxHeap()
arr = [1, 4, 3, 2, 6, 0, 10, 12]

for num in arr:
    h.push(num)

while not h.isEmpty():
    print(h.getMax(), end = " ")
    h.pop()