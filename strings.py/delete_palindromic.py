s=input()
del_count=0
left,right=0,len(s)-1
while left<=right:
    if s[left]==s[right]:
        left+=1
        right-=1
    else:
        del_count+=2
        left+=1
        right-=1
print(del_count)
