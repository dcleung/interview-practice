import unittest

# Method to see if two strings are at least one character away from each other.
def isOneAway(str1, str2):
    # If same string then must be true.
    if str1 == str2:
        return True
    # If lengths not within one, then cannot be one char away.
    if len(str1) <= len(str2) + 1 and len(str1) >= len(str2) + 1:
        return False
    # Get the longer and shorter strings properly assigned.
    if len(str1) >= len(str2):
        longer = str1
        shorter = str2
    else:
        longer = str2
        shorter = str1
    hash = {}
    # Hash all the characters in the longer string.
    for c in longer:
        if hash.has_key(c):
            hash[c] = hash[c] + 1
        else:
            hash[c] = 1
    # Flag for if we found the one difference so far.
    flag = False
    # Iterate all strings in the shorter string.
    for d in shorter:
        if hash.has_key(d):
            hash[d] = hash[d] - 1
            if hash[d] == 0:
                del(hash[d])
        else:
            if flag:
                return False
            else:
                flag = True
    print(hash)
    if len(hash) >= 2:
        return False
    return True

# Testing suite for isPalindromePermutation.
class MyTests(unittest.TestCase):
    def test(self):
        # Sample test cases.
        self.assertTrue(isOneAway('pale', 'ple'))
        self.assertTrue(isOneAway('pales', 'pale'))
        self.assertTrue(isOneAway('pale', 'bale'))
        self.assertFalse(isOneAway('pale', 'bae'))
        # Larger fail case.
        self.assertFalse(isOneAway('pale', 'bbb'))

if __name__ == '__main__':
    unittest.main()
