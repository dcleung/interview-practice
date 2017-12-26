import unittest

# Magic Index: A magic index in an array A[1. .. n-1] is defined to be an index such that A[ i]
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

# We leverage the invariant that our input array is sorted and that every entry is an integer.
# This means, if we encounter an entry that is greater than index, every entry afterwards is > index.
# This runs in O(n) time, because worst case, our entry could be the last entry in the array.
def find_index(array):
    for i in range(0, len(array)):
        if array[i] == i:
            return True
        elif array[i] > i:
            return False
    return False

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