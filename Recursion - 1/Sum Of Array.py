def sum(arr):
    count=0
    if len(arr)<=1:
        return arr[0]
    else:
        count=count+arr[0]
    return count+sum(arr[1:])


num=int(input())
arr=list(map(int,input().split()))
print(sum(arr))