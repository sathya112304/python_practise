# To check spy number or not 
def spy_numbers(n):
    sum=0
    prod=1
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit
        prod*=digit
        temp=temp//10
    if sum==prod:
        print("its a spy number")
    else:
        print("not a spy number")
n=int(input())
spy_numbers(n)