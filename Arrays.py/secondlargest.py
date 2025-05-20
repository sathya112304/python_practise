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