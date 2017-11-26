import unittest

# Method to see if a string is a permuation of a palindrome.
# We first note that a string can be a palindrome iff it has
# at most one character whose count is odd.
def isPalindromePermutation(input):
    # Initialize dictionary for counts.
    dict = {}
    # Count up the number of occurences for each character.
    for c in input.lower():
        if c == ' ':
            continue
        if dict.has_key(c):
            dict[c] = dict[c] + 1
        else:
            dict[c] = 1
    # Boolean that keeps track if we have found the one odd count.
    found = False
    for key, value in dict.items():
        # Found a odd count.
        if value % 2 == 1:
            # It is the only odd count so far.
            if not found:
                found = True
            # It is not the only odd count => not a permutation.
            else:
                return False
    return True

# Testing suite for isPalindromePermutation.
class MyTests(unittest.TestCase):
    def test(self):
        # Sample test case.
        self.assertTrue(isPalindromePermutation('Tact Coa'))
        # Empty string is a permutation.
        self.assertTrue(isPalindromePermutation(''))
        # Single letter is a permutation.
        self.assertTrue(isPalindromePermutation('L'))
        # Odd number of letter is a permutation.
        self.assertTrue(isPalindromePermutation('aaa'))
        # Multiple odd counts is not a permutation.
        self.assertFalse(isPalindromePermutation('baaabb'))
        # Multiple odd counts is not a permutation with upepr case.
        self.assertFalse(isPalindromePermutation('AB C ccb'))
    
if __name__ == '__main__':
    unittest.main()
