'''
Lattice paths
Problem 15

Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''


from functools import reduce
n = 20      #grid size
#calculating the factorial using 
'''
²ⁿCₙ =  2n×(2n−1)×...×(n+2)×(n+1) / n×(n−1)×...×2×1 
²ⁿCₙ = ⁿ∏ᵢ₌₀ (n+i)/i  
'''
product = round(reduce(lambda x,y : x*y, map(lambda x : (n+x)/x,range(1,n+1))))
print(product)