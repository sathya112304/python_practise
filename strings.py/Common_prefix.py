#longest common prefix
def longestCommonPrefix(arr):
    arr.sort()
    first=arr[0]
    last=arr[-1]
    min_length=min(len(first),len(last))
    i=0
    while i<min_length and first[i]==last[i]:
        i+=1
    return first[:i]

arr=list(map(str,input().split()))
print(longestCommonPrefix(arr))


