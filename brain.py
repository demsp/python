>>> def inp(command):
	arr=0
	command = input ("Input command(0-Exit)")
	if command>0:
		arr=arr+1
		print arr
		inp(command)
	else:
		return 0

	
>>> inp(1)
Input command(0-Exit)1
1
Input command(0-Exit)1
1
Input command(0-Exit)
