; sicp 1.3.1

>>> def inc(n):
	return n+1

>>> inc(5)
6
>>> def cube(x):
	return x*x*x

>>> cube(2)
8
>>> def sum_cubes(a,b):
	if (a>b):
		return 0
	else:
		return cube(a)+sum_cubes((a+1),b)
	
>>> sum_cubes(1,5)
225
