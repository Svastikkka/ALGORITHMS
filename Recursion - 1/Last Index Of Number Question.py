def lastIndex(arr, x):
    if len(arr)==0:
        return -1

    smallerList = arr[1:]
    smallerListOutput = lastIndex(smallerList, x)
    if smallerListOutput !=-1:
        return smallerListOutput+1
    else:
        if arr[0] == x:
            return 0
        else:return -1


def lastIndex2(arr, x,i):
    if len(arr)==i:
        return -1

    smallerListOutput = lastIndex2(arr, x,i+1)
    if smallerListOutput !=-1:
        return smallerListOutput
    else:
        if arr[i]==x:
            return i
        else:
            return -1


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(lastIndex2(arr, x))
print(lastIndex2(arr, x,0))