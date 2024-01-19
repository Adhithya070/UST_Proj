l,c= ['G-M-Neeraj', 'S-M-Ravi', 'S-W-Mira', 'B-W-Sindhu', 'B-W-Lovlina', 'B-M-Hockey', 'B-M-Bajarang', 'Others'],1
for i in l:
    print('TOP',c,':',i)
    if (c == 3): break
    c+=1

print("")

#using range
for i in range(0,3):print('TOP',i+1,':',l[i])

print("")

for i in l:
    if i[0]=='G':print(i,':','GOLD')
    elif i[0] == 'S': print(i, ':', 'SILVER')
    else: break

#pattern
c=1
for i in l:
    if i[0]=='G':
        print("\nGOLD\n====")
    elif i[0] == 'S':
        if c!=2 :
            print("\nSILVER\n====")
            c+=1
    else: break
    print(i)

print("")

#for-else usage
for i in l:
    if i[2]=='W':print('Congragulations',i[4:])
else:print('Congragulations to all Gentlemen')