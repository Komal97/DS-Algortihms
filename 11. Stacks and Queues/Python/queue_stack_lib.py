from collections import deque

# stack
s = deque([])
    
for i in range(6):
    s.append(i)
print(s)
print(s.pop())
print(s)

# queue
q = deque([])
for i in range(6):
    q.append(i)
print(q)
print(q.popleft())
print(q)
   
# reverse
q.reverse()
print(q)
# length
print(len(q))
# rotate by 3 to left
q.rotate(-3)
print(q)
    
