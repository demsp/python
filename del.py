>>> lst = [ 1,2,3,4,5,6,4,2,8,1]
>>> out = []
>>> for x in lst:
    if not x in out:
        out.append(x)

        
>>> out
[1, 2, 3, 4, 5, 6, 8]

>>> a=[1,2,3,4,5]
>>> b=[1,2,3]
>>> c=[]
>>> for x in a:
	if not x in b:
		c.append(x)

		
>>> c
[4, 5]
