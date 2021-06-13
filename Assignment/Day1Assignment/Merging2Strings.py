str1 =input("string1:")
str2 =input("string2:")

str1_list =list(str1)
str2_list=list(str2)
list1=[]
if len(str1_list)==len(str2_list):
  for i in range(len(str1_list)):
    list1.append(str1_list[i])
    list1.append(str2_list[i])
else:
    print("length of 2 strings need to be equal!!")

print("".join(list1))