i=15
j=14
while(j>=10):
    print(i,end="")
    if(i%10==1):
        if(i!=51):
            print(" ** ",end=" ")
        i+=j
        j-=1
    else:
        print(", ", end="")
        
    i-=1