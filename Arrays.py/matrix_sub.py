def matrix_input():
    matrix=[]
    rows =int(input())
    columns=int(input())
    for i in range(rows):
        row=list(map(int,input().split()))
        if len(row)!=columns:
            break
        matrix.append(row)
    return matrix
A=matrix_input()
B=matrix_input()
result=matrix_input()
if len(A)==len(B):
    for i in range(len(A)):
        for j in range(len(B)):
                result[i][j]=A[i][j]-B[i][j]
    print(result)
