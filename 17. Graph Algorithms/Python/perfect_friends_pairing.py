'''
You are given a number n (representing the number of students). Each student will have an id from 0 to n - 1.
You are given a number k (representing the number of clubs)
In the next k lines, two numbers are given separated by a space. The numbers are ids of students belonging to same club.
You have to find in how many ways can we select a pair of students such that both students are from different clubs.
Input:
7
5
0 1
2 3
4 5
5 6
4 6
Output:
16
'''

from collections import defaultdict

def perfect_friends(graph, src, visited, count):
    
    visited[src] = True
    count[0] += 1
    for neighbour in graph[src]:
        if not visited[neighbour]:
            perfect_friends(graph, neighbour, visited, count)
        

n = int(input())                                    # number of students = number of vertices
k = int(input())                                    # number of clubs = number of edges

graph = defaultdict(list)
visited = defaultdict(bool)

for i in range(k):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

# find number of clubs and members in each club = number of connected components
comp_count = []                                     # keep count of members in each component
for i in range(n):
    count = [0]
    if not visited[i]:
        perfect_friends(graph, i, visited, count)   
        comp_count.append(count[0])

# to find pairs = choose c1 ways from 1 club and c2 ways in other club = so c1*c2 
# final ans = take all combinations of clubs
pairs = 0
for i in range(len(comp_count)):                   
    for j in range(i+1, len(comp_count)):
        count = comp_count[i]*comp_count[j]
        pairs += count
        
print(pairs)