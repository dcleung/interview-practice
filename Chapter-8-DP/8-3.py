import unittest

# Magic Index: A magic index in an array A[1. .. n-1] is defined to be an index such that A[ i]
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

# We leverage the invariant that our input array is sorted and that every entry is an integer.
# Start at median, then compare, and recurse depending if the median greater/less than the index.

# The running time is O(log n) because we will ever search one half of the array in the recursive call,
# thus the recurrence is T(n) = T(n/2) + 1 for recursing and comparing.  This results in O(log n).

def recurse_find_index(array, lo, hi):
    index = (lo + hi) / 2 # This gives us the middle index
    value = array[index] # This gives us the median value
    if index == value:
        return True # Establish the base case for True
    elif lo == hi:
        return False # Estblish the base case for False
    elif index > value:
        return recurse_find_index(array, index + 1, hi)
    else:
        return recurse_find_index(array, lo, index)

# Call the recursive method
def find_index(array):
    return recurse_find_index(array, 0, len(array))

# Test cases for find magic index.
class MyTests(unittest.TestCase):
    def test(self):
        # Everything is a "magic index".
        self.assertTrue(find_index([0, 1, 2]))

        # Magic index is last index.
        self.assertTrue(find_index([-6, -5, 2]))

        # Magic index does not exist.
        self.assertFalse(find_index([1, 2, 3]))

if __name__ == '__main__':
    unittest.main()