def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)

n=int(input())
dn=n
s=0
while(dn!=0):
    s=s+fact(int(dn%10))
    # print(s)
    dn=dn/10

if(s==n):
    print("Krishnamurthy")
else:
    print("Not Krishnamurthy")