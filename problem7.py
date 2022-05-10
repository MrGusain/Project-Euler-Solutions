'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''



def is_prime(num):
    if num == 3 or num == 5:
        return True
    for x in range(3,int(math.sqrt(num)+1)):
        if num%x == 0:
            return False
    return True


def _10001st_prime():
    start = time.time()
    count = 1
    num = 3
    while count != tar:
        if is_prime(num):
            count += 1
        num += 2
    return num-2

  
  
print(_1001st_prime())

