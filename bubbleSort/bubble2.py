>>> def bubble(lst):
	i=0
	while i<len(lst):
		j=0
		while j<len(lst)-1:
			if lst[j+1]<lst[j]:
				print("j=",j)
				lst[j],lst[j+1]=lst[j+1],lst[j]
				print(lst)
			j+=1
		i+=1
	return lst

>>> l=[1, 2, 3, 5, 6, 4]
>>> bubble(l)
j= 4
[1, 2, 3, 5, 4, 6]
j= 3
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>> 
