# num is divisible by 7
def divisible(n):
    if n==0:
        return True
    while n>=7:
        n-=7
    return n==0

n=int(input())
print(divisible(n))