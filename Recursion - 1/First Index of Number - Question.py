"""MY CODE"""
def firstIndex(arr, x):
    # Please add your code here
    if arr[0]==x:
        return n-len(arr)
    if len(arr)==1 and arr[0]!=0:
        return int(-1)
    return firstIndex(arr[1:],x)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print("My Code",firstIndex(arr, x))



#SIR CODE
def firstIndex1(arr,x):
    if len(arr)==0:
        return -1
    if arr[0]==x:
        return 0
    smallerList= arr[1:]
    smallerListOutput=firstIndex1(smallerList,x)

    if smallerListOutput ==-1:
        return -1
    else:
        return smallerListOutput +1

print("Sir Code",firstIndex1(arr, x))

def firstIndex3(arr,x,i):
    if len(arr)==i:
        return -1
    if arr[i]==x:
        return i
    i= i+1
    smallerListOutput=firstIndex3(arr,x,i)

    if smallerListOutput ==-1:
        return -1
    else:
        return smallerListOutput


print("Sir Code",firstIndex3(arr, x,0))

