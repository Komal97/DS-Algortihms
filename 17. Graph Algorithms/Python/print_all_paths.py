'''
You are given a graph, a src vertex and a destination vertex.
You are required to find and print all paths between source and destination. Print them in lexicographical order.
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
0123456
012346
03456
0346
'''
from collections import defaultdict

class Edge:
    def __init__(self, src, nbr, dist):
        self.src = src
        self.nbr = nbr
        self.dist = dist
            
def print_path(src, dest, visited, graph, output):
    if src == dest:                                     # if src = dest means we found a path
        print(output)
        return
    
    visited[src] = True
    for neighbour in graph[src]:
        if not visited[neighbour.nbr]:
            print_path(neighbour.nbr, dest, visited, graph, output+str(neighbour.nbr)) 
           
    visited[src] = False
                

vertices = int(input())                                 # number of vertices
edges = int(input())                                    # number of edges

graph = defaultdict(list)
visited = defaultdict(bool)

for i in range(edges):
    parts = list(map(int, input().split()))
    src = int(parts[0])
    nbr = int(parts[1])
    wt = int(parts[2])
    graph[src].append(Edge(src, nbr, wt))               # add edge as an object in graph
    graph[nbr].append(Edge(src, nbr, wt))
    
source = int(input())                                   # source node
destination = int(input())                              # destination node

print_path(source, destination, visited, graph, str(source))     # function to check path exist or not



