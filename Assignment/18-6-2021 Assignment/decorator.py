def validnumber(func):
         def inner(n,str):
             if n<0:
                 print("Please provide a positive number")
             else:
                 return func(n,str)
         return inner

@validnumber
def display(n,str):
    for i in range(n):
        print(str)


str =input("What do you want to print?")
n=int(input("How many times do you want to print the statement?"))
display(n,str)