#equal point in a string of brackets
def brackets(s):
    for i in range(len(s)):
        count1,count2=0,0
        for j in range(i):
            if s[j]=='(':
                count1+=1
        for j in range(i,len(s)):
            if s[j]==')':
                count2+=1
        if count1==count2:
            return i
    return -1
s=input()
print(brackets(s))

