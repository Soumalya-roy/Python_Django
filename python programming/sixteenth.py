# def fact(n):
#     f=1
#     if n==0 or n==1 :
#         return 1
#     return n*fact(n-1)
# r=(lambda n: fact(n))(5)
# print("Sum is ",r)

s=lambda a:1 if a==0 else a*s(a-1)
print(s(5))