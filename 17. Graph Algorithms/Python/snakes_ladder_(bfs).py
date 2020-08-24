'''
https://practice.geeksforgeeks.org/problems/snake-and-ladder-problem/0
Find minimum number of moves to reach dest from starting point
'''

# since to find = min moves means find shortest path from src to dest which can be acheived using bfs
from collections import defaultdict, deque
class Graph:

    def __init__(self):
        self.__h = defaultdict(list)
    
    def add_edge(self, u, v, bidirec = True):
        
        self.__h[u].append(v)
        if bidirec:
            self.__h[v].append(u)
    
    def bfs(self, src, dest):
        
        queue = deque()
        parent = defaultdict()
        dist = defaultdict(int)
        # for node in self.__h:
        #     dist[node] = float('inf')
        for node in range(max_board_limit):
            dist[node] = float('inf')
        
        queue.append(src)
        dist[src] = 0
        parent[src] = src

        while len(queue) > 0:
            node = queue.popleft()
            for neighbour in self.__h[node]:
                if dist[neighbour] == float('inf'):
                    queue.append(neighbour)
                    dist[neighbour] = dist[node] + 1
                    parent[neighbour] = node
        
        temp = dest                                     # print path from dest to src because we have parent stored
        while temp != src:
            print(temp, end = ' <- ')
            temp = parent[temp]
        print(src)
        
        return dist[dest]

# create a board of snake and ladder
# if +ve means ladder => board[2] = 13 means from 2 reach 2+13 = 15 so edge will created is 1 -> 15 instead of 1 -> 2
# if -ve means snake => board[17] = -13 means from 17 reach 17-13 = 4
max_board_limit = 50
dice_count = 6
board = [0]*max_board_limit
board[2] = 13                                      
board[5] = 2
board[9] = 18
board[18] = 11
board[17] = -13
board[20] = -14
board[24] = -8
board[25] = -10
board[32] = -2
board[34] = -22

g = Graph() 
for u in range(37):                             # create edges from each point to all 6 possibilities
    for dice in range(1, dice_count+1):   
        if u + dice < max_board_limit:         
            v = u + dice + board[u + dice]
            g.add_edge(u, v, False)

min_moves = g.bfs(1, 36)
print(min_moves)