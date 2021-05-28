"""
Day-0 (28/05/2021)
Bubble sort 
Author: Prajwal Prakash
Time complexity:
Data structures used: 
"""


def bubble_sort(list1, n):
    
    for i in range(1, n):
        for j in range(n-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
                return list1


###############################################################################
# Driver Code
list1 = [10, 5, 13, 8, 2]
n = len(list1)
print("The unsorted list is:", list1)
print("The sorted list1 is:", bubble_sort(list1, n))