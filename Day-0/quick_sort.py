"""
Day-0 (28/05/2021)
Quick sort 
Author: Prajwal Prakash
Time complexity:
Data structures used: 
"""


def quick_sort(list1, low, high):
    
    for i in range(1, len(list1)):
        pivot = list1[i]
        if low > pivot and high < pivot:
            list1[0], list1[-1] = list1[-1], list1[0]
            return (list1, pivot)


###############################################################################
# Driver Code
list1 = [10, 5, 13, 8, 2]
low = list1[0]
high = list1[-1]
print("The unsorted list is:", list1)

print("The sorted list1 is:", quick_sort(list1, low, high))
