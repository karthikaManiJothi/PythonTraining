#random 6 digit password

import random as r
import string

list1 = list(string.ascii_letters)
num_list =[]
alpha_list=[]
final_list=[]
for i in range(3):
        otp_n=r.randint(1,9)
        num_list.append(otp_n)

for i in range(3):
        alpha_list.append(r.choice(list1))


for i in range(len(alpha_list)):

          final_list.append(alpha_list[i])
          final_list.append(num_list[i])

final_list=list(map(str,final_list))
print("Password:","".join(final_list))

            




