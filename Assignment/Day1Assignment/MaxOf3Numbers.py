a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
c=int(input("Enter num3:"))
result = a if a>b and a>c else b if b>c else c
print("Maximum value:",result)