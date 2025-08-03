s1=input()
s2=input()
n=len(s1)
is_isomorphic=True
for i in range(n):
    c1=s1[i]
    c2=s2[i]
    for j in range(n):
        if s1[i]==c1 and s2[j]!=c2 or s2[j]==c1 and s1[j]!=c1:
            is_isomorphic=False
if is_isomorphic:
    print("True")
else:
    print("False")