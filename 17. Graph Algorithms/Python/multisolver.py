from collections import defaultdict
from heapq import heappush, heappop
class Edge:
    def __init__(self, src, nbr, dist):
        self.src = src
        self.nbr = nbr
        self.dist = dist

spath = ''
sweight = float('inf')
lpath = ''
lweight = float('-inf')
cpath = ''
cweight = float('inf')
fpath = ''
fweight = float('-inf')
heap = []
def print_path(src, dest, criteria, k, visited, weight, graph, output):
    global spath 
    global sweight 
    global lpath
    global lweight
    global cpath 
    global cweight 
    global fpath 
    global fweight
    global heap
    if src == dest:   
        #print(output, weight) 
        if weight < sweight:
            sweight = weight 
            spath = output
            
        if weight > lweight:
            lweight = weight
            lpath = output
        
        if weight > criteria and weight < cweight:
            cweight = weight
            cpath = output 
        
        if weight < criteria and weight > fweight:
            fweight = weight
            fpath = output
    
        if len(heap) < k:
            heappush(heap, [weight, output])
        else:
            top = heap[0]
            if top[0] < weight:
                heappop(heap)
                heappush(heap, [weight, output])
        return

    visited[src] = True
    for edge in graph[src]:
        if not visited[edge.nbr]:
            print_path(edge.nbr, dest, criteria, k, visited, weight+edge.dist, graph, output+str(edge.nbr)) 
           
    visited[src] = False
                

vertices = int(input())                                 
edges = int(input())                                    

graph = defaultdict(list)
visited = defaultdict(bool)

for i in range(edges):
    parts = list(map(int, input().split()))
    src = int(parts[0])
    nbr = int(parts[1])
    dist = int(parts[2])
    edge = Edge(src, nbr, dist)
    graph[edge.src].append(edge)                        
    graph[edge.nbr].append(edge)
    
source = int(input())                                   
destination = int(input()) 
criteria = int(input())                                   
k = int(input()) 

print_path(source, destination, criteria, k, visited, 0, graph, str(source))     

print('Smallest Path =', spath + '@' + str(sweight)) 
print('Largest Path =', lpath + '@' + str(lweight)) 
print('Just Larger Path than', criteria, '=', cpath + '@' + str(cweight)) 
print('Just Smaller Path than', criteria, '=', fpath + '@' + str(fweight)) 
print(str(k) + 'th largest path =', heap[0][1] + '@' + str(heap[0][0])) 



