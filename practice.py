# a=int(input("Enter a no."))
# b=int(input("Enter a no."))
# if a>b :
#     print("a is greater then b")
# else:
#     print("b is greater then a")


# a=int(input("Enter a no."))
# b=int(input("Enter a no."))
# c=int(input("Enter a no."))
# if a>b and a>c:
#     print("a is the greatest no. among all the given no.'s")
# elif b>c:
#     print("b is the greatest no. among all the given no.'s")
# else:
#     print("c is the greatest no. among all the given no.'s")


# n=int(input("Enter any three digit no."))
# units={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# tens={2:'Twenty',3:'Thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
# hundreds={1:'one hundred and',2:'two hundred and',3:'three hundred and',4:'four hundred and',5:'five hundred and',6:'six hundred and',7:'seven hundred and',8:'eight hundred and',9:'nine hundred and'}

# h=n//100
# unit=n%10
# ten=n//10

# output=hundreds[h]+" "+tens[ten]+" "+units[unit]
# print(output)

# n=(input("Enter the string "))
# print(type(n))
# l=print(n.replace('vivek','omi'))

# n=(input("Enter the string "))
# r=reversed(n)
# # print(r)
# print(''.join(r))

# def split_and_join(line):
#     r=line.split()
#     return '-'.join(r)

# if __name__ == '__main__':
#     line = input('Enter a string:')
#     result = split_and_join(line)
#     print(result)

# def swap_case(s):
#     return s.swapcase()

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)   

# def print_full_name(first, last):
#      print("Hello {} {}! you just delved into python".format(first_name,last_name))
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# v=(input("Enter the string ")).split()
# print(v)

# if __name__ == '__main__':
#     n = int(input("Enter any no.").strip())


# if n%2!=0:
#     print("Weird")
# elif n%2==0 in range(2,6):
#     print("Not Weird") 
# elif n%2==0 in range(6,21): 
#     print("Weird")
# elif n%2==0 and n>20:
#     print("Not Weird")
# else:
#     print()
# if __name__ == '__main__':
#     n = int(input().strip())


# def count_substring(string, sub_string):
#     count=0
#     count+=1
#     return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
# count = count_substring(string, sub_string)
# print(count)

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string) - len(sub_string) + 1):
#         if string[i:i+len(sub_string)] == sub_string:
#             count += 1
#     return count
# # print(count)
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
# count = count_substring(string, sub_string)
# print(count)
# print(len(string))
# print(len(sub_string))

# s=input("Enter any string:")
# l=s.split()
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i=i-1
# output=' '.join(l1)
# print(s)
# print(output)

# s=input("Enter any string:")
# count=0
# for ch in s:
#     if ch in "aeiou":
#         count+=1
# print(count)

# s = input("Enter a string: ")
# ch = input("Enter a character: ")
# print("Frequency:", s.count(ch))

# s=input("Enter any string:")
# print(s.replace('vivek','omi'))

# s=input("Enter any string:")
# word=s.split()
# print(len(word))

# s=input("Enter any string:")
# # w=s.replace(' ','')
# print(s.replace(' ',''))

# vs=input("Enter any string:")
# # s=vs.split()
# print(s[0],s[-1])

# s=input("Enter any string:")
# # v=s.split()
# ch=input(("Enter any string:"))
# if ch in s:
#     print("yes the substring exists")
# else :
#   print("no the substring exists")


# #Count digits in a string

# s=input("Enter any string:")
# count=0
# for x in s:
#    if x.isdigit():
#     count+=1
# print(count)  

# #Separate characters of a string

# s=input("Enter any string:")
# for x in s:
#     print(x)

# s=input("Enter any string:")
# o={}
# for x in s:
#     if x not in o:
#         o[x]=1
#     else:
#         o[x]=o[x]+1
# print(o)        

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
    
