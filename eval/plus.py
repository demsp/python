# https://habr.com/ru/post/227119/

def eval(list_or_atom):
    if isinstance(list_or_atom, tuple):
		    fn, *fn_args = [eval(item) for item in list_or_atom]
		    return fn(*fn_args)
    else:
		    return list_or_atom
def plus(*args):
    return sum(args)

eval((plus, 3, 4, 5))
#12
def listsum(numList):
    theSum = 0
	  for i in numList:
		    theSum = theSum + i
    return theSum
    
listsum([2,3,5]) #10

eval((listsum, [2, 3, 5])) #10

  
  
