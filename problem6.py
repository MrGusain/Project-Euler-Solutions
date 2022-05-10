'''
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
1² + 2² + 3² + ....... + 10² = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + 3 + ........ + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def diff_pattern(limit):
    diff = limit*(limit**2-1)*(3*limit+2)
    return diff//12
