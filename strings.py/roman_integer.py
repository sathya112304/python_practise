# roman to integer conversion
def roman_decimal(s):
    roman={
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
    res=0
    i=0
    while i<len(s):
        if i+1 <len(s) and roman[s[i]]<roman[s[i+1]]:
            res+=roman[s[i+1]]-roman[s[i]]
            i+=1
        else:
            res+=roman[s[i]]
        i+=1
    return res

s=input()
print(roman_decimal(s))

#integer to roman conversion


