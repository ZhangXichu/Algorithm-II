from collections import deque

# Cviceni 9

"""
Mame tri nadoby velikost 10 l, 7 l a 4 l. Sedmilitrova a ctyrlitrova
nadoba jsou na pocatku plne a desetilitrova nadoba je prazdna.
Chceme prelvanm doclit toho, aby v sedmilitrové nebo ve
čtyřlitrové nádobě byly přesně 2 litry. Nemáme však jiný způsob
měření objemu a nechceme nic odhadovat, přelívání z nádoby A do
nádoby B tedy může probbíhat jen tak, že bud' se vyprázdní nádoba
A nebo se zcela naplní nádoba B. Je rovněž zakázáno vodou plýtvat
a vylívat ji mimo nádoby.
"""


def pour_water(x, y, max_y):
    if x == 0 or y == max_y:
        return x, y

    # less free space in y then liquid in x
    if max_y - y < x:
        new_x = x - (max_y - y)
        new_y = max_y
    else:
        new_x = 0
        new_y = y + x

    return new_x, new_y


def next_states(state):
    states = set()

    a = state[0]
    b = state[1]
    c = state[2]

    max_a = 10
    max_b = 7
    max_c = 4

    # a -> b
    states.add((pour_water(a, b, max_b)[0], pour_water(a, b, max_b)[1], c))
    # b -> a
    states.add((pour_water(b, a, max_a)[1], pour_water(b, a, max_a)[0], c))
    # a -> c
    states.add((pour_water(a, c, max_c)[0], b, pour_water(a, c, max_c)[1]))
    # c -> a
    states.add((pour_water(c, a, max_a)[1], b, pour_water(c, a, max_a)[0]))
    # b -> c
    states.add((a, pour_water(b, c, max_c)[0], pour_water(b, c, max_c)[1]))
    # c -> b
    states.add((a, pour_water(c, b, max_b)[1], pour_water(c, b, max_b)[0]))

    return states


def bfs(s, visited, pairs):  # pairs of two consecutive states
    queue = deque()
    queue.append(s)
    solution = []
    while queue:
        u = queue.popleft()
        visited.add(u)
        if u[1] == 2 or u[2] == 2:
            solution.append(u)
        for v in next_states(u):
            if v not in visited:
                pairs.append((u, v))
                queue.append(v)
    return solution


def get_path(pairs, config):
    path = [config]
    final = config
    while final != (0, 7, 4):
        for pair in pairs:
            if pair[1] == final:
                path.insert(0, pair[0])
                final = pair[0]
                break
    return path


def main():
    visited = {(0, 7, 4)}
    pairs = []
    solution = bfs((0, 7, 4), visited, pairs)
    print("solution:", solution)
    for s in solution:
        print(get_path(pairs, s))


if __name__ == '__main__':
    main()
