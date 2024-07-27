n=int(input("Enter : "))
try:
    i=2
    while i<=n/2 :
        if n%i==0 :
            i=0
            break
        i=i+1
    if i!=0 :
        print("Prime")
    else:
        print("Not Prime")
except:
    print("Error Found")