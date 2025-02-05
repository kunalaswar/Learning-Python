
#^------------------------------------------------------------------------------------------------------
# dict1={}
# def find_max_length_word(list1):
#     dict1 = {i:len(i) for i in list1}
#     max = 0
#     # print(dict1)
#     for i in dict1:
#         # print(dict1[i])
#         if dict1[i]>max:
#             max=dict1[i]
#             idx=i
            
#     return idx,max

# list1 = [input("Enter names :") for i in range(1,5)]
# word,l=find_max_length_word(list1)
# print(word,l)

#^--------------------------------------------------------------------------------------------------
# lst=[1,2,33,33,33,33,33,33,5,6,7,1,4,6]

# for val in lst:
#     if val==33:
#         continue
#     lst.append(val)
# print(lst)
# i=0
# while(i<=len(lst)-1):
#     # print(lst[i])
#     if lst[i]<33:
#         lst.append(lst[i])
#     i=i+1




#^--------------------------------------------------------------------------------------------------
# l1=[1,2,10,10,10,10,5,10,10,10,10,3,4,4]
# # d1={ val:l1.count(val) for val in l1  }
# # print(d1)
# d1={}
# for val in l1:
#     d1[val]=l1.count(val)
# print(d1)    


#^------------------------------------------------------------------------------------------------------

# lst=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# l1 = [0,1,2,3,4,]
# l1 = []
# for i in range(len(lst)):
#     if len(l1)==0:
#         l1.append(lst[i])
#     elif(l1[-1]==lst[i]):pass    
#     else:
#         l1.append(lst[i])
# print(l1)    

#!Fibonacci series
#^---------------------------------------------------------------------------------------------------
# n=int(input('Enter a number for upto you want:'))
# a=0
# b=1
# for val in range(1,n+1):
#     c=a+b
#     a=b
#     b=c
#     print(c)

#^---------------------------------------------------------------------------------------------------
