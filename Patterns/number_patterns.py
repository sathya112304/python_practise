#Pyramid number pattern
def number_pattern(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(1,2*i):
            print(i,end=" ")
        print()
    
n=int(input())
number_pattern(n)

# Left aligned pyramid
def number_pattern(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(0,i):
            print(i,end=" ")
        print()

# Right aligned pyramid    
n=int(input())
number_pattern(n)

def number_pattern(n):
    for i in range(1,n+1):
        for j in range(0,i):
            print(i,end=" ")
        print()
    
n=int(input())
number_pattern(n)

# pyramid pattern with incerasing order
def number_pattern(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print("",end=" ")
        for k in range(1,i+1):
            print(k,end=" ")
        print()
    
n=int(input())
number_pattern(n)