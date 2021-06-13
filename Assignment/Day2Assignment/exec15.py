list1 =[int(i) for i in input("Enter list of numbers").split()]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print("Duplicate elimination without set:",list2)

list3 =list(set(list1))
print("Duplicate elimination using set:",list3)
