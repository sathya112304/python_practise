def automorphic(num):
    square=num*num
    while num>0:
        if square%10!=num%10:
            return False
        square//=10
        num//=10
    return True
    
num=int(input())
if automorphic(num):
    print('Yes')
else:
    print('No')