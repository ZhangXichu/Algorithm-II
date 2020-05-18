from collections import deque


class Record:
    def __init__(self, size, rank):
        self.size = size
        self.rank = rank  # m in w_pref_lists
        self.current = [None] * size
        self.freemen = [i for i in range(size)]


def init_record(w_pref_lists):
    size = len(w_pref_lists[0])
    rank = [[0] * size for _ in range(size)]
    i = 0
    for lst in w_pref_lists:
        rank_m = 1
        for m in lst:
            rank[i][m] = rank_m
            rank_m += 1
        i += 1
    print(rank)
    return Record(size, rank)


def propose(m_pref_lists, record):
    current = record.current
    freemen = record.freemen
    rank = record.rank
    while len(freemen) > 0:
        print(freemen)
        free_m = freemen[0]
        lst = m_pref_lists[free_m]  # lst[0]: highest ranked w on m_pref_lst
        w_h = lst[0]
        if current[w_h] is None:
            current[w_h] = free_m
            freemen.remove(free_m)
        else:
            if rank[w_h][free_m] < rank[w_h][current[w_h]]:
                freemen.append(current[w_h])
                current[w_h] = free_m
                freemen.remove(free_m)
        lst.remove(w_h)


def stable_match(m_pref_lists, w_pref_list):
    record = init_record(w_pref_list)
    propose(m_pref_lists, record)
    return record


def main():
    m_pref_lists = [[0, 1], [0, 1]]
    w_pref_lists = [[1, 0], [0, 1]]
    record = stable_match(m_pref_lists, w_pref_lists)
    print("current: ", record.current)

    m_pref_lists = [[2, 1, 0], [1, 2, 0], [2, 1, 0]]
    w_pref_lists = [[0, 1, 2], [0, 1, 2], [0, 2, 1]]
    record = stable_match(m_pref_lists, w_pref_lists)
    print("current: ", record.current)


if __name__ == '__main__':
    main()