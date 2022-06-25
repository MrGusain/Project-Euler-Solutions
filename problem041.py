'''
Pandigital prime
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

from math import sqrt
from itertools import permutations

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    for x in range(3, int(sqrt(num)) + 1, 2):
        if num % x == 0:
            return False
    return True


def pandigital_7():
    pandigital_4 = [1243, 1423, 2143, 2413, 4123, 4213, 2341, 2431, 3241, 3421, 4231, 4321]
    # max_pandigital = max(filter(is_prime, pandigital_4))
    max_pandigital = 4231

    nums = ['2','4','5','6']
    last_digits = {'1','3','7'}

    for x in last_digits:
        for each_p in sorted(permutations(list(last_digits - set(x)) + nums), reverse = True):
            number = int(''.join(each_p) + x)
            if is_prime(number):
                max_pandigital = max(number, max_pandigital)
                break

    print(max_pandigital)

pandigital_7()
# answer: 7652413
