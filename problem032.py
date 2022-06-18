'''
Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

from itertools import permutations

def possible_pairs(num):
    numbers = {'1','2','3','4','5','6','7','8','9'} - set(map(lambda x: str(x), str(num)))
    return [int(''.join(num))  for num in permutations(numbers,5 - len(str(num)))]

def is_genuine(a):
    num = str(a)
    if '0' in num:
        return False
    return True if len(num) == len(set(num)) else False

def is_pandigital(a,b):
    string = str(a) + str(b) + str(a*b)
    if len(string) != len(set(string)):
        return False
    return True if set(string) == {'1', '2', '3', '4', '5', '6', '7', '8', '9'} else False


def solution_32():
    pandigitals = set()
    start = 1
    while start < 9877:
        if is_genuine(start):
            pairs = possible_pairs(start)
            for pair in pairs:
                if is_pandigital(start,pair):
                    print(start,pair,start*pair)
                    pandigitals.add(start * pair)
        start += 1

    print(sum(pandigitals))


solution_32()
# answer: 45228
