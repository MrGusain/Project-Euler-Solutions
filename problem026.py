'''
Reciprocal cycles
Problem 26
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

#important note:
# set ul according to denomiator, as the denomiator incereases so does ul, to make sure your loop won't run forever
#i've tested the limit to 10,000 and guess what? .. it works fine, above 10,000 i've no idea if it'll work or not
#correct me if i'm wrong

ul = 1000
def solution_26(d):
    num, cycle, num_seen = 10, '0.', set()
    limit = 1

    while True:
        num_seen.add(num)
        div = num // d
        num = num % d

        if num == 0:
            cycle += f'{div}'
            break

        cycle += f'{div}'

        if limit > ul:
            print(d,'fix your program or incerease the ul to some high number')
            break

        limit += 1
        num = num*10

        if num in num_seen:
            break

    return cycle


cycle, max_len = '1', 1
num = 1

# max_l as asked in question
max_l = 1000

for x in range(2,max_l):
    res = solution_26(x)
    new_len = len(res)

    if new_len > max_len:
        max_len = new_len
        cycle = res
        num = x

print(f'number: {num}, answer: {cycle}')



#you can verify above result with wolframalpha's solution as given below


def check_solution(num):
    app_id = '12A34C-D56EFGHIJ7' #setup an account on wolframalpha and get yourself one a new id
    import wolframalpha,re

    client = wolframalpha.Client(app_id)
    res = client.query(f'1/{num}')

    ans, sol = None, solution_26(num)
    data = []

    for pod in res.pods:
        flag = False
        for sub in pod.subpods:
            text = str(sub.plaintext)
            if text.startswith('0.'):
                ans = text
            data = re.findall(r'(0\.\d+)\^_',text)
            if data:
                ans = data[0]
                flag = True
                break
        if flag:
            break

    if not ans:
        # sometimes wolframalpha happens to not send all the digits as the length of recurring pattern increases
        print('modify the regex pattern!')

    return True if sol == ans else False



# print(check_solution(50))
