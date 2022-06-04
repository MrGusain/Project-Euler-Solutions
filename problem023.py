'''
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import math
from collections import Counter
from functools import reduce


def allPrimeFactors(n):
    factors = []
    if n % 2 == 0:
        lastFactor = 2
        n = n // 2
        factors.append(2)
        while n % 2 == 0:
            n = n // 2
            factors.append(2)
    else:
        lastFactor = 1

    factor = 3
    maxFactor = int(math.sqrt(n)) + 1
    while n>1 and factor <= maxFactor:
        if n % factor == 0:
            factors.append(factor)
            n = n // factor
            lastFactor = factor
            while n % factor == 0:
                factors.append(factor)
                n = n // factor
            maxFactor = int(math.sqrt(n)) + 1

        factor += 2


    if n != 1:
        factors.append(n) 

    return factors


def sumOfPrimesFactors(number):
    factors = Counter(allPrimeFactors(number))
    num = reduce(lambda x,y:x*y,map(lambda x:(x[0]**(x[1]+1))-1,factors.items()))
    den = reduce(lambda x,y:x*y,map(lambda x:x-1,factors.keys()))
    return num//den - number



limit = 28124
abundant = []
start = time.time()
for x in range(12,limit):
    sums = sumOfPrimesFactors(x)
    if sums > x:
        abundant.append(x)



l = len(abundant)
pairs = {}

for x in range(l): 
    if abundant[x] > limit//2:
        break
    for y in range(x,l):
        if abundant[x]+abundant[y] < limit:
            pairs[abundant[x]+abundant[y]] = True
        else:
            break


print(sum(x for x in range(limit) if not pairs.get(x,False)))














