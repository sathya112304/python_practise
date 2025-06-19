# min distance between words
def min_dis(arr,word1,word2):
    d1=d2=-1
    ans=float('inf')
    for i in range(len(arr)):
        if arr[i]==word1:
            d1=i
        if arr[i]==word2:
            d2=i
        if d1!=-1 and d2!=-1:
            ans=min(ans,abs(d1-d2))
    return ans

arr=list(map(str,input().split()))
word1=input()
word2=input()
print(min_dis(arr,word1,word2))