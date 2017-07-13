s=[1,2,3,0]
s1=[1,2,0,3,0,4]
var=0
ind=[]
# удаление до первого нуля, вывод счетчика
def ff(s,v):
    if s[0]!=0:
        v=v+1
        print(v)
        s.remove(s[0])
        ff(s,v)
    else:
        print("!!!")
#ff(s,var)
#вывод всего, кроме нулей
def ff_1(s,i,v):
    if s!=[]:
        if s[0]!=0:
            v=v+1
            i.append(v)
            print(v)
            s.remove(s[0])
            ff_1(s,i,v)
        else:
            v=v+1
            s.remove(s[0])
            ff_1(s,i,v)
    else:
        print("list is empty")
#ff_1(s1,ind,var)

# добавление элементов в конец нового массива
def ff_2(s,i):
    if s!=[]:
        if s[0]!=0:
            i.append(s[0])
            print(i)
            s.remove(s[0])
            ff_2(s,i)
        else:
            s.remove(s[0])
            ff_2(s,i)
    else:
        print ("List is empty")
#ff_2(s,ind)
        
# замена нулями        
def ffc(s,v):
    
    if v<=6:
        s[v]=0
        print(v)
        v=v+1
        ffc(s,v)
    else:
        print("XXXX")
    #v=v+1
#ffc(s,var)    
