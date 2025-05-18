def prime(n):
    if n<=1:
        return False
    else:
        is_prime=True
        for i in range(2,n):
        #for i in range(2,int(n**0.5)+1)
            if n%i==0:
                is_prime=False
                break
        return (is_prime)
n=int(input())
print(prime(n))