def power(base,a):
    if a!=0:
        return base*power(base,a-1)
    else:return 1

x,y=list(map(int,input().split()))
print(power(x,y))
