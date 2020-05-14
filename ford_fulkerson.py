import math


class Graph:
    def __init__(self, size):
        self.size = size
        # tuple: (out node label, weight (capacity), flow)
        self.out_nodes = [[(-1, -1, -1) for _ in range(size)] for _ in range(size)]
        self.predecessors = [-1 for _ in range(size)]
        self.visited = [False for _ in range(size)]
        self.matrix = [[math.inf for _ in range(size)] for _ in range(size)]
        # self.residue_graph = None


def add_edge(u, v, w, graph):
    graph.out_nodes[u][v] = (v, w)
    graph.matrix[u][v] = w


# assume that t is reachable from s
def get_path(graph):
    path = [0]
    current = 0
    parents = graph.predecessors
    for v in range(len(parents)):
        neighbors = get_neighbors(graph, current)
        if v in neighbors:
            path.append(v)
    path.append(graph.size - 1)
    return path


def get_neighbors(graph, u):
    # return list(filter(lambda x: x >= 0, [(lambda t: t[0])(x) for x in graph.out_nodes[u]]))
    neighbors = []
    for v in range(graph.size):
        if graph.matrix[u][v] != math.inf:
            neighbors.append(v)
    return neighbors


def dfs(graph, s, t):
    neighbors = get_neighbors(graph, s)
    graph.visited[s] = True
    print('graph.predecessors: ', graph.predecessors)
    print('neighbors: ', neighbors)
    for neighbor in neighbors:
        if not graph.visited[neighbor]:
            graph.predecessors[neighbor] = s
            dfs(graph, neighbor, t)


# https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
def ford_fulkerson(graph):
    source, sink = 0, graph.size - 1
    max_flow = 0
    while graph.visited[sink]:
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph.matrix[graph.predecessors[s]][s])
            s = graph.predecessors[s]
        max_flow += path_flow
        v = sink
        # update residual capacity
        while v != source:
            u = graph.predecessors[v]
            graph.matrix[u][v] -= path_flow
            graph.matrix[v][u] += path_flow
            v = graph.predecessors[v]

            temp = graph.matrix[u][v]
            graph.matrix[u][v] = graph.matrix[v][u]
            graph.matrix[v][u] = temp
            print(graph.matrix)

        graph.visited[graph.size - 1] = False
        dfs(graph, 0, graph.size - 1)
    return max_flow


# Dodatek k graphvizu:
# Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur, coz se
# hodi predevsim pro ladeni.Vygenerovane soubory nahrajte do online nastroje
# pro zobrazeni graphvizu:
# http://sandbox.kidstrythisathome.com/erdos/
# nebo http://www.webgraphviz.com/ - zvlada i vetsi grafy.
#
# Alternativne si muzete nainstalovat prekladac z jazyka dot do obrazku na
# svuj pocitac.
def make_graph(graph, filename):
    with open(filename, 'w') as f:
        f.write("digraph MyGraph {\n")
        make_graphviz(graph, f)
        f.write("}\n")


def make_graphviz(graph, f):
    print(graph.out_nodes)
    for u in range(graph.size):
        for v in range(graph.size):
            if graph.out_nodes[u][v] != (-1, -1):
                f.write('"{}" -> "{}"\n'.format(u, v))


def create_test_graph():
    graph = Graph(4)
    for (u, v, w, f) in [(0, 1, 20, 0), (0, 2, 10, 0), (1, 2, 30, 0), (1, 3, 10, 0), (2, 3, 20, 0)]:
        add_edge(u, v, w, graph)
    # make_graph(graph, 'graph.dot')
    return graph


def main():
    graph = create_test_graph()
    dfs(graph, 0, 3)
    path = get_path(graph)
    # print(graph.matrix )
    # print('reachable: ', graph.visited[3])
    print(path)
    res = ford_fulkerson(graph)
    print('predecessors: ', graph.predecessors)
    print('visited: ', graph.visited)
    print('max_flow: ', res)


if __name__ == '__main__':
    main()
