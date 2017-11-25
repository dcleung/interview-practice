import unittest

# Return true if input is of unique letters, false otherwise.
# Extra memory is permitted.
def isUnique(input):
	dict = {}
	for c in input:
		if dict.has_key(c):
			return False
		else:
			dict[c] = 1
	return True

# Return true if input is of unique letters, false otherwise.
# No extra memory allowed.
def isUnique2(input):
	for c in range (0, len(input)):
		for d in range (c + 1, len(input)):
			if c == d:
				return False
	return True


# Testing suite for isUnique and isUnique2.
class MyTests(unittest.TestCase):
	def test(self):
		# String 'abc' is unique.
		self.assertTrue(isUnique('abc'))
		self.assertTrue(isUnique2('abc'))
		# String 'cbc' is not unique.
		self.assertFalse(isUnique('cbc'))
		self.assertTrue(isUnique2('cbc'))
		# Empty string is unique.
		self.assertTrue(isUnique(''))
		self.assertTrue(isUnique2(''))


if __name__ == '__main__':
	unittest.main()
