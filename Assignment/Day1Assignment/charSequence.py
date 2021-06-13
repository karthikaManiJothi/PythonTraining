str=input("enter :")
str_list =list(str)

list1= [x for x in str_list[0::2]]
list2 =[int(x) for x in str_list[1::2]]
list3=[]
list4=[]
list5=[]

for i in list1:
    list3.append(ord(i))   # ord - converting alphabet into ascii value

result =list(map(lambda x ,y :x+y,list2,list3))

for i in result:
 list4.append(chr(i))    #chr - converting asciivalue into alphabet char

for i in range(len(list1)):
    list5.append(list1[i])
    list5.append(list4[i])

print("".join(list5))