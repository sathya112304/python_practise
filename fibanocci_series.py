# Fibanocci series
def fib(n):
    arr=[]
    a,b=0,1
    while a<=n:
        arr.append(a)
        a,b=b,a+b
    return arr
n=int(input())
print(fib(n))

#Non-Fibanocci series
def fib(n):
    arr=[]
    a,b=0,1
    while a<=n:
        arr.append(a)
        a,b=b,a+b
    for i in range(0,n+1):
        if i not in arr:
            print(i,end=" ")
n=int(input())
fib(n)

#nth fibanocci number
def fib(n):
    count=0
    a,b=0,1
    while count<n:
        a,b=b,a+b
        count+=1
    return a
n=int(input())
print(fib(n))