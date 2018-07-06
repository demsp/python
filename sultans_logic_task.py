>>> prime_nums=[3,5,7,11,13,17,19]
>>> def mult_nums(nums):
	    arr=[]
	    for i in nums:
	    	for j in nums:
			arr.append(i*j)
	    return arr
>>> def del_same(nums):
	    arr=[]
	    for i in nums:
	    	if not i in arr:
		        arr.append(i)
	    return arr

>>> def del_same(nums):
	nums=set(nums)
	return nums

>>> def sort_nums(nums):
	    nums=sorted(nums)
	    return nums  
>>> sort_nums(del_same(mult_nums(prime_nums)))
[9, 15, 21, 25, 33, 35, 39, 49, 51, 55, 57, 65, 77, 85, 91, 95, 119, 121, 133, 143, 169, 187, 209, 221, 247, 289, 323, 361]      
      
      
      
      
            
