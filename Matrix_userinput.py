rows =int(input())
columns=int(input())
matrix=[]
for i in range(rows):
    row=list(map(int,input().split()))
    if len(row)!=columns:
        break
    matrix.append(row)
print(matrix)