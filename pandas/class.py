class student:
    first_name=""
    last_name=""
    roll=None
    
    def values(self,fname,lname,roll):
        self.first_name=fname
        self.last_name=lname
        self.roll=roll
        return

t=student()
t.values('Akshay','Mokalwar',101)
temp=[t]
k=student()
k.values('Hritik','Gupta',103)
temp.append(k)
z=student()
z.values('Mohit','Sharma',105)
temp.append(z)
for i in range(0,len(temp)):
    print(temp[i].first_name)
print("-"*90)
z.values('Rohit','Sharma',105)
for i in range(0,len(temp)):
    print(temp[i].first_name)
print("-"*90)
# arr=[temp,]
# print(type(arr))
# print(arr[0])
