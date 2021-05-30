"""
This is a pure implementation of exponential Search in python
https://en.wikipedia.org/wiki/Exponential_search

For manual testing run:

python3 exponential_search.py

Time complexity: o(logN)


"""


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
    while (key< array_size and sorted_array[key] < key):
        key *=2
        return binary_search(sorted_array, key/2, min(key+1, array_size))