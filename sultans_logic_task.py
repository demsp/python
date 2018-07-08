#  сумма не превышает 100
#  subtact_nums(range(4,101),(sum_nums(prime_nums)))
# [11, 17, 23, 27, 29, 35, 37, 41, 47, 51, 53, 57, 59, 65, 67, 71, 77, 79, 83, 87, 89, 93, 95, 97]

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
# произведения слагаемых, образующих суммы
>>> def mult_summands(summands):
	arr=[]
	for i in range(2,30):
		for j in range(2,30):
			for k in summands:
				if i+j==k:
					arr.append(i*j)
	return arr

#  mult_summands(subtact_nums(range(4,101),sum_nums(prime_nums)))
>>> sorted(set(mult_summands(subtact_nums(range(4,101),sum_nums(prime_nums)))))
[18, 24, 28, 30, 42, 50, 52, 54, 60, 66, 70, 72, 76, 78, 90, 92, 100, 102, 110, 112, 120, 126, 130, 132, 138, 140, 152, 154, 162, 168, 170, 174, 176, 180, 182, 190, 196, 198, 
 204, 208, 210, 216, 232, 234, 250, 252, 264, 270, 276, 286, 294, 300, 304, 306, 312, 322, 330, 336, 340, 342, 348, 364, 378, 390, 400, 
 408, 414, 418, 420, 522, 532, 540, 546, 550, 552, 638, 644, 648, 650, 696, 700, 702, 812]

##			##		##
>>> def mult_summands_k(k):
	arr=[]
	for i in range(2,30):
		for j in range(2,30):
			if i+j==k:
				arr.append(i*j)
	return arr

>>> mult_summands_k(11)
[18, 24, 28, 30, 30, 28, 24, 18]
>>> mult_summands_k(17)
[30, 42, 52, 60, 66, 70, 72, 72, 70, 66, 60, 52, 42, 30]
>>> sorted(set(mult_summands_k(23)))
[42, 60, 76, 90, 102, 112, 120, 126, 130, 132]
>>> sorted(set(mult_summands_k(27)))
[50, 72, 92, 110, 126, 140, 152, 162, 170, 176, 180, 182]

>>> def sets_mult_summands_k(k):
	arr=[]
	for i in k:
		arr.append(set(mult_summands_k(i)))
	return arr

>>> sets_mult_summands_k(subtact_nums(range(4,101),(sum_nums(prime_nums))))
[{24, 18, 28, 30}, {66, 70, 72, 42, 52, 60, 30}, {130, 132, 102, 42, 76, 112, 120, 90, 60, 126}, 
 {162, 72, 170, 140, 110, 176, 50, 180, 182, 152, 92, 126}, {100, 198, 168, 138, 204, 78, 208, 210, 180, 54, 120, 154, 190}, 
 {196, 294, 264, 234, 300, 174, 304, 306, 276, 216, 250, 286}, {322, 232, 330, 300, 270, 336, 340, 342, 312, 252, 286}, 
 {418, 420, 390, 364, 400, 408, 378, 348, 414}, {546, 550, 552, 522, 532, 540}, {648, 650, 644, 638}, {696, 700, 702},
 {812}, set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]

      
      
            
