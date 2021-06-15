# random 6 digit OTP

import random as r
def otp():
    for i in range(6):
        otp=r.randint(1,9)
        print (otp,end="")
print("Your One Time Password : ")
otp()
