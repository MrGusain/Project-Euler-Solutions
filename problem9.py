'''
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def triplets(n):
    for a in range(3,n//3+1):
        b = (n**2 - 2*a*n)//(2*n - 2*a)
        c = n - b - a
        if a**2 + b**2 == c**2:
            return (a*b*c)

