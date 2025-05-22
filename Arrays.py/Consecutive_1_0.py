arr=[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]    
max_count,count=0,1
for i in range(1,len(arr)):
    if arr[i]==arr[i-1]:
        count+=1
    else:
        max_count=max(max_count,count)
        count=1
print(max(max_count,count))