
# time complexity o(n^2)

#l=[-2,1,-3,4,-1,2,1,-5,4]

l=[5,2,3,4,5]
def max_sub_array(l):
    max_s=l[0]
    curr_max=l[0]
    sub_list=[]
    for j in range(0,len(l)):
        for i in range(0,len(l)):
            
            if(len(l)==(i+1) and j==0):
                print("Full array")
                continue;
            else:
                print(l[0+j:i+1])
                curr_max=sum(l[0+j:i+1])
            print(curr_max)
            if(curr_max>max_s):
                max_s=curr_max
                sub_list=l[0+j:i+1]
                
                
    print(max_s)
    print(sub_list)
    return sub_list
print(max_sub_array(l))


