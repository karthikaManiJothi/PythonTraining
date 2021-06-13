d=dict()

for i in range(int(input("how many students?"))):
 key,value =input("enter student name and mark:").split()
 d[key]=int(value)

for i,j in d.items():
    print(i,j)

name =input("enter name:")
print(name,"scored",d[name],"marks")
