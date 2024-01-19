def rev(x):
    for i in range(len(x)-1,-1,-1):print(x[i],end="")
y=input("Enter string : ")
print("reverse : ",end="")
rev(y)