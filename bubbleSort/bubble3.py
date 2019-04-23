>>> def bubble1(lst):
	i=0
	j=0
	while i<len(lst)-1:
		if lst[i+1]<lst[i]:
			print("min_i=",lst[i+1])
			lst[i], lst[i+1] = lst[i+1], lst[i]
			print(lst)
			j=i
			while j>0:
				if lst[j-1]>lst[j]:
					print("j=",j)
					print("min_j=",lst[j])
					lst[j],lst[j-1]=lst[j-1],lst[j]
					print(lst)
				j-=1
		i+=1
	return lst

>>> l=[1, 2, 3, 5, 6, 4]
>>> bubble1(l)
min_i= 4
[1, 2, 3, 5, 4, 6]
j= 4
min_j= 4
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>> 
>>>
>>> l=[2,3,7,4,5,6,1]
>>> bubble1(l)
min_i= 4
[2, 3, 4, 7, 5, 6, 1]
min_i= 5
[2, 3, 4, 5, 7, 6, 1]
min_i= 6
[2, 3, 4, 5, 6, 7, 1]
min_i= 1
[2, 3, 4, 5, 6, 1, 7]
j= 5
min_j= 1
[2, 3, 4, 5, 1, 6, 7]
j= 4
min_j= 1
[2, 3, 4, 1, 5, 6, 7]
j= 3
min_j= 1
[2, 3, 1, 4, 5, 6, 7]
j= 2
min_j= 1
[2, 1, 3, 4, 5, 6, 7]
j= 1
min_j= 1
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
>>> 
