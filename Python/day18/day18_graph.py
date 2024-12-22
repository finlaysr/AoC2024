import matplotlib.pyplot as plt
import networkx as nx
from random import random
import sys
sys.setrecursionlimit(10**6)

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


with open('day18_test.txt') as file:
    coordsOrig = [[int(j) for j in i.split(',')] for i in file.read().splitlines()]

size = 70+1

def check(falling):

    coords = coordsOrig[:falling]
    #board = [['.' for _ in range(size)] for _ in range(size)]
    #for i in coords: 
    #    board[i[1]][i[0]] = '#' 
    #print('\n'.join([''.join(i) for i in board]))

    d = ((0, -1), (1, 0), (0, 1), (-1, 0))
    visited = []
    mazeGraph = nx.Graph()

    def mover(pos: list, dist:int):
        #print(f'{indent}{pos}')
        visited.append(pos)

        valid = []
        for dx, dy in d:
            new = [pos[0]+dx, pos[1]+dy]
            if new[0] >= 0 and new[0] < size and new[1] >= 0 and new[1] < size and new not in visited :
                if new not in coords:
                    valid.append([new.copy(), pos.copy()])
        
        for v in valid:
            mazeGraph.add_edge(f'{v[1][0]}-{v[1][1]}', f'{v[0][0]}-{v[0][1]}', weight=1)
            mover(v[0], dist+1)

    mover([0,0], 0)

    shortest = nx.astar_path_length(mazeGraph, '0-0', f'{size-1}-{size-1}')
    '''
    for i in shortest:
        s = [int(j) for j in i.split('-')]
        board[s[1]][s[0]] = 'o'

    print('\n'.join([''.join(i) for i in board]))'''

    print(falling, 'has length:', shortest-1)
    #drawGraph(mazeGraph)

#check(1024)

low = 0; found = False
high = len(coordsOrig)
while not found and low <= high:
    mid = (low+high) // 2
    #print(mid)
    try:
        check(mid)
        low = mid + 1
    except:
        high = mid-1

print('Found at', mid, coordsOrig[mid])
