"""
Day-1 (29/05/2021)
Binary sort
Author: Prajwal Prakash
Time complexity:
Data structures used:
Result: Successful
"""
import time


def binary_search(list, element):

    start = 0
    last = len(list) - 1
    while start <= last:
        key_element_index = int((start + last) // 2)
        key_element = list[key_element_index]
        if x == key_element:
            return key_element_index

        elif key_element < element:
            start = key_element_index + 1

        else:
            last = key_element_index - 1


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
x = 101
start_time = time.time()
print("The element in list is found at :", binary_search(arr, x))

print("Process finished --- %s seconds ---" % (time.time() - start_time))
