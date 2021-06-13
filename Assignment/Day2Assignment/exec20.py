n=int(input("enter no of weights:"))
weight_list =[]
for i in range(n):
    weight_list.append(float(input("weight:")))

dis_weight_list =list(set(weight_list))
avg =sum(dis_weight_list)/len(dis_weight_list)
print(weight_list)
print(avg)