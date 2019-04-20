>>> arr=[0,1,2,8,7] 
>>> temp=0 
>>> for i in range(4): 
    if arr[i]>arr[i+1]: 
        temp=arr[i] 
        arr[i]=arr[i+1] 
        arr[i+1]=temp 
>>> arr 
[0, 1, 2, 7, 8] 
>>># WHILE 
>>> arr=[0, 3, 7, 1, 5] 
>>> i=0 
>>> temp=0 
>>> while i<5: 
    if arr[i]<arr[i-1]: 
        print arr[i] 
    i+=1 
>>> # WHILE SORT 
print("##############")
l=[0, 3, 7, 1, 5]; 
print (l) 
i=0; 
while i<len(l): 
        j = 0 
        while j<len(l)-1: 
            if l[j+1] < l[j]: 
                l[j], l[j+1] = l[j+1], l[j] 
            j += 1 
        i += 1 
print (l)
print("##############") 
l=[0, 3, 7, 1, 5]; 
print (l) 
i=0; 
j=0
while i<len(l): 
        j = i 
        while j<len(l)-1: 
            if l[j+1] < l[j]: 
                l[j], l[j+1] = l[j+1], l[j] 
            j += 1 
        i += 1 
print (l) 

print("##############") 
#l=[2,3,4,5,1,9,6,7,8] 
l=[2,4,3,5,1,9,6,7,8] 
print (l) 
i=0 
j=0 
while i<len(l)-1: 
            if l[i+1] < l[i]: 
                print ('min=',l[i+1]) 
                l[i], l[i+1] = l[i+1], l[i] 
                j=i 
                while j>0: 
                    print ('j=',j) 
                    if l[j-1]>l[j]: 
                        l[j], l[j-1] = l[j-1], l[j] 
                    j-=1 
            i += 1 
print (l)         
