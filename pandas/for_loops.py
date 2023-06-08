
# if print(12):
#     print(True)
# else:
#     print(False)

# for i in range(0,10):
#     print(i)
# for i in range(0,10,2):
#     print(i)
# for i in range(10,0,-2):
#     print(i)

# ----------------range
from re import A


age=45
# if age>18= and age <=60:
# if 18<=age<=60:
if age in range(18,61):
    print("Go for work")
else:
    print("Enjoy free time")

s="545,.45m.465,4m.54m.4,m5.kl44m.56.4m564."
# seperators=""
# for char in s:
#     if(not char.isnumeric()):
#         seperators=seperators+char
#         # print(char)
# arr="".join(char if  char.isnumeric() else " " for char in s).split()
# print(arr)

# for i in range(0,len(arr)):
#     arr[i]=int(arr[i])
# print(arr)

# # print Capital Letter from the string
# quote="""
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
# s=""
# for c in quote:
#     if(c.isupper()):
#         s=s+c
# print()


# print([i for i in range(10) if(i&1==0)])
# print([i for i in range(10) if(i&1==1)])

s="Hello World!!"
print([i for i in s.split("")])


a=5
b=10
a,b=b,a 
print("a = ",a,"and b = ",b)
# print("b = ",b)