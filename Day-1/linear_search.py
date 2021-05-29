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
arr = [2, 3, 5, 8, 9, 11, 22, 56, 45, 56, 59]
x = 59
start_time = time.time()
print("The element in list is found at :", linear_search(arr, x))

print("Process finished --- %s seconds ---" % (time.time() - start_time))
