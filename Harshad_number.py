# To check harshad (Niven) number or not
def harshad(num):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit
        temp=temp//10
    if num%sum==0:
        print("Its a harshad number")
    else:
        print("Not a harshad number")
num=int(input())
harshad(num)

# To generate harshad numbers upto n
num=int(input())
arr=[]
for i in range(1,num+1):
    sum=0
    temp=i
    while temp>0:
        digit=temp%10
        sum+=digit
        temp=temp//10
    if i%sum==0:
        arr.append(i)
    else:
        continue
print(arr)
