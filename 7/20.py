#1

class sw1:
    def __init__(self):
        self.N=int(input())
        self.array=""
        for i in range(1,self.N+1):
            if (self.N%i)==0:
                self.array=self.array+str(i)+" "
        print(self.array)
#sw01=sw1()
#2
class sw2:
    def __init__(self):
        self.N=int(input())
        self.array=""
        self.n=1
        for i in range(0,self.N+1):
            self.array=self.array+str(self.n)+" "
            self.n*=2
        print(self.array)
#sw02=sw2()
#3
class sw3:
    def __init__(self):
        self.str0=input().upper()
        self.rt=""
        for i in self.str0:
            self.rt=self.rt+str(ord(i)-ord("A")+1)+" "
        print(self.rt)
#sw03=sw3()
#4
class sw4:
    def __init__(self):
        self.N=int(input())
        self.n=0
        for i in range(1,self.N+1):
            if(i%2==0):
                self.n-=i
            else:
                self.n+=i
        print(self.n)
#sw01=sw4()
class sw5:
    def __init__(self):
        self.N=int(input())
        self.array=[]
        for k in range(1,self.N+1):
            for i in range(5):
                self.n=int(input())
                self.array.append(self.n)
            if(self.array[2]>self.array[4]):
                self.n=self.array[1]
            else:
                self.n=self.array[1]+(self.array[4]-self.array[2])*self.array[3]
            if(self.array[0]*self.array[4])<self.n:
                print("#"+str(k)+" "+str(self.array[0]*self.array[4]))
            else:
                 print("#"+str(k)+" "+str(self.n))
#sw05=sw5()