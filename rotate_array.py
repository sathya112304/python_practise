# Brute force approach small arrays
def left_rotated(d,arr):
    low,high=0,len(arr)-1
    for i in range(low,high):
        if d>i:
            temp=arr[0]
            arr.pop(0)
            arr.append(temp)
        else:
            break
    return arr
d=int(input())
arr=list(map(int,input().split()))
print(left_rotated(d,arr))

#Optimized approach

def left_rotated(d,arr):
    d=d%len(arr)
    return arr[d:]+arr[:d]
    
d=int(input())
arr=list(map(int,input().split()))
print(left_rotated(d,arr))

# Brute force approach for small arrays
def right_rotated(arr,d):
    low,high=0,len(arr)-1
    for i in range(low,high):
        if d>i:
            temp=arr[-1]
            arr.pop()
            arr.insert(0,temp)
        else:
            break
    return arr
arr=list(map(int,input().split()))
d=int(input())
print(right_rotated(arr,d))

# Optimized approach
def right_rotated(d,arr):
    d=d%len(arr)
    return arr[-d:]+arr[:-d]
    
d=int(input())
arr=list(map(int,input().split()))
print(right_rotated(d,arr))
