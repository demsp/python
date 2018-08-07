def reciprocal(c,y0,n):
	arr=[]
	for i in range(n):
		arr.append(y0)
		y0=y0*(2-c*y0)
	return arr
