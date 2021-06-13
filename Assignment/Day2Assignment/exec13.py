str =input("Enter a word:")
list1 =list(str)
list2 =[x for x in list1 if x in ['a','e','i','o','u'] ]
s =set(list2)
for i in s:
    print(i,end=" ")