from collections import deque


class Graph:
    def __init__(self, size):
        """Vytvori orientovany graf se 'size' vrcholy a bez jakychkoli hran.
        Atributy:
            size: pocet vrcholu v grafu
            matrix: maticova reprezentace grafu popsana vyse
            parent, distance: pro pouziti v algoritmu BFS, viz nize
            parent, visited, discovery_time, finishing_time:
                pro pouziti v algoritmu DFS, viz nize
        """
        self.size = size
        self.matrix = [[False] * size for _ in range(size)]
        self.clear_flags()

    def clear_flags(self):
        self.parent = [None] * self.size
        self.distance = [None] * self.size
        self.discovery_time = [None] * self.size
        self.finishing_time = [None] * self.size

        self.visited = [False] * self.size


def get_neighbours(graph, v):
    neighbors = []
    for u in range(graph.size):
        if graph.matrix[v][u]:
            neighbors.append(u)
    return neighbors


def dfs_recc(graph, s):
    neighbors = get_neighbours(graph, s)
    graph.visited[s] = True
    print(s, end=" ")
    for neighbor in neighbors:
        if not graph.visited[neighbor]:
            dfs_recc(graph, neighbor)


def bfs(graph, s):
    queue = deque()
    queue.append(s)
    while queue:
        u = queue.popleft()
        graph.visited[u] = True
        print(u, end=" ")
        for v in get_neighbours(graph, u):
            if not graph.visited[v]:
                queue.append(v)


def dfs_iter(graph, s):
    stack = deque()
    stack.append(s)
    while stack:
        u = stack.pop()
        print(u, end=" ")
        graph.visited[u] = True
        for v in get_neighbours(graph, u):
            stack.append(v)


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
    for u in range(graph.size):
        for v in range(graph.size):
            if graph.matrix[u][v]:
                f.write('"{}" -> "{}"\n'.format(u, v))


def print_matrix(graph):
    for u in range(graph.size):
        for v in range(graph.size):
            print(1 if graph.matrix[u][v] else 0, end=" ")
        print()


# acyclic
def create_test_graph1():
    graph = Graph(7)
    graph.matrix[0][1] = True
    graph.matrix[0][2] = True
    graph.matrix[0][4] = True
    graph.matrix[1][3] = True
    graph.matrix[1][5] = True
    graph.matrix[2][6] = True

    return graph


# cyclic
def create_test_graph2():
    graph = Graph(6)
    graph.matrix[0][1] = True
    graph.matrix[0][5] = True
    graph.matrix[1][2] = True
    graph.matrix[1][3] = True
    graph.matrix[1][5] = True
    graph.matrix[2][5] = True
    graph.matrix[2][4] = True
    graph.matrix[4][1] = True
    graph.matrix[4][3] = True
    graph.matrix[5][4] = True

    return graph


# acyclic
def create_test_graph3():
    graph = Graph(4)
    graph.matrix[0][1] = True
    graph.matrix[1][2] = True
    graph.matrix[2][3] = True
    graph.matrix[0][2] = True

    return graph


def test_dfs():
    print("Test 1. recursive dfs:")
    graph1 = create_test_graph1()
    make_graph(graph1, "graph1.dot")
    dfs_recc(graph1, 0)
    print()

    graph2 = create_test_graph2()
    make_graph(graph2, "graph2.dot")
    dfs_iter(graph2, 0)
    print()

    graph3 = create_test_graph3()
    dfs_recc(graph3, 0)
    print()


def test_bfs():
    print("Test 2. BFS:")
    graph1 = create_test_graph1()
    bfs(graph1, 0)
    print()

    graph2 = create_test_graph2()
    bfs(graph2, 0)
    print()

    graph3 = create_test_graph3()
    bfs(graph3, 0)
    print()


if __name__ == '__main__':
    test_dfs()
    test_bfs()
