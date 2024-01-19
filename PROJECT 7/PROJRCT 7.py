#localhos=127.0.0.1
import pymongo as mo
'''
c=mycl.get_database('MBCETDATABASE')
d=c.get_collection('EMPLOYEE')
'''
def conpy():
    global mycl
    global dblist
    mycl=mo.MongoClient("mongodb://localhost:27017/")
    dblist=mycl.list_database_names()
    print(dblist)

def chdbex():
    if('MBCETDATABASE' in dblist):
        print('my database exists')

def fitstrow():
    c=mycl['MBCETDATABASE']['EMPLOYEE']
    for i in c.find_one():
        if (i != '_id'):
            print(c.find_one()[i], end="   ")

def all():
    d = mycl['MBCETDATABASE']['EMPLOYEE']
    doc = d.find()
    for i in doc:
        print(i)

def rowcrit():
    d = mycl['MBCETDATABASE']['EMPLOYEE']
    q={'Dept':'Sales'}
    c=d.find(q,{'_id':0, 'EmpName':1,'Dept':1})
    for rec in c:
        print(rec)

def insert():
    d = mycl['MBCETDATABASE']['EMPLOYEE']
    n=int(input("\nEnter how many emp to add : "))
    for i in range(n):
        n1, n2, n3, n4 = int(input("Enter EmpID : ")), (input("Enter EmpName : ")), (input("Enter Dept : ")), (input("Enter Email : "))
        data={'EmpID':n1, 'EmpName':n2, 'Dept':n3, 'Email':n4}
        d.insert_one(data)

def delrec():
    d = mycl['MBCETDATABASE']['EMPLOYEE']
    n = int(input("Enter EmpID to remove : "))
    x = d.find({}, {'_id': 0, 'EmpID': 1})
    j = []
    for i in x:
        j.append(i['EmpID'])
    if n in j:
        q = {'EmpID': n}
        c = d.find(q, {'_id': 0, 'EmpName': 1, 'Dept': 1})
        for i in c: print(i, "was deleted")
        d.delete_one({"EmpID": n})
    else:
        print("rec not found")


def sort():
    d = mycl['MBCETDATABASE']['EMPLOYEE']
    doc = d.find({}, {'_id': 0}).sort("EmpName")
    doc1 = d.find({}, {'_id': 0}).sort("EmpName",-1)
    for i in doc:
        print(i)
    print("")
    for i in doc1:
        print(i)

def drop():
    mycl['MBCETDATABASE']['EMPLOYEE'].drop()

def updt():
    d = mycl['MBCETDATABASE']['EMPLOYEE']
    n = int(input("Enter EmpID to update : "))
    x = d.find({}, {'_id': 0, 'EmpID': 1})
    j = []
    for i in x:
        j.append(i['EmpID'])
    if n in j:
        n2, n3, n4 = input("Enter new name : "), input("Enter New Dept : "), input("Enter new Email : ")
        data = {"EmpName": n2, "Dept": n3, "Email": n4}
        q = {'EmpID': n}
        c = d.find(q, {'_id': 0, 'EmpID': 0})
        for i in c:
            y = i
            print(i, "changed to", end=" ")
        d.update_one(y, {"$set": data})
        print(data)
    else:
        print("rec not found")

def limit():
    d = mycl['MBCETDATABASE']['EMPLOYEE']
    res=d.find({},{'_id':0}).limit(6)
    for i in res:
        print(i)

if __name__ == '__main__' :
    conpy()
    print("")
    chdbex()
    print("")
    fitstrow()
    print("")
    insert()
    print("")
    delrec()
    print("")
    all()
    print("")
    #drop()
    print("")
    rowcrit()
    print("")
    sort()
    print("")
    updt()
    print("")
    limit()
