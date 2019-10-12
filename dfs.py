from collections import defaultdict

class DFSResult:
    def __init__(self):
        self.parent = {}
        self.start_time = {}
        self.finish_time = {}
        self.edges = {} # for directed graph
        self.order = []
        self.t = 0


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def neighbors(self, u):
        res = list(self.adj[u])
        res.sort()
        return res

    def get_vertices(self):
        res = list(self.vertices)
        res.sort()
        return res

    
def dfs(g):
    results = DFSResult()
    
    dfs_visit(g, 'f', results)
    for vertex in g.get_vertices():
        if vertex not in results.parent:
            dfs_visit(g, vertex, results)
    
    return results

def dfs_visit(g, v, results, parent = None):
    results.parent[v] = parent
    results.t += 1
    results.start_time[v] = results.t
    if parent:
        results.edges[(parent, v)] = 'tree'

    for n in g.neighbors(v):
        if n not in results.parent: # n is not visited yet
            dfs_visit(g, n, results, v)
        elif n not in results.finish_time:
            results.edges[(v, n)] = 'back'
        elif results.start_time[v] < results.start_time[n]:
            results.edges[(v, n)] = 'forward'
        else:
            results.edges[(v, n)] = 'cross'
    
    results.t += 1
    results.finish_time[v] = results.t
    results.order.append(v)

def is_acylic(g):
    results = dfs(g)
    if 'back' not in results.edges.values():
        return True
    else:
        return False

g = Graph()
g.add_edge('a', 'c')
g.add_edge('a', 'b')
# g.add_edge('a', 'f')
g.add_edge('b', 'd')
g.add_edge('b', 'c')
g.add_edge('f', 'a')
g.add_edge('f', 'c')
g.add_edge('d', 'c')
# g.add_edge('d', 'a') 
g.add_edge('e', 'c')
g.add_edge('e', 'g')
g.add_edge('g', 'd')
# g.add_edge('g', 'e')

print('vertices: ', g.get_vertices())
r = dfs(g)
print('parent: ', r.parent)
print('start_time: ', r.start_time)
print('finish_time: ', r.finish_time)
print('edges: ', r.edges)
print('order: ', r.order)

print('This graph is acylic: ', is_acylic(g))

