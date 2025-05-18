# check whether number is armstrong or not
def armstrong(num):
    temp=num
    sum=0
    power=len(str(num))
    while temp>0:
        digit=temp%10
        sum+=digit**power
        temp=temp//10
    if sum==num:
        print("it is armstrong")
    else:
        print("not a armstrong")

num=int(input())
armstrong(num)

# to generate all armstrong numbers upto n
n=int(input())
arr=[]
for i in range(0,n+1):
    temp=i
    sum=0
    power=len(str(i))
    while temp>0:
        digit=temp%10
        sum+=digit**power
        temp=temp//10
    if sum==i:
        arr.append(i)
    else:
        continue
print(arr)