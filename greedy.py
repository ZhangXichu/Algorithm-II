from fractions import Fraction as frac
import portion as P


def minimum_s(arr):
    s = []
    # start from the leftmost (smallest) element in arr
    interval = P.closed(arr[0], arr[0] + 1)
    s.append(interval)
    for i in range(len(arr) - 1):
        if not arr[i] in interval:
            interval = P.closed(arr[i], arr[i] + 1)
            i += 1
            s.append(interval)
    return s


def main():
    arr = [frac(1, 2), 1, frac(4, 3), frac(5, 3), 2, frac(8, 3)]
    s = minimum_s(arr)
    print(s)

    arr2 = [frac(11, 10), frac(5, 3), frac(11, 6), frac(13, 6), frac(7, 3), frac(17, 6)]
    s = minimum_s(arr2)
    print(s)


if __name__ == '__main__':
    main()