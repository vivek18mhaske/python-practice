# s={10,'vivek',30,10}
# print(s)

# l=[10,12,13,45,3,5,324,5]
# s=set(range(20))
# print(s)

# l=[10,12,13,45,3,5,324,5]
# s=set(l)
# print(s)

# d={100:'vivek',200:'omi'}
# s=set(d)
# print(s) ## in dict only keys are printed

# s=set()
# s.update(range(1,6),range(6,11),range(11,21))
# print(s)


# s={10,30,20,23,20,40,59,40,40,30,39,49}
# while len(s)!=0:
#     n=s.pop()
#     print(n)

# s={10,20,30}
# s.remove(20)
# print(s)

# s={10,20,30}
# if 40 in s:
#     s.remove(40)
# print(s)

# s={10,20,30}
# s.discard(40)
# print(s)

# s={10,20,30}
# y={10,20,30,40,50,60,70}
# print(s.union(y))
# print(s|y)

# s={10,20,30}
# y={10,20,30,40,50,60,70}
# print(s.intersection(y))
# print(s&y)

# s={10,20,30}
# y={10,20,30,40,50,60,70}
# print(y.difference(s))
# print(y-s)

# s={10,20,30,100}
# y={10,20,30,40,50,60,70}
# print(s.symmetric_difference(y))
# print(s^y)

# y={10,20,30,40,50,60,70}
# print(50 in y)

# s={x*x for x in range(1,6)}
# print(s)

# s={10,20,30}
# o={20,30,10}
# print(s is o)
# print(s==o)
# print(s in o)

# f=input("enter any string:")
# s=set(f)
# v={'a','e','i','o','u'}
# print(sorted(s.intersection(v)))

# # f=input("enter any string:")
# s=set(f)
# v={'a','e','i','o','u'}
# r=sorted(s.intersection(v))
# k=set(r)
# print(k)