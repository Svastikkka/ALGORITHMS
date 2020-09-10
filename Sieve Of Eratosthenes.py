"""
Getting Prime Number using SieveOfEratosthenes
"""
l=int(input())
p=2 #set the starting node
prime = [True for i in range(l + 1)] #create a prime list and make all elements set to TRUE
prime[0] = False
prime[1] = False
while p*p <=l:
    if prime[p]==True:
        for i in range(p*2,l+1,p):
            prime[i]=False
    p=p+1

"""
This loop basically for printing prime numbers
"""
for p in range(l+1):
    if prime[p]:
        print(p)

