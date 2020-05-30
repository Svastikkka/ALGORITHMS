def merge(s1,s2,arr):
    i=0
    j=0
    k=0
    while i<len(s1)and j<len(s2):
        if s1[i]<s2[j]:
            arr[k]=s1[i]
            k=k+1
            i=i+1
        else:
            arr[k]=s2[j]
            k=k+1
            j=j+1
    while i < len(s1):
        arr[k] = s1[i]
        k = k + 1
        i = i + 1
    while j < len(s2):
        arr[k] = s2[j]
        k = k + 1
        j = j + 1


def mergeSort(arr):
    # Please add your code here
    if len(arr)==0 or len(arr)==1:
        return

    mid=(len(arr))//2
    s1=arr[0:mid]
    s2=arr[mid:]
    mergeSort(s1)
    mergeSort(s2)

    merge(s1,s2,arr)



# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(arr)
