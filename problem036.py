'''
Double-base palindromes
Problem 36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

limit = 10 ** 6

def solution_36():
    total = 0
    for num in range(1, limit, 2):
        string = str(num)
        if string == string[::-1]:
            binary = bin(num).split('b')[-1]
            if binary == binary[::-1]:
                total += num
    print(f'sum is {total}')


solution_36()
# answer: 872187
