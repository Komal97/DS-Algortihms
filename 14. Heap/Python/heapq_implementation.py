from heapq import heapify, heappush, heappop, heappushpop, heapreplace, nlargest, nsmallest

arr = [1, 4, 3, 2, 6, 0, 10, 12]

# create min heap from array in-place
heapify(arr)

# print heapified arr
print(list(arr))                        # [0, 2, 1, 4, 6, 3, 10, 12]

# insert element in heap
heappush(arr, 13)

# push new element and then pop min element
heappushpop(arr, 3)

# pop min element and then push new element
heapreplace(arr, 0)

# get min element
print(arr[0])

# print nlargest and nsmallest elements from heap, here n=3
print(nlargest(3, arr))                 # [13, 12, 10]
print(nsmallest(3, arr))                # [0, 2, 3]

# pop and print elements from heap
while len(arr) > 0:
    print(heappop(arr), end = ' ')      # 0 2 3 3 4 6 10 12 13
    
    
# insert tuple as pair
q = []

heappush(q, (2, 'code'))
heappush(q, (1, 'eat'))
heappush(q, (3, 'sleep'))

while q:
    next_item = heappop(q)
    print(next_item)

# Result:
#   (1, 'eat')
#   (2, 'code')
#   (3, 'sleep')