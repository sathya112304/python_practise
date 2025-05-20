# Using maxheap

import heapq
def kth_smallest(arr,k):
    q=[]
    for i in arr:
        heapq.heappush(q,-i)
        if len(q)>k:
            heapq.heappop(q)
    return -q[0]
    
arr=arr=list(map(int,input().split()))
k=int(input())
print(kth_smallest(arr,k))

#Bubble sort
def kth_smallest(arr,k):
    arr=list(set(arr))
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            else:
                continue
    return arr[k-1]

arr=arr=list(map(int,input().split()))
k=int(input())
print(kth_smallest(arr,k))