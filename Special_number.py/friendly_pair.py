def friendly_pair(num1,num2):
    sum1=0
    sum2=0
    for i in range(1,num1):
        if num1%i==0:
            sum1+=i
    for j in range(1,num2):
        if num2%j==0:
            sum2+=j
    ratio1=sum1/num1
    ratio2=sum2/num2
    if round(ratio1,3)==round(ratio2,3):
        print("friendly pair")
    else:
        print("No")
        
num1=int(input())
num2=int(input())
friendly_pair(num1,num2)