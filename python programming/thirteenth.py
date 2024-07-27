L1=eval(input("Set1 = "))
L2=eval(input("Set2 = "))
I=[]
U=[]
S1=[]
S2=[]
for i in L1:
    if(i in L2):
        I.append(i)
        U.append(i)
    else:
        S1.append(i)
        U.append(i)
for i in L2:
    if i not in L1:
        S2.append(i)
        U.append(i)
print(I,U,S1,S2)
if S2 == []:
    print("SuperL1")
    print("SubL2")
if S1 == []:
    print("SuperL2")
    print("SubL1")