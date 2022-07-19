#sw1
class sw1:
    def str_int(str0):
        rt=int(str0)
        return rt

    def __init__(self):
        self.T=int(input())
        self.rt_array=[]
        for i in range(self.T):
            temp=input().split()
            temp1=[]
            for k in temp:
                temp1.append(int(k))
            self.rt_array.append([temp1[0]//temp1[1],temp1[0]%temp1[1]])
    def print_sw1(self):
        for i in range(self.T):
            print("#"+str(i)+" "+str(self.rt_array[i][0])+" "+str(self.rt_array[i][1]))
#obj=sw1()
#obj.print_sw1()
#sw2
class sw2:
    def __init__(self):
        self.N=int(input())
        self.str0=""
        while self.N+1:
            self.str0=self.str0+str(self.N)+" "
            self.N-=1
        print(self.str0)
#sw20=sw2()
#sw3
class sw3:
    def __init__(self):
        self.N=int(input())
        self.array0=[]
        self.rt=""
        for i in range(self.N):
            temp=0
            for k in range(10):
                temp+=int(input())
            self.array0.append(temp//10)
        for m in range(self.N):
            self.rt=self.rt+"#"+str(m+1)+" "+str(self.array0[m])+"\n"
        print(self.rt)
#sw03=sw3()
class sw4:
    def __init__(self):
        self.N=int(input())
        self.array0=[]
        self.rt=""
        for i in range(self.N):
            temp=0
            temp+=int(input())
            temp-=int(input())
            if(temp>0):
                self.array0.append(">")
            elif(temp<0):
                self.array0.append("<")
            else:
                self.array0.append("=")
        for m in range(self.N):
            self.rt=self.rt+"#"+str(m+1)+" "+self.array0[m]+"\n"
        print(self.rt)
#sw04=sw4()
class py20:
    def __init__(self):
        self.N=int(input())
        self.rt=self.N%10
        while self.N:
            self.N=int(self.N/10)
            self.rt+=self.N%10
        print(self.rt)
#py_20=py20()
class py21:
    def __init__(self):
        self.N=int(input())
        self.rt=0
        while self.N:
            self.rt*=10
            self.rt+=(self.N%10)
            self.N=int(self.N/10)
        print(self.rt)
#py_21=py21()