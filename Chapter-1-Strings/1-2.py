import unittest

# Return if two strings are permuations.
def isPermutation(str1, str2):
	dict = {}
	# If lengths are not the same, cannot be permutations.
	if len(str1) != len(str2):
		return False
	# Iterate through str1 and add to the dictionary.
	for c in str1:
		if dict.has_key(c):
			value = dict.get(c)
			dict[c] = value + 1
		else: dict[c] = 1
	# Iterate through str2 and make sure the counts work out.
	for d in str2:
		if dict.has_key(d):
			value = dict.get(d) - 1
			if value == 0:
				del dict[d]
			else:
				dict[d] = value
		else:
			return False
	return True

# Testing suite for isUnique and isUnique2.
class MyTests(unittest.TestCase):
	def test(self):
		# Strings 'abc' and 'bac' are permutations.	
		self.assertTrue(isPermutation('abc', 'bac'))
		# Strings 'abb' and 'abc' are not permutations.
		self.assertFalse(isPermutation('abb', 'abc'))
		# Strings 'ab' and 'abb' are not permutations.
		self.assertFalse(isPermutation('ab', 'abb'))
		# Empty strings are permutations.
		self.assertTrue(isPermutation('', ''))
		# Same character strings are permutations.
		self.assertTrue(isPermutation('a', 'a'))
	
if __name__ == '__main__':
	unittest.main()