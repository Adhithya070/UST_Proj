class addsub():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):return self.a+self.b
    def sub(self): return self.a-self.b

class muldiv():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def mul(self):return self.a*self.b
    def div(self): return self.a/self.b

def main():
    o1=addsub(2,1)
    o2=addsub(4,3)
    print(o1.add())
    print(o1.sub())
    print(o2.add())
    print(o2.sub())

if __name__=='__main__' :
    main()
else:
    o3 = muldiv(4,2)
    o4 = muldiv(6,3)
    print(o3.mul())
    print(o3.div())
    print(o4.mul())
    print(o4.div())