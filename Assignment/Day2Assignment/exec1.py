n=int(input("Enter a number"))
if n>0:
    if n%2!=0:
        print("Weird")
    elif n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=10:
        print("Weird")
    elif n>20:
        print("Not Weird")
else:
    print("enter only positive number")