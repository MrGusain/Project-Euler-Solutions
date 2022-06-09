'''
Digit fifth powers
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

n = 5
def solution_30(n):
    max_limit = 9*(9 ** 9)
    powers = {x:x**n for x in range(10)}
    lst = [(x*(9**n),x) for x in range(1,10)]
    limit = list(filter(lambda x: (lambda x:len(str(x)))(x[0])>=x[1], lst))[-1][0]
    max_limit = min(limit,max_limit)
    pairs = sum(number for number in range(1,max_limit) if number == sum(map(lambda x:powers[x], map(int,str(number)))))
    print(pairs-1)

solution_30(n)



#one-liner
powers = {x:x**n for x in range(10)}
pairs = sum(number for number in range(1,list(filter(lambda x: (lambda x:len(str(x)))(x[0])>=x[1], [(x*(9**n),x) for x in range(1,10)]))[-1][0]) if number == sum(map(lambda x:powers[x], map(int,str(number)))))-1
print(pairs)
