# s=[10,20,30,40,50,60,70,80,90,100]
# v=sum(s)
# print(v)

# s=[1,2,3,4,5,6,7,8,9]
# for x in s:
#     if x%2==0:
#         print(x)

# s=[1,2,3,4,5,6,7,8,9]
# x=int(input("enter any element to find index:"))
# l=s.index(x)
# print('at {} place {} element is avilable'.format(l,x))

# s=[1,2,3,4,5,6,7,8,9]
# x=int(input("enter any element to find index:"))
# if x in s:
#  l=s.index(x)
#  print('at {} place {} element is avilable'.format(l,x))
# else:
#  print("cdvsdf")

# l=[]
# for x in range(101):
#     if x%10==0:
#         l.append(x)
#         print("{} is divisible by 10".format(x,))
#     else:
#         print("not divisible")
# print(l)

# l=[10,20,30,40,50]
# l.insert(-10,70) # added at begging 
# l.insert(7,60). #added at last
# print(l)

# l1=[10,20,30,40,50]
# l2=[60,70,80,90,100]
# l1.extend(l2)
# print(l1)

# l1=[10,20,30,40,50]
# l2=[60,70,80,90,100]
# print(l1+l2)

# l1=[10,20,30,40]. # cloning here different address{id}
# l2=l1.copy()
# l1[1]=777
# l2[1]=222
# print(l1)
# print(l2) 

# l1=[10,20,30,40] # alising here same address{id}
# l2=l1
# l1[2]=77
# print(l2)

# l1=[10,20,30,40]
# l1.extend('abc')
# print(l1)

# l=[10,20,30]
# print(3*l)

# l=[10,20,30]
# k=[100,20,30]
# m=['vivek','mhaske']
# n=['VIVEK','MHASKE']
# print(l==m) #False
# print(l>k) #False

# m=['vivek','mhaske']
# print('vivek' in m) #True

###.  NESTED LIST. ####
# l=[10,20,[12,34]]
# print(l[2]) # [12,34] #
# print(l[2][1]) # 34 #

# l=[[10,20,30],[40,50,60],[70,80,90]]
# for x in l:
#     for element in x:
#         print(element,end=' ')
#     print() 

# l=[[10,20,30],[40,50,60],[70,80,90]]
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(l[i][j],end=' ')
#     print()    

# l=[]
# for x in range(1,11):
#     l.append(x*x)
# print(l)

### LIST COMPRIENTION ###
# l=[x*x for x in range(1,11)]
# print(l)

# l=[x*x for x in range(1,11) if x%2 == 0]
# print(l)


# l=[]
# for x in range(1,11): 
#     if x%2==0:
#      l.append(x*x) 
# print(l)

# words=['vivek','irish','viraj','emy','kiran']
# l=[word[0] for word in words]
# print(''.join(l))

# num1=[10,20,30]
# num2=[100,20,30] 
# n=[]
# for x in num1:
#     if x not in num2:
#         n.append(x)
# print(n)

# num1=[10,20,30]
# num2=[100,20,30] 
# n=[ x for x in num1 if x not in num2]
# print(n)

# num1=[10,20,30]
# num2=[100,20,30] 
# n=[x for x in num1 if x in num2]
# print(n) 

# s='vivek mhaske you dont have a girlfriend'
# word=s.split()
# print(word)
# l=[]
# for x in word: 
#     l.append([x,len(x)])
# print(l)

# s='vivek mhaske you dont have a girlfriend'
# word=s.split()
# l=[[x,len(x)] for x in word ]
# print(l)

# s='vivek mhaske you dont have a girlfriend'
# word=s.split()
# l=[[x.capitalize(),len(x)] for x in word ]
# print(l)

# s=input('Enter any string:')
# for x in s:
#     if x in 'aeiou':
#       print(x,end=" ")




# s=input('Enter any string:')
# count=0
# for x in s:
#     if x in 'aeiou':
#         print(x,end=" ")
#         count=count+1
# print(count)


# s=input('Enter any string:')
# v=['a','i','o','u','e']
# f=[]
# for x in s:
#     if x in v:
#         f.append(x)
# print(f)

# s=input('Enter any string:')
# f=[x for x in s if x in 'aeiou']
# print(f)

