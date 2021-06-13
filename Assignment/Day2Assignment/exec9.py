str=input("Enter the string")
li=list(str)
alnum,alpha =False,False
digit,upper,lower =False,False,False
for i in li:
 if i.isalnum():
    alnum=True
 if i.isalpha():
    alpha=True
 if i.isdigit():
     digit=True
 if i.isupper():
     upper =True
 if i.islower():
     lower =True

print("\n",alnum,"\n",alpha,"\n",digit,"\n",upper,"\n",lower)
