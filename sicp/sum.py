# sicp. page 71

>>> def inc(n):
	return n+1
>>> inc(5)
6
>>> def cube(x):
	return x*x*x
>>> cube(2)
8


>>> def sum(a,b):
	if(a>b):
		return 0
	else:
		return cube(a)+sum((inc(a)),(b))

	
>>> sum(1,5)
225
