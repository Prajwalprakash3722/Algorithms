"""
Day-1 (29/05/2021)
Binary sort 
Author: Prajwal Prakash
Time complexity:
Data structures used:
Result: Successful 
"""

def binary_search(list, element):
    
    start = 0
    last  = len(list) - 1
    key_element_index = int((start + last)//2)
    key_element = list[key_element_index]
    if x == key_element:
        return key_element_index
    else:
        if key_element > element:
            for i in range(key_element_index):
                if list[i] == element:
                    return i
        else:
            for i in range(key_element_index, len(list)):
                if list[i] == element:
                    return i

###############################################################################
# Driver Code
arr = [2, 3, 5, 8, 9]
x = 9
print("The element in list is found at :", binary_search(arr, x))