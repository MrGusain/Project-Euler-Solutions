'''
Power digit sum
Problem 16

2¹⁵ = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2¹⁰⁰⁰?
'''



def power_digit_sum(base,power):
    result = str(base ** power)
    digit_sum = sum(int(x) for x in result)
    return digit_sum

print(power_digit_sum(2,1000))