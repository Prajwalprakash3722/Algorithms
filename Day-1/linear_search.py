"""
Day-1 (29/05/2021)
Binary sort 
Author: Prajwal Prakash
Time complexity: Process finished --- 2.8371810913085938e-05 seconds ---
Data structures used:
Result: Successful 
"""
import time


def linear_search(list, element):
    for i in range(len(list)):
        if element == list[i]:
            return i


###############################################################################
# Driver Code
arr = [
    2,
    3,
    5,
    8,
    9,
    11,
    22,
    56,
    45,
    56,
    59,
    60,
    62,
    65,
    68,
    69,
    74,
    75,
    78,
    79,
    80,
    81,
    83,
    84,
    87,
    89,
    90,
    92,
    95,
    97,
    99,
    100,
]
x = 79
start_time = time.time()
print("The element in list is found at :", linear_search_2(arr, x))

print("Process finished --- %s seconds ---" % (time.time() - start_time))
