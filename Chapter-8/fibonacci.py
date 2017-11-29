import time

# Recursive implementation of fibonacci.
# Runs in O(2^n) time.
# O(1) space (unless considering the stack space used).
def recurse_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recurse_fibonacci(n-1) + recurse_fibonacci(n-2)

t0 = time.time()
print(recurse_fibonacci(5))
t1 = time.time()
print "Recursive fibonacci took {} seconds to run.".format(t1-t0)

# Dynamic programming implementation () of fibonacci.
# Runs in O(n) time, but uses O(n) space to store the table.
mem = [0, 1]
def dp_fibonacci(n):
    if n < len(mem):
        return mem[n]
    else:
        curr = dp_fibonacci(n-1) + dp_fibonacci(n-2)
        mem.append(curr)
        return curr

t0 = time.time()
print(dp_fibonacci(40))
t1 = time.time()
print "Dynamic programming fibonacci took {} seconds to run.".format(t1-t0)

# Dynamic programming implementation with constant space.
# Runs in O(n) time and uses O(1) space.
def const_fib(n):
    if n == 0 or n == 1:
        return n
    prev = 0
    curr = 1
    count = 0
    while(count < n - 1):
        temp = prev
        prev = curr
        curr = temp + curr
        count += 1
    return curr

t0 = time.time()
print(const_fib(40))
t1 = time.time()
print "Dynamic programming const space fibonacci took {} seconds to run.".format(t1-t0)

'''
Notes: there is a significance difference in the run-times of the recursive fibonacci
versus the dynamic programming implementatinos.  I also noticed that in practice,
the DP implementation with constant space ran faster than the one with the table,
probably because of the time used to access/write to table.
'''
