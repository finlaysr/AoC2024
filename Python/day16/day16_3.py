import matplotlib.pyplot as plt
import networkx as nx
from random import random
import sys
sys.setrecursionlimit(10**6)

with open('day16_test.txt') as file:
    maze = [list(i) for i in file.read().splitlines()]

for y in range(len(maze)):
    if 'S' in maze[y]:
        start = [maze[y].index('S'), y]
    if 'E' in maze[y]:
        end = [maze[y].index('E'), y]

#print('\n'.join([''.join(i) for i in maze]))
print(f'Start: {start}, end: {end}')
print(len(maze) * len(maze))

def drawGraph(graph: nx.Graph):
    # nodes
   
    pos = nx.spring_layout(graph, seed=7)  # positions for all nodes - seed for reproducibility
    nx.draw_networkx_nodes(graph, pos, node_size=400, node_color=[tuple(random() for _ in range(3)) for _ in range(graph.__len__())])
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(), width=1)

    nx.draw_networkx_labels(graph, pos, font_size=10, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.0)
    plt.axis("off")
    
    plt.tight_layout()
    plt.show()

amount = 0
def mover(pos: list, facing:int):
    global amount
    visited.append(pos)

    amount += 1
    if amount >= 7110: 
        print(amount)

    valids = []
    for i, (dx, dy) in enumerate(d):
        new = [pos[0]+dx, pos[1]+dy]
        if new[0] >= 0 and new[0] < len(maze[0]) and new[1] >= 0 and new[1] < len(maze) and new not in visited:
            if maze[new[1]][new[0]] != '#':
                valids.append([new.copy(), i])
    
    for v in valids:
        mazeGraph.add_edge(f'{pos[0]}-{pos[1]}', f'{v[0][0]}-{v[0][1]}', weight = dist[abs(v[1]-facing)])
        mover(v[0], v[1])

d = ((0, -1), (1, 0), (0, 1), (-1, 0)) #up, right, down, left
visited = [start.copy()]
dist = {0: 1, 1: 1001, 3:1001}

mazeGraph = nx.Graph()
mover(start, 1)
print('Here')

shortest = nx.astar_path(mazeGraph, f'{start[0]}-{start[1]}', f'{end[0]}-{end[1]}')
for i in shortest:
    s = [int(j) for j in i.split('-')]
    maze[s[1]][s[0]] = 'o'
print('\n'.join([''.join(i) for i in maze]))

print(nx.astar_path_length(mazeGraph, f'{start[0]}-{start[1]}', f'{end[0]}-{end[1]}')-1000)

#drawGraph(mazeGraph)

