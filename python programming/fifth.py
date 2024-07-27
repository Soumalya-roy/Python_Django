n=int(input("Enter the no. of Terms :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="") 
    for j in range(0,(n-i+1)*2-3):
        print(" ",end="")
    for j in range(1,i+1):
        if(i!=n):
            print("*",end="") 
    if(i==n):
        print("*"*(n-1))
    print()