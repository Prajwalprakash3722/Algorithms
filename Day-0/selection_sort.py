"""
Day-0 (28/05/2021)
Insertion sort 
Author: Prajwal Prakash
Time complexity:
"""


def selection_sort(list1, n):
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if list1[min_index] > list1[j]:
                min_index = j
                list1[i], list1[min_index] = list1[min_index], list1[i]
                return list1

###############################################################################
# Driver Code
list1 = [10, 5, 13, 8, 2]
n = len(list1)
print("The unsorted list is:", list1)
print("The sorted list1 is:", selection_sort(list1, n))
