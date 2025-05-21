def diagonal_sum(matrix,n):
    primary=0
    secondary=0
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                primary+=matrix[i][j]
            if (i+j)==(n-1):
                secondary+=matrix[i][j]
    print(primary)   
    print(secondary)

matrix=[]
n=int(input())
columns=n
for _ in range(0,n):
    row=list(map(int,input().split()))
    if len(row)!=columns:
        exit()
    matrix.append(row)
diagonal_sum(matrix,n)

# sum of matrix elements without diagonals
def diagonal_sum(matrix,n):
    total_sum=0
    for i in range(0,n):
        for j in range(0,n):
            if i==j or (i+j)==n-1:
                continue
            total_sum+=matrix[i][j]
            
    print(total_sum)   

matrix=[]
n=int(input())
columns=n
for _ in range(0,n):
    row=list(map(int,input().split()))
    if len(row)!=columns:
        exit()
    matrix.append(row)
diagonal_sum(matrix,n)