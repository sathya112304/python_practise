def second_largest(arr):
    largest=0
    second_largest=0
    for i in range(0,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    for j in range(0,len(arr)-1):
        if arr[j]>second_largest and arr[j]!=largest:
            second_largest=arr[j]
    return second_largest

arr=list(map(int,input().split()))
print(second_largest(arr))

#Optimal
def second_largest(arr):
    first=second=float('-inf')
    for i in range(len(arr)):
        if arr[i]>first:
            second=first
            first=arr[i]
        elif arr[i]<first and arr[i]>second:
            second=arr[i]
    return second

arr=list(map(int,input().split()))
print(second_largest(arr))