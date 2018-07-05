>>> s1=[3,5,0,0,30,0,40,50]
>>> ind=[]
>>> var=0
>>> def ff_1(s,i,v):
    if s!=[]:
        if s[0]!=0:
            v=v+1
            i.append(s[0]) #i.append(v)
            print(s[0])    #print(v)
            s.remove(s[0])
            ff_1(s,i,v)
        else:
            v=v+1
            s.remove(s[0])
            ff_1(s,i,v)
    else:
        print("list is empty")

        
>>> ff_1(s1,ind,var)

3
5
30
40
50
list is empty
