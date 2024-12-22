from time import sleep
import matplotlib.pyplot as plt
import networkx as nx
from random import random

with open('day16_test.txt') as file:
    maze = file.read().splitlines()

for y in range(len(maze)):
    if 'S' in maze[y]:
        start = [maze[y].index('S'), y]
    if 'E' in maze[y]:
        end = [maze[y].index('E'), y]

#print('\n'.join([''.join(i) for i in maze]))
print(f'Start: {start}, end: {end}')
print(len(maze) * len(maze) * 2001)
print('\n'.join([''.join(f'{i:02}{m}') for i, m in enumerate(maze)]))



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


counter = 0
def mover(pos: list, facing:int, prevs: list, prevNode:list, score:int, indent):    
    global ds, visited, counter
    counter += 1

    print(f'{indent}{pos=}, ', end='')

    
    valids = []
    for dirn in range(4):
        new = [pos[0]+ds[dirn], pos[1]+ds[::-1][dirn]]
        
        if maze[new[1]][new[0]] != '#' and new not in prevs:
            valids.append([new.copy(), dirn])

    exits = len(valids)
    print('exits:', exits)

    newPrevs = prevs.copy()
    newPrevs.append(pos)
    
    if exits > 1:
        mazeGraph.add_edge(f'{prevNode[0]}-{prevNode[1]}', f'{pos[0]}-{pos[1]}', weight=score)
    visited.append([facing, pos.copy()])

    for v in valids:
        mover(v[0], v[1], newPrevs, pos.copy() if exits > 1 else prevNode, 0 if exits > 1 else score+add[abs(dirn-facing)], indent+('.' if exits>1 else ''))

visited = []
mazeGraph = nx.Graph()

ds = [0, 1, 0, -1] #up, right, down, left
add = {0: 1, 1: 1001, 2: 2001, 3:1001}

mover(start, 1, [0,0].copy(), [0,0].copy(), 0, '')

drawGraph(mazeGraph)

print(nx.astar_path(mazeGraph, f'{start[0]}-{start[1]}', f'{end[0]}-{end[1]}', weight='weight'))


