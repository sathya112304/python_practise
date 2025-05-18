#To check plaindrome or not
def palindrome(num):
    num1=str(num)
    if num1==num1[::-1]:
        print("Given is palindrome")
    else:
        print("Not a palindrome")
num=int(input())
palindrome(num)

#To check palindrome without string
def palindrome(n):
    temp=n
    reverse=0
    while n>0:
        digit=n%10
        reverse=reverse*10+digit
        n=n//10
    if temp==reverse:
        return "Its a palindrome"
    else:
        return "not a palindrome"
n=int(input())
print(palindrome(n))

#To print all palindromes
def palindrome(n):
    for i in range(0,n+1):
        str_i=str(i)
        if str_i==str_i[::-1]:
            print(i,end=" ")
        else:
            pass
n=int(input())
palindrome(n)

# To print all palindromes without string
def palindrome(n):
    arr=[]
    for i in range(0,n+1):
        temp=i
        reverse=0
        while i>0:
            digit=i%10
            reverse=reverse*10+digit
            i=i//10
        if temp==reverse:
            arr.append(temp)
        else:
            continue
    return arr
n=int(input())
print(palindrome(n))