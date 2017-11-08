import math
import pathfinder


g = pathfinder.Graph()

g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')

g.add_edge('A', 'B', 3)
g.add_edge('A', 'C', 2)
g.add_edge('C', 'D', 3)
g.add_edge('B', 'D', 1)

print g.dijkstra('A')




def distance(x2, x1, y2, y1):
    return math.sqrt(((x2-x1) ^ 2)+((y2-y1) ^ 2))

