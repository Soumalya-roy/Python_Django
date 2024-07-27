y=int(input("Enter no. of years : "))
L=[]
s=0
print("Enter sgps marks(out of 10) : ")
for i in range (0,2*y):
    m=int(input())
    L.append(m)
    s=s+m
c=s/(2*y)
print("Cgpa = ",c)