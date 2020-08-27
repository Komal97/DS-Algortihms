'''
You are given a graph and a source vertex. The vertices represent computers and the edges represent length of LAN wire required to connect them.
You are required to find the minimum length of wire required to connect all PCs over a network. 
Print the output in terms of which all PCs need to be connected, and the length of wire between them.
Input:
7
8
0 1 10
1 2 10
2 3 10
0 3 40
3 4 2
4 5 3
5 6 3
4 6 8
Output:
[1-0@10]
[2-1@10]
[3-2@10]
[4-3@2]
[5-4@3]
[6-5@3]
'''

from heapq import heappush, heappop
from collections import defaultdict

def min_length_path(graph, visited):

    heap = []
    heappush(heap, [0, [0, -1]])
    
    while len(heap) > 0:
        dist = heap[0][0]
        node, parent = heap[0][1]
        heappop(heap)
        
        if visited[node]:
            continue
        
        if parent != -1:
            print('[' + str(node) + '-' + str(parent) + '@' + str(dist) + ']')
        
        visited[node] = True
        for neighbour, distance in graph[node]:
            if not visited[neighbour]:
                heappush(heap, [distance, [neighbour, node]])

v = int(input())                                   
e = int(input())                                    

graph = defaultdict(list)
visited = defaultdict(bool)

for i in range(e):
    a, b, c = list(map(int, input().split()))
    graph[a].append([b, c])
    graph[b].append([a, c])

min_length_path(graph, visited)