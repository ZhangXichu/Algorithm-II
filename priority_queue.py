def get_left_child(n, i):
    if 2 * i + 1 <= n:
        return 2 * i + 1  # returns index of left child
    return None


def get_right_child(n, i):
    if 2 * i + 2 <= n:
        return 2 * i + 2  # index
    return None


def get_parent(i):
    if i > 0:
        return (i - 1) // 2  # index
    return None


def is_right_child(n, i):
    p = get_parent(i)
    return get_right_child(n, p) == i


def is_left_child(n, i):
    p = get_parent(i)
    return get_left_child(n, p) == i


def heapify_up(min_heap, i):
    # print("index parent: ", get_parent(i))
    if not (get_parent(i) is None):
        p = get_parent(i)
        if is_left_child(len(min_heap), i):
            sibling = get_right_child(len(min_heap), p)
        else:
            sibling = get_left_child(len(min_heap), p)
        # print("p: {0}, sibling: {1}, i: {2}".format(p, sibling, i))
        smallest = min(min_heap[p], min_heap[sibling], min_heap[i])
        index_min = p
        for index in [p, sibling, i]:
            if min_heap[index] == smallest:
                index_min = index
        temp = min_heap[p]
        min_heap[p] = smallest
        min_heap[index_min] = temp
        heapify_up(min_heap, p)


def main():
    min_heap = [5, 8, 11, 10, 15, 7, 3]
    heapify_up(min_heap, len(min_heap)-1)
    print(min_heap)


if __name__ == '__main__':
    main()