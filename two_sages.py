>>>pr=[2,3,5,7]
>>> z=[]
>>> for x in pr:
	    for y in pr:
		    z.append(x*y)
>>> z=sorted(z)
>>> z1=[]
>>>i=0
>>> while i<len(z):
	    if z[i]>10:
		    z1.append(z[i])
		    del z[i]
	    else:
		    i+=1
