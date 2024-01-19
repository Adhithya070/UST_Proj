a,b,c,d,e,f="Indian","Cerificate",'Secondary','Education','Central','Board'
for i in ["ICSE","CBSE"]:
    for j in i:
        if(a[0]==j):print(j,' - ',a)
        elif(b[0]== j):
            if(i=="ICSE"):print(j,' - ',b)
            else:print(j,' - ',e)
        elif(c[0]==j): print(j,' - ',c)
        elif(d[0]== j): print(j,' - ',d)
        else: print(j,' - ',f)
    print("==========")
'''
x={'ICSE': ['Indian', 'Certificate', 'Secondary', 'Education'], 'CBSE': ['Central', 'Board', 'Secondary', 'Education']}
for i in x:
    for j in range(len(i)):print(i[j]," - ",x[i][j])
    print("==========")
'''