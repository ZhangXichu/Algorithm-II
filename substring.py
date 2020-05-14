def max_suffix(string1, string2, i, j):
    """
    Function returns the maximum length of suffix of string2 in string1 as subsequence
    :param string1:
    :param string2:
    :param i: initially length of string1
    :param j: initially length of string2
    :return: max length of suffix
    """
    if i < 0 or j < 0:
        return 0

    if string1[i] == string2[j]:
        return 1 + max_suffix(string1, string2, i - 1, j - 1)
    return max_suffix(string1, string2, i - 1, j)


def max_suffix_bottom_up(string1, string2):
    res_suffix = ""
    counter = len(string1) - 1
    for i in range(len(string2) - 1, -1, -1):
        for j in range(counter, -1, -1):
            # print("counter:", counter)
            if string2[i] == string1[j]:
                res_suffix = string1[j] + res_suffix
                break
            counter -= 1
    return res_suffix


# print("")
# exit()
def build_table(string1, string2):
    table = dict()
    for i in range(-1, len(string2)):
        for j in range(-1, len(string1)):
            table[i, j] = 0
    return table


def print_table(len1, len2, table):
    for i in range(-1, len2):
        for j in range(-1, len1):
            print(table[i, j], end=" ")
        print()


def get_solution(substring, max_suffix_len):
    return substring[len(substring) - max_suffix_len: len(substring)]


def max_non_supersequence(string1, string2, table):
    """
    Function finds length of the longest subsequence in string1 which is not supersequence of string2
    :param string1:
    :param string2:
    :param table: a dictionary data structure to memorize the configurations
    :return:
    """

    for i in range(0, len(string2)):
        for j in range(0, len(string1)):
            if string2[i] != string1[j]:
                table[i, j] = max(table[i - 1, j - 1], table[i - 1, j], table[i, j - 1]) + 1  # table[i - 1, j],
            else:
                table[i, j] = max(table[i - 1, j - 1], table[i - 1, j], table[i, j - 1])  # , table[i - 1, j]
            # table[i, j] = min(table[i, j], i)
            # print(table[i, j], end=' ')
        # print()
    print_table(len(string1), len(string2), table)
    return table[len(string2) - 1, len(string1) - 1]


# def max_non_supersequence_new(string1, string2): # string2 is the sub string
#     res = ""
#     for i in range(string2):



def min_deletion(string1, string2, table):
    if len(string2) == 0:
        return len(string1)
    return len(string1) - max_non_supersequence(string1, string2, table)


########################################
######## Tests #########################
########################################


def test_longest_suffix():
    print("##########################################")
    print("##########  test_longest_suffix  #########")
    print("##########################################")

    # string2 is substring of string1
    string1 = "abbacad"  # M
    string2 = "bcd"  # A
    res = max_suffix(string1, string2, len(string1) - 1, len(string2) - 1)
    print(res)
    print(get_solution(string2, res))
    print("Bottom up version: ")
    res_b = max_suffix_bottom_up(string1, string2)
    print('res_b', res_b)

    # string 3 is not substring of string1, but a longest suffix can be found
    string3 = "fcfad"
    res2 = max_suffix(string1, string3, len(string1) - 1, len(string3) - 1)
    print(res2)
    print(get_solution(string3, res2))
    print("Bottom up version: ")
    res_b2 = max_suffix_bottom_up(string3, "abca")
    print('res_b2', res_b2)

    # string 4 is not substring of string1, and there's no longest suffix
    string4 = "eafg"
    res3 = max_suffix(string1, string4, len(string1) - 1, len(string4) - 1)
    print(res3)
    print(get_solution(string4, res3))

    string5 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    res4 = max_suffix(string5, string5, len(string5) - 1, len(string5) - 1)
    print(res4)
    print(get_solution(string5, res4))


def test_max_non_supersequence():
    print("##########################################")
    print("#######  test_max_non_supersequence  #####")
    print("##########################################")

    string1 = "NAANNNANN"
    string2 = "NANA"
    table = build_table(string1, string2)
    res1 = min_deletion(string1, string2, table)
    print("res1", res1)
    print(table)

    string4 = "ABBCADCB"
    string5 = "ABB"
    table = build_table(string4, string5)
    res2 = min_deletion(string4, string5, table)
    print("res2", res2)
    print(table)

    string4 = "ABBCADCB"
    string5 = "ABBC"
    table = build_table(string4, string5)
    res2 = min_deletion(string4, string5, table)
    print("res3", res2)
    print(table)

    string3 = ""
    table = build_table(string1, string3)
    res1 = min_deletion(string1, string3, table)
    print("res3", res1)
    # print(table)


def main():
    table = build_table("ABBCADCB", "ABB")
    print_table(8, 3, table)
    # test_longest_suffix()
    test_max_non_supersequence()


if __name__ == '__main__':
    main()
