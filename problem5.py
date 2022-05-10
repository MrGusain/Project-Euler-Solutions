'''
Smallest multiple 
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def evenly_divisible(tar):
    factors = [2]
    product = 2
    for x in range(3,tar):
        num = x
        for y in factors:
            if num%y == 0:
                num = (num//y)
        if num ==1:
            continue
        factors.append(num)
        product *= num

    return product
