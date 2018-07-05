>>> s1=[3,5,0,0,30,0,40,50]
>>> ind=[]
>>> def ff_1(s,i): 
    if s!=[]:
        if s[0]!=0:
            i.append(s[0])
            s.remove(s[0])
            ff_1(s,i)
        else:
            s.remove(s[0])
            ff_1(s,i)
    else:
	  print("list is empty")
>>>ff_1(s1,ind)
>>>>ind
[3, 5, 30, 40, 50]
