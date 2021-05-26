# def solution(S):
#     # write your code in Python 3.6
#     consonants = "BCDFGHJKLMNPQRSTVWXYZ"
#     vowels = "AEIOU"
#     input_length = len(S)
#     consonants_list = []
#     vowels_list = []
#     for char in S:
#         if char in consonants:
#             consonants_list.append(char)
#         else:
#             vowels_list.append(char)
#     if input_length % 2 == 0:
#         if len(consonants_list) < input_length // 2:
#             return 0 % (1e9 + 7)
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(4))

a = {"g": 2, "g": 6}
print(a.values())