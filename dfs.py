from pprint import pprint

def DFS (G):
    for u in G:
        if color[u] == 'white':
            DFS_visit(u)

def DFS_visit(u):
    global time
    color[u] = 'gray'
    time += 1
    distance[u] = time
    for v in graph[u]:
        if color[v] == 'white':
            parent[v] = u
            DFS_visit(v)
    color[u] = 'black'
    time += 1
    final[u] = time



graph = {
    'A' :['B','C'],
    'B' : ['A', 'D','E'],
    'C' : ['A','F'],
    'D' : ['B'],
    'E' : ['B', 'F'],
    'F' : ['C', 'E']
}
color = {}
distance = {}
parent = {}
final = {}
time = 0

for i in graph:
    color[i] = 'white'
    distance[i] = 0
    parent[i] = 'NIL'

pprint ("Before DFS")
print()
print("Actual Graph")
pprint(graph)
print('\n Inital node colors \n')
pprint(color)
print('\n Initial Distance Matrix\n')
pprint(distance)
print()

DFS(graph)

print ("After DFS")
print()
print('\n Final node colors \n')
pprint(color)
print('\n Final Distance Matrix\n')
pprint(distance)
print('\n Final Graph after DFS\n')
pprint(final)            



