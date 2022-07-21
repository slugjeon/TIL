#1
class sw1:
    def end(self):
        for i in range (10):
            if(i not in self.dict0):
                return False
        return True

    def __init__(self):
        self.N=int(input())
        self.array=[]
        self.dict0={}
        temp=1
        self.cnt=1
        for i in range(self.N):            
            self.array.append(int(input()))
            while(True):
                temp=self.cnt*self.array[i]
                while(temp):
                    if(temp%10 not in self.dict0):
                        self.dict0[temp%10]=-1
                    temp=int(temp//10)
                if(self.end()):break
                self.cnt+=1
            print("#"+str(i+1)+" "+str(self.cnt*self.array[i]))
            self.cnt=1
            self.dict0.clear()
#sw01=sw1()
class sw2:
    def __init__(self):
        self.N=int(input())
        self.array=[]
        self.dict0={}
        for i in range(self.N):            
            self.array.append(input())
            temp=len(self.array[i])
            rt=True
            for k in range(temp//2):
                if(self.array[i][k]!=self.array[i][-k-1]):
                    rt=False
                    break
            if(rt==True):
                print("#"+str(i+1)+" "+str(1))
            else:
                print("#"+str(i+1)+" "+str(0))
#sw02=sw2()
class sw3:
    def __init__(self):
        self.N=int(input())
        self.array=[]
        self.answer=[]
        self.dict0={}
        temp0=0
        temp1=0
        for i in range(self.N):            
            self.answer.append("")
            for k in range(4):
                self.array.append(int(input()))
            temp0=(self.array[1+i*4]+self.array[3+i*4])%60
            if(temp0>60):
                temp1=self.array[0+i*4]+self.array[2+i*4]+1
                temp1=temp1%12
                if(temp1==0):
                    temp1=12
            else:
                temp1=self.array[0+i*4]+self.array[2+i*4]
                temp1=temp1%12
                if(temp1==0):
                    temp1=12
            self.answer[i]="#"+str(i+1)+" "+str(temp1)+" "+str(temp0)
#sw03=sw3()
#for i in range(sw03.N):
#    print(sw03.answer[i])
class sw4:
    def __init__(self):
        self.N=int(input())
        temp0=0
        cnt=0
        answer=""
        for i in range(1,self.N+1):
            temp0=i
            cnt=0
            while temp0:
                if(temp0%3==0):
                    cnt+=1
                temp0=temp0//10
            if(cnt==0):
               answer=answer+str(i)+" "
            else:
                for k in range(cnt):
                    answer=answer+"-"
                answer=answer+" "
        print(answer)
sw04=sw4()
