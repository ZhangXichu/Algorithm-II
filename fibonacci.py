
def fib1(n):
    # Memorization - top-down
    mem = [None]*(n+1)

    def _fib1(n):
        if mem[n] is None:
            mem[n] = n if n < 2 else _fib1(n - 1) + _fib1(n - 2)
        return mem[n]
    return _fib1(n)


def fib2(n):
    # Tabulation - bottom-up
    mem = [0,1]
    for i in range(2, n+1):
        mem.append(mem[i-1] + mem[i-2])
    return mem[n]


print([fib1(i) for i in range(10)])
print([fib2(i) for i in range(10)])
