#Maximum product of a triplet 
arr=list(map(int,input().split()))
b=sorted(arr,reverse=True)
print(max(b[0]*b[1]*b[2],b[-1]*b[-2]*b[0]))

