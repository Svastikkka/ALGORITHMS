def BinarySearch(a,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid] >x:
        ei =mid-1
        return  BinarySearch(a,x,si,ei)
    elif a[mid] <x:
        si=mid+1
        return  BinarySearch(a,x,si,ei)

a=[1,2,3,4,5,6]
print(BinarySearch(a,4,0,5))