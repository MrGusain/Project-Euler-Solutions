'''
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def product_palin(digit):
    upper,lower = (10**digit)-1,10**(digit-1)
    a,palin = upper,0
    max_11 = 11*int(upper/11)
    while a >= lower:
        if a%11 == 0:
            b,b_diff = upper,1
        else:
            b,b_diff = max_11,11
        while a>=b:
            if a*b < palin:
                break
            product = str(a*b)
            if len(product)!= digit*2:
                break
            if product == product[::-1]:
                palin = a*b
            b -= b_diff
        a -= 1
    return palin
