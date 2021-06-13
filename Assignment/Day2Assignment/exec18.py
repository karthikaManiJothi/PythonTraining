string =input("enter string:")
string_list=list(string)
char_list =list(set(string_list))
char_list.sort()
for i in range(len(char_list)):
    print(char_list[i],"--count :",string_list.count(char_list[i]))