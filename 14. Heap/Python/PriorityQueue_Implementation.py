from queue import PriorityQueue

heap = PriorityQueue()
heap.put(10)    # Puts an item into the queue
heap.put(90)
heap.put(30)
heap.put(20)

print(heap.qsize()) # Returns the current queue size.
print(heap.empty()) # Returns True if the queue is empty, False otherwise. It is equivalent to qsize()==0
print(heap.full())  # Returns True if the queue is full, False otherwise. It is equivalent to qsize()>=maxsize
print(heap.get())   # Removes and returns an item from the queue


# insert tuple as pair 
q = PriorityQueue()

q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while not q.empty():
    next_item = q.get()
    print(next_item)

# Result:
#   (1, 'eat')
#   (2, 'code')
#   (3, 'sleep')