'''
Summation of primes 
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

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
    return sum(x for x in primes if x!=-1)+1
  
  
