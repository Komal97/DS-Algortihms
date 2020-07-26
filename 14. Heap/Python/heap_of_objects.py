from heapq import heappush, heappop

# MIN HEAP of objects
class Car:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self):
        return (self.x * self.x) + (self.y * self.y)
    
    def printObj(self):
        print('location:', self.x, self.y, 'with distance:', self.dist())
        
    # this is a inbuilt function, tells criteria to sort object in heap
    def __gt__(self, other):
        return self.dist() > other.dist()

heap = []
x = [5, 6, 17, 18, 9, 11, 0, 3]
y = [1, -2, 8, 9, 10, 91, 1, 2]

for i in range(len(x)):
    c = Car(x[i], y[i])
    heappush(heap, c)

# give points in ascending order of distance from origin
while len(heap) > 0:
    c = heap[0]
    c.printObj()
    heappop(heap)