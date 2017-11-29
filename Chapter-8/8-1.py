import unittest

# Triple Step
# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

# Strong induction assumption: assume you know how many ways for 0, ..., n-1 stairs,
# then triple_step(n) = triple_step(n-1) + triple_step(n-2) + triple_step(n-3)
# because at the first step, you have 3 options, and then you apply induction
# hypothesis.

# Establish memory for base cases.
mem = [0, 1, 2, 4]
def triple_step(n):
    if n < len(mem):
        return mem[n]
    else:
        curr = triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)
        mem.append(curr)
        return curr

# I noticed that we only care about the previous three computations.
# This is an implementation of triple step that is bottom-up.
def bottom_up_ts(n):
    if n == 0 or n == 1 or n == 2:
        return n
    elif n == 3:
        return 4
    else:
        a = 1
        b = 2
        c = 4
        count = 0
        while (count < n - 1):
            c_temp = c
            b_temp = b
            c = a + b + c
            b = c_temp
            a = b_temp
            count += 1
        return a

# Test cases for triple step.
class MyTests(unittest.TestCase):
    def test(self):
        self.assertEqual(7, triple_step(4))
        self.assertEqual(13, triple_step(5))

        self.assertEqual(7, bottom_up_ts(4))
        self.assertEqual(13, bottom_up_ts(5))

if __name__ == '__main__':
    unittest.main()
