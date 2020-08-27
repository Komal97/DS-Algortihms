'''
You are given a graph, a src vertex and a destination vertex.
You are required to find if a path exists between src and dest. If it does, print true otherwise print false.
Input:
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
0
6
Output:
true
'''

from collections import defaultdict

class Edge:
    def __init__(self, src, nbr, dist):
        self.src = src
        self.nbr = nbr
        self.dist = dist
            
def has_path(src, dest, visited, graph):
    if src == dest:                                     # if src = dest means we found a path
        return True
    
    visited[src] = True
    for neighbour in graph[src]:
        if not visited[neighbour.nbr]:
            haspath = has_path(neighbour.nbr, dest, visited, graph) # if first path is found then return true
            if haspath:
                return True
    return False
                

vertices = int(input())                                 # number of vertices
edges = int(input())                                    # number of edges

graph = defaultdict(list)
visited = defaultdict(bool)

for i in range(edges):
    parts = list(map(int, input().split()))
    src = parts[0]
    nbr = parts[1]
    wt = parts[2]
    graph[src].append(Edge(src, nbr, wt))               # add edge as an object in graph
    graph[nbr].append(Edge(src, nbr, wt))
    
source = int(input())                                   # source node
destination = int(input())                              # destination node

ans = has_path(source, destination, visited, graph)     # function to check path exist or not
if ans:
    print('true')
else:
    print('false')