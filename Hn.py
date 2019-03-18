>>> def Hn(inc,count):
	count=count+1.0/inc
	print("count=",count)
	print("inc=",inc)
	inc=inc+1
	if inc<=2199023255552:
		Hn(inc,count)

>>> Hn(1099511627777,0)
