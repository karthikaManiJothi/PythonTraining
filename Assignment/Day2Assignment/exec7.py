str=input("Enter the string:")
index,ch=input("enter the index and character:").split()
index =int(index)
li =list(str)
li[index]=ch
print("".join(li))