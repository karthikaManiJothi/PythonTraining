str =input("enter string :")
string_list =list(str)
vowels_list =['a','e','i','o','u']
for i in range(len(vowels_list)):
        print(vowels_list[i],"---",string_list.count(vowels_list[i]))
