'''
Champernowne's constant
Problem 40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digits of the fractional part is 1.

If dn represents the nth digits of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000.
'''
from functools import reduce
n = 6
limit = 10 ** n

def solution_40():
    digits, length = '0', 1
    for num in range(1, limit):
        string = str(num)
        l = len(string)

        digits += string
        length += l
        if length > limit:
            break

    mult = reduce(lambda x, y: int(x) * int(y), map(lambda x: digits[10 ** x], range(n + 1)))
    print(mult)

solution_40()
# answer: 210
