from collections import deque
from collections import defaultdict

class BFSResult:
    def __init__(self):
        self.parent = {}
        self.level = {}

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.vertex = set()

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.vertex.add(u)
        self.vertex.add(v)


def bfs(g, s):
    r = BFSResult()
    r.parent[s] = None
    r.level[s] = 0

    queue = deque()
    queue.append(s)

    while queue:
        u = queue.popleft()
        for n in g.adj[u]:
            if n not in r.level:
                r.parent[n] = u
                r.level[n] = r.level[u] + 1
                queue.append(n)

    return r



g = Graph()
g.add_edge('a', 'c')
g.add_edge('a', 'b')
g.add_edge('a', 'd')
g.add_edge('b', 'e')
g.add_edge('b', 'f')
g.add_edge('c', 'g')
g.add_edge('c', 'h')
g.add_edge('g', 'l')
g.add_edge('g', 'a') 

print(list(g.vertex))
print(bfs(g, 'a').level)
print(bfs(g, 'a').parent)

