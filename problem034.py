'''
Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

factorial = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}
def mapped_fact(num):
    return sum(factorial[int(x)] for x in str(num))


big_limits = [(10,44), (10**2,655), (10**3,7666), (10**4,88777), (10**5,851760), (10**6,2540160)]
limits = [(10,44), (10**2,655), (10**3,7666), (10**4,88777)]
# improved_limits = [(x,mapped_fact(y)) for x,y in limits]

def solution_34():
    tot = 0
    for limit in limits:
        a, b = limit
        for num in range(a+1, b+1):
            if num == mapped_fact(num):
                print(num)
                tot += num
    print(tot)
    return tot

ans = solution_34()
# one-liner
tot = sum(num for limit in limits for num in range(limit[0]+1, limit[1]+1) if num == mapped_fact(num))
print(tot)
# answer: 40730
