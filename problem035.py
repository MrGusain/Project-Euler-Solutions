'''
Circular primes 
Problem 35

The number, 197, is called a circular prime because all rotations of the digits: 
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import math
def prime_gen(num):
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

    mst = [x for x in primes if x!=-1]
    mst = [2] + mst[1:]

    return mst


limit = 1000000
primes = set(prime_gen(limit))


def all_cycles(no):
    number = str(no)
    n = len(number)
    possibles = set()
    for i in range(n):
        new_num = int(number[i:]+number[:i])
        if new_num % 2 == 0:
            return {1}
            
        possibles.add(new_num)

    return possibles

val = 1+sum(1 for prime in primes if not all_cycles(prime) - primes)
print(val)