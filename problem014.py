'''
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

#....................................................................................
# iterative solution
Chain = {1:1}
def gen_chain(num):
    lst = [num]
    count = 1
    while num !=1:
        if num%2 == 0:
            num = num//2
        else:
            num = 3*num + 1
        lst.append(num)
        if num in Chain:
            val = Chain[num]
            for i in range(len(lst)-1,-1,-1):
                Chain[lst[i]] = val
                val += 1
            return count + Chain[num] 
        count += 1
    return count

max_len,number = 1,1
limit = 1000000
for x in range(500000,limit):
    chain_len = gen_chain(x)
    if chain_len > max_len:
        max_len,number = chain_len,x
    
print(max_len,number)



#....................................................................................
# recursive solution


chains = {0:1,1:1}
def count_chain(num):
    if num in chains:
        return chains[num]
    if num%2 == 0:
        chains[num] = 1 + count_chain(num//2)
    else:
        chains[num] = 2 + count_chain((3 * num + 1) // 2)
    return chains[num]


def long_chain(limit = 10**6):
    longest_chain,answer = 0,-1
    for no in range(500000,limit):
        chain_len = count_chain(no)
        if chain_len > longest_chain:
            longest_chain,answer = chain_len,no
    return answer,longest_chain


print(long_chain())
