i=5
'''
j=i-1
while(i>1):
    print(i,end=" ")
    print(j)
    if(j<2):
        i-=1
        j=i
        print("===")
    j-=1
'''
while(i>=2):
    j=i-1
    while(j>=1):
        print(i,j)
        j-=1
    print("===")
    i-=1