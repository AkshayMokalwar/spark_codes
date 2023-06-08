# # def s(a,b):
# #     return a+b
# # print(s())


# # def s(a=0,b=0):
# #     return a+b
# # print(s())

# # li=['a','1','b','c','2','4','5']

# # li2=[ int(i)+10 if i.isnumeric() else 5 for i in li ]
# # print(li)
# # print(sum(li2)//len(li2))

# i="""JAN,NY,3
# JAN,PA,1
# JAN,NJ,2
# JAN,CT,4
# FEB,PA,1
# FEB,NJ,1
# FEB,NY,2
# FEB,VT,1
# MAR,NJ,2
# MAR,NY,1
# MAR,VT,2
# MAR,PA,3
# """
# rdd=[k.split(',') for k in i.split('\n')]


# print(rdd)

# while ((i in rdd ) and (j in rdd)):
#     print(i)
#     print(j)

# print(2&1==0)
# print([i for i in range(21) if (i&1==1)])
def fucn(k):
    print("k")
    return "AS"
print(fucn("k"))
