i=1
'''
while(i<5):
    print(i)
    i+=1

while(i<5):
    print(i,end='   ')
    i+=1

while(i<5):
    print(i,end="   ")
    if(i==2):
        print("")
    i+=1
    
while(i<31):
    print(i,end="-")
    if(i%10==0):
        print("")
    i+=1
'''
while(i<31):
    print(i,end="")
    if(i%10==0):
        print("")
    else:
        print("-",end="")
    i+=1