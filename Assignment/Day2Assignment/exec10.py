list1 =input("Enter the list(with ','):").split(",")
list2 =[int(x) for x in list1]
list2.sort(reverse=True)
print(list2)