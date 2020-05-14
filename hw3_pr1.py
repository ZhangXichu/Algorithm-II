import math, heapq
from collections import namedtuple

Edge = namedtuple('Edge', ['u', 'v', 'weight'])


class Graph:

    def __init__(self, size):
        self.size = size
        self.distances = []
        self.predecessors = []
        # self.matrix = [[math.inf] * size for _ in range(size)]
        self.all_roads = []  # implementation without matrix
        self.broken_roads = []


def add_edge(graph, u, v, w):
    if 0 <= u < graph.size and 0 <= v < graph.size:
        # graph.matrix[u][v] = w
        graph.all_roads.append(Edge(u, v, w))


def add_broken_road(graph, u, v, w):
    graph.broken_roads.append(Edge(u, v, w))


# def is_edge(graph, u, v):
#     return graph.matrix[u][v] != math.inf

def is_edge(e):
    return e[2] != math.inf


# def is_good_road(graph, u, v):
#     # the road also shouldn't be brocken (weight = -1)
#     return is_edge(graph, u, v) and graph.matrix[u][v] != -1

def is_good_road(e):
    # the road also shouldn't be brocken (weight = -1)
    return is_edge(e) and e[2] != -1


def initialize(graph, s):
    graph.distances = [math.inf] * graph.size
    graph.predecessors = [None] * graph.size
    graph.distances[s] = 0


# def relax(graph, u, v):
#     # uodate shortest distance from starting point
#     relaxed_distance = graph.distances[u] + graph.matrix[u][v]
#
#     if graph.distances[v] > relaxed_distance:
#         graph.distances[v] = relaxed_distance
#         graph.predecessors[v] = u
#         return True
#
#     return False


def relax(graph, e):
    # uodate shortest distance from starting point
    u = e[0]
    v = e[1]
    w = e[2]

    relaxed_distance = graph.distances[u] + w

    if graph.distances[v] > relaxed_distance:
        graph.distances[v] = relaxed_distance
        graph.predecessors[v] = u
        return True

    return False


# def dijkstra(graph, s):
#     initialize(graph, s)
#
#     done = [False for _ in range(graph.size)]
#     heap = [(0, s)]  # pair: (distance, vertex)
#
#     while heap:
#         _, x = heapq.heappop(heap)
#
#         if done[x]:
#             continue
#
#         done[x] = True
#
#         for y in range(graph.size):
#             # if not done[y] and is_edge(graph, x, y) and relax(graph, x, y):
#             if not done[y] and is_good_road(graph, x, y) and relax(graph, x, y):
#                 heapq.heappush(heap, (graph.distances[y], y))
#
#     return graph.distances, graph.predecessors

def get_weight(u, v, graph):
    for e in graph.all_roads:
        if e[0] == u and e[1] == v:
            return e[2]
    return math.inf


def dijkstra(graph, s):
    initialize(graph, s)

    done = [False for _ in range(graph.size)]
    heap = [(0, s)]  # pair: (distance, vertex)

    while heap:
        _, x = heapq.heappop(heap)

        if done[x]:
            continue

        done[x] = True

        for y in range(graph.size):
            # if not done[y] and is_edge(graph, x, y) and relax(graph, x, y):
            e = Edge(x, y, get_weight(x, y, graph))
            if not done[y] and is_good_road(e) and relax(graph, e):
                heapq.heappush(heap, (graph.distances[y], y))

    return graph.distances, graph.predecessors


# O(V + E)
def reverse_graph(graph):
    res_graph = Graph(graph.size)

    # for i in range(graph.size):
    #     for j in range(graph.size):
    #         if is_edge(graph, i, j):
    #             res_graph.matrix[j][i] = graph.matrix[i][j]

    # implementation without matrix
    for e in graph.all_roads:
        add_edge(res_graph, e[1], e[0], e[2])

    return res_graph


# whether a node is reachable from starting point
def reachable(distances, v):
    return distances[v] != math.inf


def opt_road(graph, s, t):
    # s: city1, t: city2
    # set weight of brocken road to -1
    distances_s, _ = dijkstra(graph, s)
    distances_t, _ = dijkstra(reverse_graph(graph), t)

    # print(distances_s)
    # print(distances_t)

    minimum_distance = math.inf
    for e in graph.broken_roads:
        u = e[0]
        v = e[1]
        w = e[2]

        # print("u:", u, "v:", v)

        if reachable(distances_s, u) and reachable(distances_t, v):
            minimum_distance = min(minimum_distance, distances_t[v] + distances_s[u] + w)

    print(minimum_distance)

    return minimum_distance


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
            if graph.matrix[u][v] != math.inf:
                f.write('"{}" -> "{}"\n'.format(u, v))


# def print_matrix(graph):
#     for u in range(graph.size):
#         for v in range(graph.size):
#             # print(1 if graph.matrix[u][v] else 0, end=" ")
#             print(graph.matrix[u][v], end=" ")
#         print()


def create_test_graph1():
    graph = Graph(6)
    for u, v, w in ((0, 1, 1), (0, 5, 2), (1, 5, 3),
                    (1, 2, 7), (4, 5, 4),
                    (1, 4, 11), (2, 5, 1), (2, 4, 12),
                    (2, 3, 13), (3, 4, 3)):
        add_edge(graph, u, v, w)

    return graph


# brocken roads
def create_test_graph2():
    graph = Graph(6)
    for u, v, w in ((0, 1, 1), (0, 5, 2), (1, 5, 3),
                    (1, 2, -1), (4, 5, 4),
                    (1, 4, 11), (2, 5, -1), (2, 4, 12),
                    (2, 3, 13), (3, 4, 3)):
        add_edge(graph, u, v, w)

    add_broken_road(graph, 1, 2, 7)
    add_broken_road(graph, 2, 5, 11)

    return graph


def test_dijkstra():
    print("Test: Dijkstra algorithm: ")

    graph1 = create_test_graph1()
    # make_graph(graph1, "graph1.dot")
    # print_matrix(graph1)
    ret = dijkstra(graph1, 0)
    print(ret)

    graph2 = create_test_graph2()
    # print_matrix(graph2)
    opt_road(graph2, 0, 3)


def main():
    test_dijkstra()


if __name__ == '__main__':
    main()
