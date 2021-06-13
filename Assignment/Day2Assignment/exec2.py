n=int(input("Enter a number:"))
if n>0 and n<=20:
    for i in range(0,n):
        print(i*i)
else:
    print("Please! enter valid input")