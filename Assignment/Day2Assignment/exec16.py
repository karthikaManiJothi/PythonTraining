d=dict()

for i in range(int(input("how many inputs ?"))):
 key,value =input("enter key and value:").split()
 d[key]=int(value)

sum=0
for value in d.values():
    sum+=value

print("sum of values:",sum)