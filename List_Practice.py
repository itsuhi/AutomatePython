import numpy as np
import matplotlib.pyplot as plt

"""
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma
and a space, with and inserted before the last item. For example, passing the previous spam list to the function would
return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.
Be sure to test the case where an empty list [] is passed to your function.
"""


def list_to_string(lst):
    length = len(lst)
    result = ""
    if length == 0:
        return ""
    elif length == 1:
        result = result + lst[0]
        return result
    else:
        for i in range(length-1):
            result = result + lst[i] + ", "
        result = result + "and " + lst[-1]
        return result

# print(list_to_string(['apples']))


# ======================================================================================================================
"""
Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated 
list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of rando-
mly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this code in 
a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak 
of six heads or tails in a row.
"""


# streaks = []
# simulation = 10000
# for i in range(simulation):
#     no_streaks = 0
#     flip_result = list(np.random.randint(0, 2, 100))
#     # check for 5 consecutive 0 or 1
#     for idx in range(0, 95):
#         if idx == 94:
#             if len(set(flip_result[idx:])) == 1:
#                 no_streaks = no_streaks + 1
#         else:
#             if len(set(flip_result[idx:idx+6])) == 1:
#                 no_streaks = no_streaks + 1
#     streaks.append(no_streaks)
# plt.hist(streaks, bins=np.arange(0, 20, 1))
# plt.show()

# ======================================================================================================================
"""
Character Picture Grid
"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y], end="")
    print("")



