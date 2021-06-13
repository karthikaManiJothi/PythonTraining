str =input("Enter string").split()
list1 =[]
for i in str:
    list1.append(i[::-1])
print(" ".join(list1))