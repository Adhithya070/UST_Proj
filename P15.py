'''
#square
x=int(input("Enter no of len  : " ))
for i in range(x):
    print(x*"*  ")

#rectangle
x=int(input("Enter no of len  : " ))
y=int(input("Enter no of breadth  : " ))
for i in range(y):print(x*"*  ")

#right tri lefr
x=int(input("Enter no of len  : " ))
for i in range(x+1):print(i*'* ')

#right tri right
x=int(input("Enter no of len  : " ))
for i in range(x+1):
    print((x-i)*"  ",end="")
    print(i*'* ')

#right tri lefr rev
x=int(input("Enter no of len  : " ))
for i in range(x,-1,-1):print(i*'* ')

#right tri right rev
x=int(input("Enter no of len  : " ))
for i in range(x,-1,-1):
    print((x-i)*"  ",end="")
    print(i*'* ')

#pyramid
x=int(input("Enter no of len  : " ))
for i in range(x+1):
    print((x-i)*" ",end="")
    print(i*'* ')

#pyramid rev
x=int(input("Enter no of len  : " ))
for i in range(x,-1,-1):
    print((x-i)*" ",end="")
    print(i*'* ')
'''
#diamond
x=int(input("Enter no of len  : " ))
for i in range(x+1):
    print((x-i)*" ",end="")
    print(i*'* ')
for i in range(x-1,-1,-1):
    print((x-i)*" ",end="")
    print(i*'* ')