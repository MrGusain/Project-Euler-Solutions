'''
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

'''




'''
This one also by hand (self explanatory):

one             3
two             3
three           5
four            4
five            4
six             3
seven           5
eight           5
nine            4=36
ten             3+36=39
eleven          6
twelve          6   
thirteen        8
fourteen        8
fifteen         7
sixteen         7
seventeen       9
eighteen        8
nineteen        8=67
19              (67+39)

twenty          6+67+39=112
thirty          6+6*9+36+112=208
forty           5+6*9+36+208=303
fifty           5+5*9+36+303=389
sixty           5+5*9+36+389=475
seventy         7+5*9+36+475=563
eighty          6+7*9+36+563=668
ninety          6+6*9+36+668=764
99              6*9+36+764=854
onehundred      10+6*9+36+764=864

onehundredand   (=13)
199             (13*99+854+864)

twohundred      10+13*99+854+864=3015
twohundredand   (=13)
299             (13*99+854+3015)

threehundred    12+13*99+854+3015=5168
threehundredand (=15)
399             (15*99+854+5168)

fourhundred     11+15*99+854+5168=7518
fourhundredand  (=14)
499             (14*99+854+7518)

fivehundred     11+14*99+854+7518=9769
fivehundredand  (=14)
599             (14*99+854+9769)

sixhundred      10+14*99+854+9769=12019
sixhundredand   (=13)
699             (13*99+854+12019)

sevenhundred    12+13*99+854+12019=14172
sevenhundredand (=15)
799             (15*99+854+14172)

eighthundred    12+15*99+854+14172=16523
eighthundredand (=15)
899             (15*99+854+16523)

ninehundred     11+15*99+854+16523=18873
ninehundredand  (=14)
999             (14*99+854+18873)

onethousand     11+14*99+854+18873=21124

'''



#python has a module that deals with this sort of conversion
from num2words import num2words
def letters_count(limit):
    count = sum(len(''.join(''.join(num2words(number).split()).split('-'))) for number in range(1,limit+1))
    return count


print(letters_count(1000))