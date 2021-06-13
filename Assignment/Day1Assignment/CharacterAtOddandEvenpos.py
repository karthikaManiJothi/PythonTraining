string =input("enter string:")
str_list =list(string)

#using slice operator
list1 = [x for x in str_list[1::2]]
list2 =[x for x in str_list[0::2]]
list1.extend(list2)
print("".join(list1))

#without using slice operator
list3=[]
list4=[]
count=1
for i in str_list:
    if count%2==0:
        list3.append(i)
    else:
        list4.append(i)
    count+=1
list3.extend(list4)
print("".join(list3))