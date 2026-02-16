# def calc(a,b):
#     print('sum:',a+b)
#     print('product:',a*b)
# calc(10,20)

# n=int(input("enter any no."))
# def square(n):
#     print("square of {} is {}".format(n,n*n))
# square(10)
# square(n)

# def add(x,y):
#     print("sumof {} and {} is {}".format(x,y,x+y))
# add(10,12)

# def add(x,y):
#     return x+y
# result=add(10,20)
# print('the sum:',result)

# def validate(mobile_number):
#     if len(mobile_number)==10:
#         print(True)
#     else:
#         print(False)
# mobile_number=input("enter the mobile number:")
# result=validate(mobile_number)

# if result==True:
#     print("nice to see you again please proceed forward")

# def chek(number):
#     if number%2==0:
#         print("the number {} is even".format(number))
#     else:
#         print("the number {} is odd".format(number))
# number=int(input("enter the mobile number:"))
# chek(number)
# chek(15)

# def show(n):
#     result=1
#     while n>1:
#         result=result*n
#         n=n-1
#     print(result)
# for i in range(1,11):
#     print("the factorial of {} is {}".format(i,show(i)))

# n=int(input("enter the number:"))
# print(show(n))

# def show(n):
#     result=1
#     while n>1:
#         result=result*n
#         n=n-1
#     print("the factorial of {} is {}".format(i,result))
# for i in range(1,11):
#     show(i)

## filter function = for filtering the values as per the condition###

# l=[0,5,10,15,20,25,30,35,40,45,50]
# output=list(filter(lambda n: n%2 !=0,l))
# print(output)

# o=list(filter(lambda n: n%3 ==0,l))
# print(o)

## map function = for maping the values as per the given data

# l=[0,5,10,15,20,25,30,35,40,45,50]
# output=list(map(lambda n:2*n ,l))
# print(output)

# l=[0,5,10,15,20,25,30,35,40,45,50]
# output=list(map(lambda n:n**2 ,l))
# print(output)

# def sum(*n):
#     for i in n:
#         print(i)

# sum(10,"durga") 
 


# def sum(n,*x):
#     print(n)
#     print(x)
# sum(10,20,30,40,50)

# def sum(*n,x,y,z):
#     print(*n)
#     print(x,y,z)
# sum(10,20,30,x=40,y=50,z=60)

## RECUSIVE FUNCTION ##
# def factorial(n):
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     return result
# print("factorial of 5 is:",factorial(5))

# s=lambda a,b:a+b
# print(s(10,20))

# s=lambda a,b:a if a>b else b
# print(s(10,20))
# print(s(200,100))

# s=lambda a,b,c:a if a>b and a>c else b if b>c else c
# print(s(20,10,30))
# print(s(30,20,10))
# print(s(10,30,20)) 

### FILTER FUNCTION ###
# l=[1,2,3,4,5,6,7,8]
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# output=list(filter(is_even,l))
# print(output) 

# l=[1,2,3,4,5,6,7,8]
# output=list(filter(lambda n:n%2==0,l))
# print(output)

# l=[1,2,3,4,5,6,7,8]
# even=list(filter(lambda n:n%2==0,l))
# odd=list(filter(lambda n:n%2!=0,l))
# print(even)
# print(odd)

# class employ():
#     def __init__(self,name,sal,age,has_gf):
#         self.name=name
#         self.sal=sal
#         self.age=age
#         self.has_gf=has_gf

#     def display(self):
#         return self.name,self.age
        
# e1=employ('vivek',9000,18,True)
# e2=employ('omi',8000,17,True)
# e3=employ('chacha',3000,19,False)
# e4=employ('rohan',8000,21,True)
# e5=employ('nipu',7000,20,True)
# l=[e1,e2,e3,e4,e5]
# output=list(filter(lambda e:e.sal>5000 and e.age>17 and e.has_gf ,l))
# for e in output:
#    print(e.display())
# print("employ who can get bonas are:")
# output=list(filter(lambda e:e.sal<4000 or e.sal>7000,l))
# for e in output :
#     print(e.display())
# print("employes who can go for pub")
# output=list(filter(lambda e:(e.sal>5000 and e.age>17) and not (e.sal<4000 or e.sal>7000),l))
# for e in output:
#     print(e.display())

### MAP ###

# class employ():
#     def __init__(self,name,sal,age,has_gf):
#         self.name=name
#         self.sal=sal
#         self.age=age
#         self.has_gf=has_gf

#     def display(self):
#         return self.name,self.age
        
# e1=employ('vivek',9000,18,True)
# e2=employ('omi',8000,17,True)
# e3=employ('chacha',3000,19,False)
# e4=employ('rohan',8000,21,True)
# e5=employ('nipu',7000,20,True)
# l=[e1,e2,e3,e4,e5]
# output=list(map(lambda e:employ(e.name,e.sal+1000,e.age,e.has_gf),l))
# for e in output:
#     print(e.name,"....",e.sal) 

# l1=[1,2,3,4,5]
# l2=[10,20,30,40,50,60]
# output=list(map(lambda x,y:x*y,l1,l2))
# print(output)

### REDUCE ###
# from functools import *
# l=[10,20,30,40,50]
# result=reduce(lambda x,y:x+y,l)
# print(result)

# from functools import *
# l=range(1,101)
# result=reduce(lambda x,y:x+y,l)
# print(result)

# from functools import *
# result=reduce(lambda x,y:x+y,range(1,101))
# print(result)

# from functools import *
# result=reduce(lambda x,y:x*y,range(1,6))
# print(result)
