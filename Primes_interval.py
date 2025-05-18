def prime_numbers(n1,n2):
    arr=[]
    for i in range(n1,n2+1):
        if i<=1:
            return False
        else:
            is_prime=True
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    is_prime=False
                    break
            if is_prime:
                arr.append(i)
    '''return arr'''
    for k in arr:
        print(k,end=" ")
    
n1=10
n2=50
prime_numbers(n1,n2)


