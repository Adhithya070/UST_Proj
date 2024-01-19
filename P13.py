def sum(a,b):
    s=a+b
    return s
def sub(a,b):
    s=a-b
    return s
def mul(a,b):
    s=a*b
    return s
def div(a,b):
    s=a/b
    return s
def mod(a,b):
    s=a%b
    return s
print("Calculator using Python\n1. SUM\n2. SUB\n3. MUL\n4. DIV\n5. MOD\n6. EXIT")
t=1
while t!=6:
    t=int(input("Enter choice : "))
    if t == 6:
        print("EXIT")
        break
    a,b=int(input("enter 1stno : ")),int(input("enter 2ndno : "))
    if t==1:print(a,"+",b,"=",sum(a,b))
    elif t == 2: print(a, "-", b,"=", sub(a,b))
    elif t == 3: print(a, "*", b,"=", mul(a,b))
    elif t == 4: print(a, "/", b,"=", div(a,b))
    elif t == 5: print(a, "%", b,"=", mod(a,b))
    else : print("INVALID")
'''
def lof2(a,b):
    if(a>b):return a
    else:return b
sum=lambda a,b:a+b
a=int(input("enter 1stno : "))
b=int(input("enter 2ndno : "))
print("greatest =",lof2(a,b))
print("greatest =",sum(a,b))
'''