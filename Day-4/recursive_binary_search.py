"""
Day-4 (01/05/2021)
Recursive Binary Search
Author: Prajwal Prakash
Time complexity:
Data structures used:
Result: Successful
"""
import doctest


def recursive_binary_search(list, element):
    """
    >>> recursive_binary_search([0,2,4,6,8,10,12],8)
    True
    >>> recursive_binary_search([1,3,5,7,9,11,13,15],9)
    True
    >>> recursive_binary_search([1,2,3,4,5,6,7,8,9,10], 11)
    False
    >>> recursive_binary_search([14,25,31,42,51,63,74,85,96,100], 3)
    False
    """
    if len(list) == 0:
        return False
    midpoint = len(list)//2
    if list[midpoint] == element:
        return True
    else:
        if list[midpoint] < element:
            return recursive_binary_search(list[midpoint+1:], element)
        else:
            return recursive_binary_search(list[:midpoint], element)


if __name__ == '__main__':
    doctest.testmod()
###############################################################################SS
