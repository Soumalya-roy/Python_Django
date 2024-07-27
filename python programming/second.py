n=int(input("Enter the terms :"))
n2=int(input("Enter the terms :"))
for i in range(n,n2):
    d=i
    r=0
    while(d!=0):
        r=r*10+d%10
        d=d/10
    if(i==r):
        print(i)
    