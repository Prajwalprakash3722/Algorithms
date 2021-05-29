"""
Day-0 (28/05/2021)
Insertion sort
Author: Prajwal Prakash
Time complexity:
"""


def insertion_sort(list1, low, high):

    for i in range(1, len(list1)):
        key_element_index = i
        j = i-1
        key_element = list1[key_element_index]
        while i > 0 and list1[j] > key_element:
            list1[i] = list1[j]
            j -= 1
            list1[i] = key_element
            return list1


###############################################################################
# Driver Code
list1 = [4, 22, 41, 40, 27, 30, 36, 16, 42,
         37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
n = len(list1)
low = 0
high = len(list1) - 1
print("The unsorted list is:", list1)
print("The sorted list1 is:", insertion_sort(list1, low, high))
>>> 5