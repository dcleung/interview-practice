import unittest

# Method to replace all white spaces in an input string with '%20'.
# We are given the input and its length.
def replaceWhiteSpaces(input, length):
    # Remove leading and trailing white space.
    input = input.strip()
    # Make character list from input string.
    inList = list(input)
    # Define the return list and a count pointer.
    ret = list()
    # Iterate through the character list.
    for i in range(0, len(inList)):
        # If character is space, we extend the return list with %20.
        if inList[i] == ' ':
            ret.extend(['%', '2', '0'])
        # Otherwise, we append the current character to the return list.
        else:
            ret.append(inList[i])
    # Convert to string.
    ret = ''.join(ret)
    return ret

# Testing suite for replaceWhiteSpaces.
class MyTests(unittest.TestCase):
    def test(self):
        # Sample test case.
        self.assertEquals('Mr%20John%20Smith', replaceWhiteSpaces('Mr John Smith ', 13))
        # Test just spaces.
        self.assertEquals('', replaceWhiteSpaces('  ', 3))
        # Test one character.
        self.assertEquals('a', replaceWhiteSpaces(' a ', 3))
        # Test multiple spaces between letters.
        self.assertEquals('a%20%20b', replaceWhiteSpaces(' a  b ', 3))
    
if __name__ == '__main__':
    unittest.main()
