

"""
Link by rank
"""


# find the root of the tree (subset), which x belongs to
def find(parent, x):
    while not x == parent[x]:
        x = parent[x]
    return x


# union of two subsets
def union(parent, rank, x, y):
    r = find(parent, x)
    s = find(parent, y)
    if r == s:
        return
    elif rank[r] > rank[s]:
        parent[s] = r
    elif rank[r] < rank[s]:
        parent[r] = s
    else:
        parent[r] = s
        rank[s] += 1


def make_graph(parent, filename):
    with open(filename, 'w') as f:
        f.write("digraph MyGraph {\n")
        make_graphviz(parent, f)
        f.write("}\n")


def make_graphviz(parent, f):
    for i in range(len(parent)):
        f.write('"{}" -> "{}"\n'.format(i, parent[i]))


def main():
    # array representation of the set tree
    parent1 = [7, 5, 7, 8, 8, 7, 5, 7, 8, 8]
    rank1 = [1, 0, 1, 0, 0, 1, 0, 2, 0, 1]
    make_graph(parent1, "graph1.dot")
    union(parent1, rank1, 7, 8)
    make_graph(parent1, "union1.dot")


if __name__ == '__main__':
    main()
