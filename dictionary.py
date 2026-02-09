# d={}
# d[100]='vivek'
# d[20]='omi'
# d[50]='chacha'
# d[50]= 'rohan'
# print(d)

# d={100: 'vivek', 20: 'omi', 50: 'chacha'}
# key=int(input("enter the key to see the value:"))
# if key in d:
#     print(d[key])
# else:
#     print("enter the correct key")

# d={}
# while True:
#     name=input("Enter the student name:")
#     marks=input("Enter the students marks:")
#     d[name]=marks
#     print("thanks for sharing your details")
#     option=input("would you like to share another students details:[yes/no]:")
#     while True:
#         if option.lower()=='no':
#             break
#         elif option.lower()=='yes':
#             break
#         else:
#             option=input("Enter only yes or no:")
#     if option.lower()=='no':
#         break
# print(d)


# d={}
# while True:
#     name=input("Enter the student name:")
#     marks=input("Enter the students marks:")
#     d[name]=marks
#     print("thanks for sharing your details")
#     option=input("would you like to share another students details:[yes/no]:")
#     while True:
#         if option.lower() in ['yes','no']:
#             break
#         else:
#             option=input("Enter only yes or no:")
#     if option.lower()=='no':
#         break
# print(d)


# d={}
# while True:
#     name=input("Enter the student name:")
#     marks=input("Enter the students marks:")
#     d[name]=marks
#     print("thanks for sharing your details")
#     option=input("would you like to share another students details:[yes/no]:")
#     while option.lower() not in ['yes','no']:
#           option=input("Enter only yes or no:")
#     if option.lower()=='no':
#         break
# print(d)

# d={}
# while True:
#     name=input("Enter the student name:")
#     marks=input("Enter the students marks:")
#     d[name]=marks
#     print("thanks for sharing your details")
#     option=input("would you like to share another students details:[yes/no]:")
#     while option.lower() not in ['yes','no']:
#           option=input("Enter only yes or no:")
#     if option.lower()=='no':
#         break
# print('Name\t\tmarks')
# print('#'*20)
# for x in d:
#      print('{}\t\t{}'.format(x,d[x]))
# print('#'*20)

# d={}
# while len(d)<5:
#     name=input("Enter the student name:")
#     marks=input("Enter the students marks:")
#     d[name]=marks
#     print("thanks for sharing your details")
# print('Name\t\tmarks')
# print('#'*20)
# for x in d:
#      print('{}\t\t{}'.format(x,d[x]))
# print('#'*20)

# d={}
# i=0
# while i<=5:
#     name=input("Enter the student name:")
#     marks=input("Enter the students marks:")
#     d[name]=marks
#     print("thanks for sharing your details")
#     i=i+1
# print('Name\t\tmarks')
# print('#'*20)
# for x in d:
#      print('{}\t\t{}'.format(x,d[x]))
# print('#'*20)

# d={}
# while True:
#     name=input("Enter the student name:")
#     marks=input("Enter the students marks:")
#     d[name]=marks
#     print("thanks for sharing your details")
#     option=input("do you want another student data[ to share [yes/no]:")
#     while option.lower().strip() not in ["yes","no"]:
#         option=input(("enter only yes or no:"))
#     if option.lower().strip()=='no':
#       break
# print(d)

# d={100:'vivek',200:'omi',300:'chacha'}
# print(d.pop(300))

# d={100:'vivek',200:'omi',300:'chacha'}
# d.setdefault(400,'rohan')
# print(d)

# d1={100:'vivek',200:'omi',300:'chacha'}
# d2={400:'rohan',500:'nipu',100:'shreyash'}
# d1.update(d2)
# d2.update(d1)
# print(d1)
# print(d2)

# d1={100:'vivek',200:'omi',300:'chacha'}
# print('sum:',sum(d1.keys()))

# d1={100:'vivek',200:'omi',300:'chacha'}
# sum=0
# for v in d1:
#     sum=sum+v
# print('sum:',sum)

#####################

## wap to find number of ocurrences of each letter present in the string ##

#####################
# s=input("enter any string")
# d={}
# for v in s:
#     if v in d:
#      d[v]=d[v]+1
#     else:
#        d[v]=1
# print(d)

# s=input("enter any string")
# d={}
# for v in s:
#    d[v]=d.get(v,0)+1
# print(d)

# s=input("enter any string")
# d={}
# for ch in s:
#    d[ch]=d.get(ch,0)+1
# for k,v in d.items():
#    print('{} occurs {} times '.format(k,v))

## VOWELS ##

# s=input("enter any string")
# vowels={'a','e','i','o','u'} 
# d={}
# for ch in s:
#    if ch in vowels:
#     d[ch]=d.get(ch,0)+1
# for k,v in d.items():
#    print('{} occurs {} times '.format(k,v))

# s=input("enter any string").strip()
# print(s)
# d={}
# for x in s:
#     if x not in d:
#      d[x]=1
#     else:
#        d[x]=d[x]+1
# print(d)
 
# d={}
# while True:
#    name=input("Enter the students name:")
#    marks=input("Enter the students marks:")
#    d[name]=marks
#    print("thanks for sharing your information!!!")
#    output=input("if you want to share detail about more students please write [YES/NO]")
#    while True:
#       if output.lower().strip() in ['yes','no']:
#          break
#       else:
#        output=input("enter only YES or NO:")
#    if output.lower().strip()=='no':
#       break
# print(d)

# d={}
# while True:
#    name=input("Enter the students name:")
#    marks=input("Enter the students marks:")
#    d[name]=marks
#    print("thanks for sharing your information!!!")
#    output=input("if you want to share detail about more students please write [YES/NO]:")
#    while output.lower().strip() not in ['yes','no']:
#      output=input("Enter only YES/NO:")
#    if output.lower().strip()=='no':
#         break
# print(d)

 
# n=int(input("Enter no. of students:"))
# d={}
# for i in range(n):
#     name=input("Enter the student name:")
#     marks=input("Enter the students marks:")
#     d[name]=marks
# print("thanks for sharing your details")
# while True:
#     name =input("enter the student name to see his/her marks:")
#     if name in d:
#         print("marks of {}:{}".format(name,d[name])) #d[name]=d.get(name)
#     else:
#         print("student name not in the shared list")
#     option=input("do you want to see another students marks [yes/no]:")
#     while option.lower().strip() not in ["yes","no"]:
#         option=input(("enter only yes or no:"))
#     if option.lower().strip()=='no':
#       break
# print(d)

## DICT COMPRIHENTION ###

# d={ x:x*x for x in range(1,6)}
# print(d)


# d={
#     'cars':('v','b','m'),
#     'mobile':('z','x','c')
#     }
# print(d['cars'][2])

### SUPER MARKET PROJECT ###

supermarket={ 
              'store1':{
                         'name':'mhaske superstore',
                         'items':[
                                   {'name':'top','quantity':20},
                                   {'name':"khulkhula",'quantity':30},
                                   {'name':"phone",'quantity':40}
                ]
                 
            },
            'store2':{
                'name':'Aaradhya  Dramma Dresses',
                'items':[
                        {'name':"ganpati",'quantity':20},
                        {'name':"mahadev",'quantity':30},
                        {'name':"mukut",'quantity':40}
                ] 
                 
            }
}

# print(supermarket)
# print(supermarket['store1']['items'])
# for d in supermarket['store1']['items']:
#     print(d['name'])
# for d in supermarket['store2']['items']:
#     if d['name']=='mahadev':
#         print('the no. of mahadev costume:',d['quantity'])

"""
acess of the name of the costume and also super store so we can see the quantity available when we enter the name of the toy or costume and also give the option to chek or not to chek the quantity of the products

"""