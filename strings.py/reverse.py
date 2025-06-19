#reverse the string
def reverse(s):
    reversed=s[::-1]
    return reversed
s=input()
print(reverse(s))

#backward approach
def reverse(s):
    reversed=[]
    for i in range(len(s)-1,1,-1):
        reversed.append(s[i])
    return ''.join(reversed)

s=input()
print(reverse(s))

#Two pointers
def reverse(s):
    left,right=0,len(s)-1
    s=list(s)
    while left<=right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1

    return ''.join(s)

s=input()
print(reverse(s))