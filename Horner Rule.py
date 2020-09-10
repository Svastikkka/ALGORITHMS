
#Link:- https://www.svastikkka.com/2020/08/horner-rule.html

def Poly(arr,value,lenght):
    result=arr[0]
    for i in range(1,lenght):
        result=result*value+arr[i]
    return result

arr=list(map(int,input().split()))
value=int(input())
length=len(arr)
print(Poly(arr,value,length))
