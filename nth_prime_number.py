def is_prime(num):
    if num<=1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
def no_primes(n):
    count=0
    num=2
    while count<n:
        if is_prime(num):
            count+=1
            if count==n:
                return num
        num+=1
    
n=int(input())
print(no_primes(n))