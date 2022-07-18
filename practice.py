def char_upper(str0):
    int0={}
    for i in str0:
        try:
            if(int0[i]!=-1):
                int0[i]+=1
        except:
            int0[i]=1
    return int0
def print_dic(dic0):
    for i in dic0:
        print(str(i)+': '+str(dic0[i]))
    return None
print_dic(char_upper('banana'))
