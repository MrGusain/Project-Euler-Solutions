'''
1000-digit Fibonacci number 
Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

'''
Saying that a number contains 1000 digits is the same as
saying that it's greater than 10**999.

The nth Fibonacci number is [phi**n / sqrt(5)], where the
brackets denote "nearest integer".

So we need phi**n/sqrt(5) > 10**999

n * log(phi) - log(5)/2 > 999 * log(10)

n * log(phi) > 999 * log(10) + log(5)/2
n > (999 * log(10) + log(5) / 2) / log(phi)
'''

def solution_25():
    phi = (1+math.sqrt(5))/2
    lhs = ((999 * math.log(10)) + (math.log(5)/2))/(math.log(phi))
    return round(lhs)


ans = solution_25()
print(ans)



