
# s=input("Enter any string:")
# count=0
# output=""
# for x in s:
#     if x not in output:
#         output+=x
#         count+=1
# print(output) 
# print(count)       

# if __name__ == '__main__':
#     n = int(input("Enter :"))
#     i=0
#     while i<n:
#         ch=i*i
#         i=i+1
#         print(ch)

# if __name__ == '__main__':
#    x=int(input())
#    y=int(input())
#    z=int(input())
#    n=int(input())
#    result = [
#       [i,j,k]
#       for i in range(x+1)
#       for j in range(y+1)
#       for k in range(z+1)
#    if x+y+z!=n
#     ]
# #    v=x+y+z
#    print(result)




# s='there are so many things to do in life'
# words=s.split()
# l=[]
# for word in words:
#    l.append([word,len(word)])
# print(l)

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# result = [[i, j, k] 
#           for i in range(x + 1) 
#           for j in range(y + 1) 
#           for k in range(z + 1) 
#           if i + j + k != n]

# print(result)

# x=(input("Enter any string:"))
# count=0
# for ch in x:
#     if ch in "aeiou":
#       count+=1
# print(count)

# x=int(input("enter any no."))
# print(x%10,x//10)

# for ch in range(10,0,-1):
#     print(ch)
  
# l=eval(input("enter the list:"))
# sum=0
# for ch in l:
#     sum=sum+ch
# print(sum)

# x=int(input("enter the no.:"))
# sum=0
# i=1
# while i<=x:
#     sum=sum+i
#     i=i+1
# print(sum)    

# x=int(input("enter the no.:"))
# sum=0
# i=1
# for x in range(11):
#     sum=sum+x
#     i=i+1
#     print(sum)
# if __name__ == '__main__':
#     n = int(input())
#     for x in range(n,n+1):
#      print(x,end='')
#      n = 3

# n = int(input())
# for i in range(1, n+1):
#     print(i, end="")

# s='durga'
# print('e'in s)

# s=input("enter any string:")
# i=0
# while i<len(s):
#    print(s[i],end='')
#    i=i+1 

# s=input("enter any string:")
# i=-1
# while i>=-len(s):
#    print(s[i],end='')
#    i=i-1 

# s=input("enter any string:")
# # i=0
# count=0
# for i in s:
#    if i in 'aeiou':
#       count=count+1
# print(count)


# s=input("enter any string:")
# print(len(s.replace(" ","")))
   

# s=input("enter any string:")
# print(s.lower())

# s = "banana"
# freq = {}
# for ch in s:
#     freq[ch] = freq.get(ch, 0) + 1
# print(freq)

# s=input("enter any string:")
# count=0
# for ch in s:
#     s.count(ch)==1
#     print(ch)
#     break

# s = "aabbcddee"
# for ch in s:
#     if s.count(ch) == 1:
#         print(ch)
#         break

# s=input("enter any string:")
# count=0
# for ch in s:
#     if ch in 'aeiou':
#         count=count+1
# print(count)

# s=input("enter any string:").split()
# sub=input("enter the substring:")
# print(s)
# count=0
# for ch in s:
#     if ch in sub:
#         count=count+1
# print(count)  

# s=input("enter any string:")
# sub=input("enter the substring:") 
# print(s.count(sub))   

# s=input("enter any string:")
# print(s.replace('vivek','omi'))

# s=input("enter any string:")
# sub=input("enter the substring:") 
# print(s.startswith(sub))
# print(s.endswith(sub))

# s=input("enter any string:")
# i=-1
# while i>=-len(s):
#   print(s[i],end='')
#   i=i-1

# s=input("enter any string:")
# print(s[: : -1])

# s=input("enter any string:")
# v=''.join(reversed(s))
# print(v)

# s=input("enter any string:").split()
# v=' '.join(reversed(s))
# print(v)

# s=input("enter any string:")
# i=len(s)-1
# output=''
# while i>=0:
#     output=output+s[i]
#     i=i-1
# print(output)  

# s=input("enter any string:").split()
# l1=[]
# i=len(s)-1
# while i>=0:
#     l1.append(s[i])
#     i=i-1
# v=' '.join(l1)
# print(v)

# s=input("enter any string:")
# l=s.split()
# # print(l)
# l1=[]
# for x in l:
#     l1.append(x[::-1])
# # print(l1)
# print(s)
# print(' '.join(l1))

# s=input("enter any string:")
# l=s.split()
# l1=[]
# for x in l:
#     l1.append(''.join(reversed(x)))
# print(' '.join(l1))
"""

'''input=one two three four 
  output=one owt three ruof'''

'''s=input("enter any string:")
l=s.split()
v=l[1::2]
# print(v)
# print(l)
l1=[]
for x in v:
    l1.append(x[::-1])
# print(l1)
print(s)
print(' '.join(l1))'''

"""
# s1='vivek'
# s2='ayush'
# output=''
# i=0
# j=0
# while i<len(s1) or j<len(s2):
#     output=output+s1[i]
#     output=output+s2[j]
#     i=i+1
#     j=j+1
# print(output)

# s1='vivek'
# s2='ayush'
# output=''
# i=0
# j=0
# for x in s1 and s2:
#     output=output+s1[i]
#     # for v in s2:
#     output=output+s2[j]
#     i=i+1
#     j=j+1
# print(output)    

# s1='vivek'
# s2='ayush'
# output=''
# i,j=0,0
# while i<len(s1) or j<len(s2):
#     output=output+s1[i]+s2[j]
#     i=i+1
#     j=j+1
# print(output)  


# s1='vivekmhaske'
# s2='ayush'
# output=''
# i,j=0,0
# while i<len(s1) or j<len(s2):
#     if i<len(s1):
#       output=output+s1[i]
#     i=i+1
#     if j<len(s2):
#       output=output+s2[j]
#     j=j+1
# print(output)  

# s='B3K8F7D9A3'
# s1=''
# s2=''
# for x in s:
#     if x.isalpha:
#         s1=s1+x
#     else:
#         s2=s2+x
# output=''
# for x in sorted(s1):
#     output=output+x
# for x in sorted(s2):
#     output=output+x
# print(output)    

# s='B3K8F7D9A3'
# s1=s2=''
# for x in s:
#     if x.isalpha:
#         s1=s1+x
#     else:
#         s2=s2+x
# print(''.join(sorted(s1)+sorted(s2)))


# s='a2b3c4'
# s1=''
# for x in s:
#     if x.isalpha():
#         ch=x
#     else:
#         s1=s1+ch*int(x)
# print(s1)

# s=input("enter any string:")
# output=''
# for x in s:
#     if x.isalpha():
#         ch=x
#     else:
#         output=output+ch*int(x)
# print(output)

# s='a2b3c4'
# output=''
# for x in s:
#     if x.isalpha():
#         ch=x
#     else:
#         output=output+ch*int(x)
# print(output)        

# s=input("enter any string:")
# output=''
# num=''
# i=0
# while i < len(s):
#     if s[i].isalpha():
#        ch=s[i]
#     else:
#         num=num+s[i]
#         if i==len(s)-1:
#           output=output+ch*int(num)
#         if i+1<len(s) and s[i+1].isalpha():
#            output=output+ch*int(num)
#            num=''
#     i=i+1       
# print(output)

# s='B3K8F7D9A3'
# s1=s2=''
# for x in s:
#     if x.isalpha:
#         s1=s1+x
#     else:
#         s2=s2+x
# print(''.join(sorted(s1)+sorted(s2)))

# s='B3K8F7D9A3'
# s1=s2=''
# i=0
# while i< len(s):
#     if s[i].isalpha():
#         s1=s1+s[i]
#     else:
#         s2=s2+s[i]
#     i=i+1    
# print(''.join(sorted(s1)+sorted(s2)))

# s='a2b3c4'
# output=''
# for x in s:
#     if x.isalpha():
#         ch=x
#     else:
#         output=output+ch*int(x)
# print(output)   

# s='a2b3c4'
# output=''
# i=0
# while i< len(s):
#     if s[i].isalpha():
#         ch=s[i]
#     else:
#         output=output+ch*int(s[i])
#     i=i+1
# print(output)

# s=input("enter any string:")
# output=''
# num=''
# i=0
# while i < len(s):
#     if s[i].isalpha():
#        ch=s[i]
#     else:
#         num=num+s[i]
#         if i==len(s)-1:
#           output=output+ch*int(num)
#         if i+1<len(s) and s[i+1].isalpha():
#            output=output+ch*int(num)
#            num=''
#     i=i+1       
# print(output)
    
# s='a20b30'
# output=''
# num=''
# for i in range(len(s)):
#     if s[i].isalpha():
#         ch=s[i]
#     else:
#         num=num+s[i]
#         if i==len(s)-1:
#             output=output+ch*int(num)
#         if i+1<len(s) and s[i+1].isalpha():
#             output=output+ch*int(num)
#             num=''
# print(output)

# s='a4k3b2'
# s1=''
# output=''
# for x in s:
#     if x.isalpha():
#         ch=x
#     else:
#         newch=chr(ord(ch)+int(x))
#         output=output+ch+newch
# print(output)


# s='a4k3b2'
# output=''
# for x in s:
#     if x.isalpha():
#         ch=x
#         output=output+ch
#     else:
#         newch=chr(ord(ch)+int(x))
#         output=output+newch
# print(output)

# s='a4k3b2'
# output=''
# i=0
# while i< len(s):
#     if s[i].isalpha():
#         ch=s[i]
#         output=output+ch
#     else:
#         newch=chr(ord(ch)+int(s[i]))
#         output=output+newch
#     i=i+1
# print(output)

# s=input("enter any string:")
# l=[]
# for x in s:
#     if x not in l:
#         l.append(x)
# print(''.join(sorted(l)))

# s=input("enter any string:")
# d={}
# for x in s:
#     if x not in d:
#         d[x]=1
#     else:
#         d[x]=d[x]+1
# print(d)
# for k,v in d.items():
#   print("{} ocurrs {} times".format(k,v))
