n =input().split("]")

list =str(n).split("[")

list3 =[]
for i in list:
 if i!="" and i!="'":
    list3.append(i)

for i in list3:
    for j in i:
       if j!="," and j!= "," and j!="'" and j!="]":
        print(j,end=" ")
    print()