#palindrome string
def palindrome(s):
    left,right=0,len(s)-1
    while left<=right:
        if s[left]!=s[right]:
            return 0
        left+=1
        right-=1
    return 1

s=input()
print(palindrome(s))

#optimization of pointers
def palindrome(s):
    n=len(s)
    for i in range(n//2):
        if s[i]!=s[n-i-1]:
            return 0        
    return 1

s=input()
print(palindrome(s))