def pyramid(n):
    alpha=65
    for i in range(0,n):
        print(" "*(n-i),end=" ")
        for j in range(0,i+1):
            print(chr(alpha),end=" ")
            alpha+=1
        
        print()
n=int(input())
pyramid(n)

#
def pyramid(n):
    alpha=65
    for i in range(0,n):
        print(" "*(n-i),end=" ")
        for j in range(0,i+1):
            print(chr(alpha),end=" ")
            alpha+=1
        alpha=65
        print()
n=int(input())
pyramid(n)

# Pyramid of singlealphabet
def pyramid(n,alpha):
    for i in range(0,n):
        print(" "*(n-i),end=" ")
        for j in range(0,i+1):
            print(chr(alpha),end=" ")
        
        print()
n=5
alpha=int(input())
pyramid(n,alpha)