'''
Multiples of 3 or 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def multiple_sum(limit):
    a,b = 3,5
    num_a,num_b,num_ab = (limit-1)//a,(limit-1)//b,(limit-1)//(a*b)
    sum_a,sum_b,sum_ab = (num_a*(num_a+1))//2,(num_b*(num_b+1))//2,(num_ab*(num_ab+1))//2
    return (a*sum_a) + (b*sum_b) - (a*b*sum_ab)


print(multiple_sum(1000))
