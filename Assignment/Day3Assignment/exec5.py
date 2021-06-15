# finding even numbers from list using filter
# both using lambda and normal function
def even(n):
    if n%2==0:
        return True
    else:
        return False

list_num =list(map(int,input("enter list of numbers:").split()))

even_list =list(filter(lambda x :x%2==0,list_num))  # lambda function
print("filter using lambda fun:",even_list)

even_list2 =list(filter(even,list_num))
print("filter using normal fun:",even_list2)