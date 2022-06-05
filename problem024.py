'''
Lexicographic permutations 
Problem 24

A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

                                012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import math
from functools import reduce

def factorial(n):
    return reduce(lambda x,y : x*y,range(1,n+1))


def group_size(n):
    return factorial(n)//n


n = 10
limit = 10**6 

def solution(n,limit):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    limit = limit - 1
    res = []
    while n >= 1:
        gsize = group_size(n)
        start = ((limit//gsize)*gsize)
        res.append(numbers[limit//gsize])
        numbers.remove(numbers[limit//gsize])
        limit = limit - start
        n -= 1

    ans = int(''.join(map(str,res)))
    return ans

print(solution(n,limit))



