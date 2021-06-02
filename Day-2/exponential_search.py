"""
This is a pure implementation of exponential Search in python
https://en.wikipedia.org/wiki/Exponential_search

For manual testing run:

python3 exponential_search.py

Time complexity: o(logN)


"""
import doctest


def binary_search(list: list, element: int) -> int:
    """
    Defining the binary search function before exponential search function
    :param list: a list of elements which are sorted in increasing order. (list)
    :param element: a item to search in the sorted_array. (int) 
    :param return: index of of the target element if found in the list or none if item is not found.
    """
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


def exponential_search(sorted_array: list, target_element: int) -> int:
    """
    :param sorted_array: a list of elements which are sorted in increasing order. (list)
    :param target_element: a item to search in the sorted_array. (int) 
    :param return: index of of the target element if found in the list or -1 if item is not found.

    Examples:
    >>> exponential_search([2,4,7,9,14], 2)
    0  
    """
    array_size = len(sorted_array)
    if array_size == 0:
        return -1
    key = 1
    while (key < array_size and sorted_array[key] < key):
        key *= 2
        return binary_search(sorted_array, key/2, min(key+1, array_size))


if __name__ == '__main__':
    doctest.testmod()
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
print("The element in list is found at :", exponential_search(arr, x))

print("Process finished --- %s seconds ---" % (time.time() - start_time))
