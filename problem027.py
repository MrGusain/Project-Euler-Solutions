'''
Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:
                                      n² + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39.
However, when n = 40, 40² + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula n² - 79 + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n² + an + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
'''

import time
def prime_gen(num=100):
    import math
    p = int(math.sqrt(num)) + 1
    primes = [x for x in range(1,num+1,2)]
    length = len(primes)

    for i in range(1,p):
        if primes[i] != -1:
            prime = primes[i]
            j = prime*i+i
            while j < length:
                primes[j] = -1
                j += prime

    mst = {x:False for x in primes if x!=-1}
    del mst[1]
    return  mst


def solution_27(l = 1000):
    max_primes = 0
    primes = prime_gen(l*l)

    for a in range(-l+1,l):
        val = abs(- 1 - a)
        val = val + 1 if val % 2 == 0 else val
        for b in range(val,l,2):
            if primes.get(b, True):
                continue
            n = 2
            while True:
                equation = (n**2) + (a*n) + b
                if primes.get(equation, True):
                    break
                n += 1

            if max_primes < n:
                max_primes = n - 1
                pairs = (a,b)

    print(f'{pairs}: {pairs[0] * pairs[1]}')
    return pairs[0] * pairs[1]

limit = 1000
solution_27(limit)
