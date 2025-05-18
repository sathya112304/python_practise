# Check whether perfect number or not
def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if num==sum:
        print("Its a perfet number")
    else:
        print("Not a perfect number")
n=int(input())
perfect(n)

# All perfect numbers in a range

def perfect(num):
    arr=[]
    for j in range(2,num):
        sum=0
        for i in range(1,j):
            if j%i==0:
                sum+=i
        if j==sum:
            arr.append(j)
    return arr
num=int(input())
print(perfect(num))

# To print kth perfect number in a range
def perfect(num,k):
    arr=[]
    for j in range(2,num):
        sum=0
        for i in range(1,j):
            if j%i==0:
                sum+=i
        if j==sum:
            arr.append(j)
    if k<=len(arr):    
        return arr[k]
    else:
        return "out of index"
num=int(input())
k=int(input())
print(perfect(num,k))

# Kth perfect number
def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum==n
def kth_perfect(k):
    count=0
    n=2
    while True:
        if perfect(n):
            count+=1
            if count==k:
                return n
        n+=1
        
k=int(input())
print(kth_perfect(k))
    
