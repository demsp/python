#  subtact_nums(range(4,201),(sum_nums(prime_nums1)))
>>> prime_nums=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
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
##		##		##
 >>> def sum_nums(nums):
	arr=[]
	for i in nums:
		for j in nums:
			arr.append(i+j)
	return arr
>>> def subtact_nums(nums1,nums2):
	arr=[]
	for i in nums1:
		if not i in nums2:
			arr.append(i)
	return arr
# сумма не превышает 100
>>> subtact_nums(range(4,101),sum_nums(prime_nums))
[11, 17, 23, 27, 29, 35, 37, 41, 47, 51, 53, 57, 59, 65, 67, 71, 77, 79, 83, 87, 89, 93, 95, 97]
##		##		##
>>> arr=[]
>>> for i in range(2,11):
	for j in range(2,11):
		if i+j==11:
			arr.append(i*j)

			
>>> arr
[18, 24, 28, 30, 30, 28, 24, 18]


      
      
      
            
