def avg(*n):
    s=0
    for x in n:
        s=s+x
    return s / len(n)
x= avg(10,20,30,40,50)
print("average is",x)