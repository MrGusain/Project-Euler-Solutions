'''
Names scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to 
obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''



from urllib.request import urlopen

with urlopen("https://projecteuler.net/project/resources/p022_names.txt") as response:
    source = response.read()


names = sorted(source.decode("utf-8").split(","))



def loop():
    total = 0
    for position,name in enumerate(names):
        val = 0
        name = name.strip('"')
        for character in name:
            val += ord(character) - ord('A') + 1

        score = (position + 1) * val

        total += score
    print(total)



# one liner
def countSum():
    total = sum(((position + 1) * sum(ord(character) - ord('A') + 1 for character in name.strip('"'))) for position,name in enumerate(names))
    print(total)



