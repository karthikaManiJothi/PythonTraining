#fibonaaci value of nth number

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

num=int(input("enter a number:"))
print("Fibonacci of",num,":")
print(fibonacci(num-1))