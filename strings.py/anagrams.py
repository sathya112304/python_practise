lst=list(map(str,input().split()))
s=input()
arr=[]
for word in lst:
    if all(ch in s for ch in word) and len(word)==len(s):
        arr.append(word)
        
print(arr)     