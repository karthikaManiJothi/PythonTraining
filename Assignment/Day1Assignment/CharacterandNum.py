str=input("enter :")
str_list =list(str)

list1= [x for x in str_list[0::2]]
list2 =[int(x) for x in str_list[1::2]]
list3=[]
print(list1)
print(list2)
for i in range(len(list1)):
    list3.append(list1[i]*list2[i])
print("".join(list3))
