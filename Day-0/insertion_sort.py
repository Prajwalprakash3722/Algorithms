"""
Day-0 (28/05/2021)
Insertion sort 
Author: Prajwal Prakash
Time complexity:
"""


def insertion_sort(list1):

    for i in range(1, len(list1)):
        key_element = list1[i]
        j = i-1
        for x in list1:
            while j >= 0:
                if x > key_element:
                    x, key_element = key_element, x
                return list1


###############################################################################
# Driver Code
list1 = [10, 5, 13, 8, 2]
n = len(list1)
print("The unsorted list is:", list1)
print("The sorted list1 is:", insertion_sort(list1, n))
