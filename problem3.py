'''
Largest prime factor 
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def all_prime_factors(num):
    factors,start = [1],2
    limit = int(math.sqrt(num))+3

    while start <= limit:
        if num%start == 0:
            factors.append(start)
            num //= start
        else:
            start += 2 if start != 2 else 1
    return factors
