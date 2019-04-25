сортировка выбором 
>>> def bubble_sort(lst):
    nums = list(lst)
    for i in range(len(lst)):
        print("i=",i)
        for j in range(i+1, len(lst)):
            print("j=",j)
            if lst[j] < lst[i]:
                print("_j=",j)
                lst[j], lst[i] = lst[i], lst[j]
                print(lst)
    return lst

>>> l=[1, 2, 3, 5, 6, 4]
>>> bubble_sort(l)
i= 0
j= 1
j= 2
j= 3
j= 4
j= 5
i= 1
j= 2
j= 3
j= 4
j= 5
i= 2
j= 3
j= 4
j= 5
i= 3
j= 4
j= 5
_j= 5
[1, 2, 3, 4, 6, 5]
i= 4
j= 5
_j= 5
[1, 2, 3, 4, 5, 6]
i= 5
[1, 2, 3, 4, 5, 6]
>>> l=[1, 2, 3, 5, 7, 6, 4]
>>> bubble_sort(l)
i= 0
j= 1
j= 2
j= 3
j= 4
j= 5
j= 6
i= 1
j= 2
j= 3
j= 4
j= 5
j= 6
i= 2
j= 3
j= 4
j= 5
j= 6
i= 3
j= 4
j= 5
j= 6
_j= 6
[1, 2, 3, 4, 7, 6, 5]
i= 4
j= 5
_j= 5
[1, 2, 3, 4, 6, 7, 5]
j= 6
_j= 6
[1, 2, 3, 4, 5, 7, 6]
i= 5
j= 6
_j= 6
[1, 2, 3, 4, 5, 6, 7]
i= 6
[1, 2, 3, 4, 5, 6, 7]
>>> 
