'''
Amicable numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from collections import Counter
from functools import reduce
import math


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


def sumOfPrimesFactors(numb):
    factors = Counter(allPrimeFactors(numb))
    num = reduce(lambda x,y:x*y,map(lambda x:(x[0]**(x[1]+1))-1,factors.items()))
    den = reduce(lambda x,y:x*y,map(lambda x:x-1,factors.keys()))

    return num//den - numb


amicable_numbers = {}
limit = 10000

for num in range(200,limit):
    pair = sumOfPrimesFactors(num)
    if pair > num:
        if sumOfPrimesFactors(pair) == num:
            k,v = min(num,pair),max(num,pair)
            amicable_numbers[k] = v


ans = 0
for x,y in amicable_numbers.items():
    ans +=  (x+y)

print(sum(k+v for k,v in amicable_numbers.items()))
