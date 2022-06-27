'''
Self powers
Problem 48

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

def lastNdigits(n = 10):
  num = str(sum(x ** x for x in range(1000 + 1)))[-n:]
  print(num)

lastNdigits()
#answer: 9110846701
