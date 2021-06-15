# reduce function -sum
from functools import *

list_num =list(map(int,input("enter list of numbers:").split()))
result = reduce(lambda x ,y : x+y ,list_num)
print("Sum:",result)