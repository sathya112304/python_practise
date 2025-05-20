n=int(input())
arr=list(map(int,input().split()))
add_number=int(input())
number=int(''.join(map(str,arr)))
new_number=number+add_number
result=list(map(int,str(new_number)))
print(*result)