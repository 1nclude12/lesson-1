# def get_len_word(word):  # 0(2 * N) - O(N)
#     dict = {}
#     for i in word:
#         dict[i] = dict.get(i, 0) + 1
#     for j in dict:
#         print(j, dict[j])
#
#
# print(get_len_word("asfasgf"))
#
#
# def get_len_str(str):  # O(N ** 2)
#     for sym in str:
#         count = 0
#         for n_sym in str:
#             if n_sym == sym:
#                 count += 1
#         print(sym, count)
#
#
# print(get_len_str("asdsad"))


# def func(s):
#     for i in s:
#         print(i, s.count(i))
#
#
# print(func("asgzdcssss"))


def get_len(str):  # O(N * M) (М - количество символов в множестве)
    for i in set(str):
        print(i, str.count(i))


print(get_len("aassda"))
# set - неупорядочное множество
