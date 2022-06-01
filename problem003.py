'''
Largest prime factor 
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

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

n = 600851475143
factors = allPrimeFactors(n)
print(factors)
print(max(factors))


