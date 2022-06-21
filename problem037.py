'''
Truncatable primes
Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
import math

def prime_list(num):
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

    mst = set.union({2}, {x for x in primes if x!=-1})
    mst.remove(1)
    return mst

def strip(string):
    setA = set(int(string[x:]) for x in range(len(string)))
    setB = set(int(string[:x+1]) for x in range(len(string)))
    return set.union(setA, setB)

def solution_37(limit = 11):
    primesL = prime_list(10**6)
    count, start = 0,11
    tot = 0
    while count < limit:

        if start not in primesL:
            start += 2
            continue

        string = str(start)
        lists = ('1','4','6','8')
        if string.endswith(lists) or string.startswith(lists):
            start += 2
            continue

        f = False
        for i in ["0", "4", "6", "8"]:
            if i in string:
                f = True
                break
        if f:
            start += 2
            continue

        if "5" in string[1:] or "2" in string[1:]:
            start += 2
            continue

        primes = strip(string)
        flag = True
        for prime in primes:
            if prime not in primesL:
                flag = False
                break

        if flag:
            count += 1
            tot += start

        start += 2

    print('total sum:',tot)
    return tot

limit = 11
solution_37(limit)
#total sum: 748317
