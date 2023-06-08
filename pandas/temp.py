
test_li=["a",1,"b",2,"c",3]
test_key=["name","id"]
arr_name=[ i for i in test_li if not str(i).isnumeric()]
arr_id=[ int(i) for i in test_li if str(i).isnumeric()]
# print(arr_name)
dic={}
li_dic=[]
for i in range(0,len(arr_name)):
   dic["name"]=arr_name[i]
   dic["id"]=arr_id[i]
   li_dic.append(dic)
   dic={}
print(li_dic)