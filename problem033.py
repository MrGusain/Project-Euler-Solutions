'''
Digit cancelling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

def solution_33(num_digits = 2):
    start, end = 10 **(num_digits - 1), 10 **(num_digits)
    from functools import reduce
    nums, dens = [], []
    for num in range(start, end):
        for den in range(num + 1, end):
            setA, setB = set(str(num)), set(str(den))
            common = setA.intersection(setB) - {'0'}
            if common:
                cNum, cDen = setA - common - {'0'}, setB - common - {'0'}
                if cNum and cDen:
                    n, d = list(map(int, cNum))[0], list(map(int, cDen))[0]
                    if num/den == n/d:
                        nums.append(n)
                        dens.append(d)

    nums = reduce(lambda x, y: x * y, nums)
    dens = reduce(lambda x, y: x * y, dens)
    print(f'solution: {nums}/{dens} -> 1/{dens/nums}')


solution_33()
# answer: 100
