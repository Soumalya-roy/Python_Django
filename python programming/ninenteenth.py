class Calculator:
    def __init__(self):
        print("init")
    def sum(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
a=int(input())
b=int(input())
print(Calculator.sum(a,b))
print(Calculator.sub(a,b))
print(Calculator.mul(a,b))
print(Calculator.div(a,b))