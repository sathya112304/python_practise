from collections import Counter
def hexdec(num):
    return (hex(num)[2:])
def encrypt(s):
    string=""
    s=Counter(s)
    for key,values in s.items():
        hexa=hexdec(values)
        string+=key+hexa
    return string[::-1]
s=input()
print(encrypt(s))


