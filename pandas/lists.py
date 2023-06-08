# li=["Akshay","Hritik","Mohit","Harish",5]
# for i in li :
#     print(i)

# nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# nums2[::2] = [1,1,1,1,1]
# print(nums2)

# input()

s="a1b2c3d4"
a=[int(i) for i in s if i.isnumeric()]
print(a)

a=10
# print(1&a)

# if(i%2==0):
if(1&a==0):
    print("even")
else:
    print("odd")


a,*b,c=[1,2,3,4,5]
print(a)
print(b)
print(c)