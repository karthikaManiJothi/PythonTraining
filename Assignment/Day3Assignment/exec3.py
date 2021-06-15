# Lambda Function to find biggest of 3 given values

s = lambda a, b,c: a if a > b and a>c else b if b>c else c

a =int(input("enter num1:"))
b =int(input("enter num2:"))
c =int(input("enter num3:"))
print("Biggest of 3 numbers:",s(a,b,c))