import unittest

# Program that finds the length of the longest increasing subsequence of an input array.
def naive_longest_sub(arr):
    max_length = 1
    for i in range(0, len(arr)):
        curr = arr[i]
        count = 1
        for j in range(i + 1, len(arr)):
            if arr[j] > curr:
                curr = arr[j]
                count += 1
        if count > max_length:
            max_length = count
    return max_length

# Test cases for longest increasing subsequence
class MyTests(unittest.TestCase):
    def test(self):
        # Sample test cases.
        self.assertEqual(1, naive_longest_sub([3, 2])) # LIS = [3] or [2]
        self.assertEqual(3, naive_longest_sub([3, 10, 2, 1, 20])) # LIS = [3, 10, 20]
        self.assertEqual(4, naive_longest_sub([50, 3, 10, 7, 40, 80])) # LIS = [3, 7, 40, 80]

        # Testing if large number in the middle
        self.assertEqual(4, naive_longest_sub([3, 100, 5, 6, 7])) # LIS = [3, 5, 6, 7]        

if __name__ == '__main__':
    unittest.main()