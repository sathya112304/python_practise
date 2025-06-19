#Strings Are Rotations of Each Other
def rotated(s1,s2):
    s1=s1+s2
    for i in s2:
        if i in s1:
            return True
    return False

s1=input()
s2=input()
print(rotated(s1,s2))

def rotated(s1,s2):
    for i in range(len(s1)):
        if s1==s2:
            return True
        s1=s1[-1]+s1[::-1]
    return False

s1=input()
s2=input()
print(rotated(s1,s2))