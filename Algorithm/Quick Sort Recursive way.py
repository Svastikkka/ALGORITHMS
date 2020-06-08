def partion(a,si,ei):
    pivot=a[si]

    c=0 #count number of elements which are greater than initial pi[si]
    # below loop use to count the number of elements are greater than initial pi
    for i in range(si,ei+1):
        if a[i]<pivot:
            c=c+1
    a[si+c],a[si]=a[si],a[si+c] #swap
    pivot_index=si+c

    i=si
    j=ei
    while i<j:
        if a[i]<pivot:
            i=i+1
        elif a[j]>=pivot:
            j=j-1
        else:
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
    return pivot_index








def QuickSort(a,si,ei):
    if si>ei:
        return
    pi=partion(a,si,ei)
    QuickSort(a,si,pi-1)
    QuickSort(a,pi+1,ei)

arr=[6,5,4,3,7,8,9,1,2]
print(partion(arr,0,len(arr)-1))

print(QuickSort(arr,0,len(arr)-1))
print(arr)