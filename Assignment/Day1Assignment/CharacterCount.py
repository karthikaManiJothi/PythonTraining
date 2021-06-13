str =input("enter string")
list1=list(str)
set1 =set(list1)
for i in set1:
    print(i,"--",list1.count(i))