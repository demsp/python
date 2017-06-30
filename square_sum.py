# -*- coding: cp1251 -*-
#факториал
def fac(n):
     if n < 0:
          print "Error"
          return 1
     if n == 0:
          return 1
     return fac(n-1) * n
#сумма квадратов чисел (1,2,3,4...n)
def fuc(n):
     #n=n+2
     if n == 0:
          return 0
     return fuc(n-1) + n**2
#сумма n единиц
def fu(n):
     n=n-1
     if n == 0:
          return 1
     return fu(n) + 1  # * (n+1)
#квадрат числа n (1,3,5,7...)
def fuu(n):
     #n=n-2
     if n == -1:
          return 0#1
     #return fuu(n) +  n + 2
     return fuu(n-2) +  n
#квадрат числа n (1,2,3,4...)
def fun(n):
     n=2*n-1
     if n == -1:
          return 0
     return fuu(n-2) +  n  
#сумма квадратов числа n
def fun_pl(n):
     #x=fun(n)
     if n < 1:
          print "Error"
          return 1
     if n==1:
          return 1
     x=fun(n)
     return fun_pl(n-1) + x
     


