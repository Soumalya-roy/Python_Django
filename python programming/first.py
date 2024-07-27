m=int(input())
n=int(input())
L1=[]
L2=[]
s1=0
s2=0
for i in range(m,n):
    if(i%2==0):
        s1=s1+i
        L1.append(i)
    else:
        s2=s2+i
        L2.append(i)
print("Sum of even = ",s1)
print("Sum of odd = ",s2)
print("Even :")
for i in L1:
    print(i, end=' ')
print()
print("Odd :")
for i in L2:
    print(i, end=' ')