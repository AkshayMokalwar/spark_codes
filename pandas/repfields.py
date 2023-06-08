# age=21
# print("My age is "+str(age)+" years")
# print("My age is {0} years".format(age))
# # print("My age is %s years" age)
# print("There are {0} days in {1} ,{2},{3},{4},{5},{6} and {7}".format(31,"Jan","Mar","May","Jul","Aug","Oct","Dec"))

# print()

for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cube is {2:4}".format(i,i**2,i**3))

print("\nLeft aligned")
for i in range(1,13):
    print("No. {0:<2} squared is {1:<3} and cube is {2:<4}".format(i,i**2,i**3))