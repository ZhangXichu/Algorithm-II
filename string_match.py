# this one works with text which only contains number
# if there is a text which contains other symbols, we can map them to digits
# (given that the alphabet has size <= 10)
def number_search(text, pattern):
    m, n = len(pattern), len(text)
    base_ten = 10 ** (m - 1)
    p = 0
    t = 0
    # preprocessing: precalculate the number representation starting from
    # each digit
    for i in range(m):
        p = 10 * p + int(pattern[i])
        t = 10 * t + int(text[i])
    for s in range(n - m + 1):
        if p == t:
            return s
        # calculate the next number representation
        t = 10 * (t - base_ten * int(text[s])) + int(text[s + m])
    return None


# metaphorically described as FA
def knuth_morris_pratt(text, pattern):
    j = 0
    n, m = len(text), len(pattern)
    fail = compute_opt_failure(pattern)
    for i in range(n):
        while j >= 0 and not text[i] == pattern[j]:
            j = fail[j]
        # print("j: ", j)
        if j == m - 1:
            return i - m + 1
        j = j+1
    return -1


def compute_failure(pattern):
    m = len(pattern)
    fail = [-1] * m
    j = -1  # initial state of FA
    for i in range(1, m):
        j += 1  # j points to the prefix
        fail[i] = j
        if pattern[i] != pattern[j]:  # mismatch, move cursor j back to the begin
            while j >= 0:
                j = fail[j]
    return fail


def compute_opt_failure(pattern):
    m = len(pattern)
    fail = [-1] * m
    j = -1
    for i in range(m):
        if pattern[i] == pattern[j]:  # saves work if pattern[j] is the same as pattern[fail[j]]
            fail[i] = fail[j]
        else:
            fail[i] = j
        while j >= 0 and (not pattern[i] == pattern[j]):
            j = fail[j]
        j += 1
    return fail

