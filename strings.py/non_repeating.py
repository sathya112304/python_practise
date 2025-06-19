#First non repeating chanracter in a string
from collections import Counter
def non_repeating(s):
    a=Counter(s)
    for key,values in a.items():
        if values==1:
            return key
    return "$"
    
str=input()
print(non_repeating(str))