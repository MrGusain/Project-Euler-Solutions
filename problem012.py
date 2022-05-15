'''
Highly divisible triangular number
Problem 12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
import math

def is_prime(num):
    if num == 3 or num == 5:
        return True
    for x in range(3,int(math.sqrt(num)+1)):
        if num%x == 0:
            return False
    return True


def nth_Prime(tar=10001):
    count = 1
    num,primes = 3,[2]
    while count != tar:
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 2
    return num-2,primes



n = 3
dn = 2
cnt = 0

no,primearray = nth_Prime(1000)

while cnt <= 500:
    n = n + 1
    n1 = n
    if n1%2 == 0:
        n1 = n1//2
    dn1 = 1

    for prime in primearray:

        if prime*prime > n1:
            dn1 = 2*dn1
            break

        exp = 1
        while n1 % prime == 0:
            exp += 1
            n1 = n1/prime

        if exp > 1:
            dn1 = dn1*exp

        if n1 == 1:
            break

    cnt = dn*dn1
    dn = dn1


print(n*(n-1)//2)