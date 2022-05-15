'''
Factorial digit sum
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


# def factorial_digit_sum(num):
#     factorial = sum(int(x) for x in str(reduce(lambda x,y : x * y ,range(1,num+1))))
#     print(factorial)


# factorial_digit_sum(100)


def amicable_numbers(num):
    a = 1 + sum(nu for nu in range(2,num//2+2) if num%nu == 0)
    # print(a,1 + sum(nu for nu in range(2,a//2+2) if a%nu == 0))
    if a == num:
        return False
    return True if (1 + sum(nu for nu in range(2,a//2+2) if a%nu == 0)) == num else False


# print(amicable_numbers(220))

total = sum(x for x in range(10000) if amicable_numbers(x))
print(total)

