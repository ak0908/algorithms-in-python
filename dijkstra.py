import queue
from collections import namedtuple, defaultdict



Edge = namedtuple('Edge', ['vertex', 'weight'])

class Graph:
    def __init__(self):
        self.vertices = set()
        self.adj = defaultdict(list)

    def add_edge(self, start, end, weight):
        self.vertices.add(start)
        self.vertices.add(end)
        self.adj[start].append(Edge(end, weight))
        self.adj[end].append(Edge(start, weight))


    def get_edge(self, vertex):
        
        return self.adj[vertex]

    def get_vertex(self):
        
        return self.vertices


def dijkstra(graph, start, end):
    visited = {}
    pq = queue.PriorityQueue()
    parents = {}
    distances_to = {}

    for i in graph.get_vertex():
        distances_to[i] = float('inf')
        parents[i] = None
        visited[i] = False


    distances_to[start] = 0
    pq.put(([distances_to[start], start]))

    while not pq.empty():
        distances_to_v , v = pq.get()

        for e in graph.get_edge(v):
            if not visited[v]:
                if distances_to[e.vertex] > min(distances_to_v + e.weight, distances_to[e.vertex]):
                    distances_to[e.vertex] = distances_to_v + e.weight
                    parents[e.vertex] = v
                    pq.put(([distances_to[e.vertex], e.vertex]))

        visited[v] = True


    shortest_path = []
    end2 = end
    while end is not None:
        shortest_path.append(end)
        end = parents[end]

    shortest_path.reverse()

    return shortest_path, distances_to[end2]



g = Graph()
g.add_edge('a', 'b', 3)
g.add_edge('a', 'c', 4)
g.add_edge('b', 'f', 6)
g.add_edge('b', 'd', 2)
g.add_edge('c', 'f', 8)
g.add_edge('c', 'd', 10)
g.add_edge('f', 'd', 10)
g.add_edge('f', 'g', 2)
g.add_edge('d', 'g', 1)




shortest_path, distance = dijkstra(g, 'a', 'f')

print("shortest_path: ", shortest_path)
print("distance between a and f: ", distance)



    
