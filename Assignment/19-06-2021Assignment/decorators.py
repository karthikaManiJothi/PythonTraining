# Printing  mobile numbers on separate lines in the required format

def validphnnumber(func):
    new_list = []
    def inner(num_list):
        edit_list=[]
        for i in num_list:
            if len(i)!=10:
                edit_list.append(i[-10:])
            else:
                edit_list.append(i)

        for i in edit_list:
                num='+91 '+i
                new_list.append(num)
        # returning sorted list to the display function
        return func(sorted(new_list))
    return inner


@validphnnumber
def display(num_list):
    print("Number list:")
    for i in num_list:
        print(i[:4],i[4:9],i[9:])


n = int(input("No of phone numbers:"))
num_list=[]
for i in range(n):
    num_list.append(input("phn-no:"))

display(num_list)