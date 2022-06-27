'''
Self powers
Problem 48

The series, 1¹ + 2² + 3³ + ... + 10¹⁰ = 10405071317.

Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 1000¹⁰⁰⁰.
'''

def lastNdigits(n = 10):
  num = str(sum(x ** x for x in range(1000 + 1)))[-n:]
  print(num)

lastNdigits()
#answer: 9110846701
