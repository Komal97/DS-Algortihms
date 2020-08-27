'''
You are given a graph, representing people and their connectivity.
You are also given a src person (who got infected) and time t.
You are required to find how many people will get infected in time t, if the infection spreads to neighbors of infected person in 1 unit of time.
Output:
count of people infected by time t

Input:
Sample Input
7
8
0 1 10
1 2 10
2 3 10
0 3 10
3 4 10
4 5 10
5 6 10
4 6 10
6
3
Output:
4
'''

# If level is greater than 't' then break
# count each node once
from collections import defaultdict, deque
def count_people(graph, visited, src, t):
    
    count = 0
    
    q = deque()
    q.append([src, 1])
    
    while len(q) > 0:
        
        node, level = q.popleft()
        if level > t:
            break
        
        if not visited[node]:
            count += 1
            
        visited[node] = True

        for neighbour in graph[node]:
            if not visited[neighbour]:
                q.append([neighbour, level+1])

    print(count)
    
v = int(input())                                   
e = int(input())                                    

graph = defaultdict(list)
visited = defaultdict(bool)

for i in range(e):
    a, b, c = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

src = int(input())                                   
t = int(input()) 

count_people(graph, visited, src, t)