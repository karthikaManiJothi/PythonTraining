# print all possible valid words from dict

d={'a':"apple",'c':"car",'e':"elephant",'F':"Football",'g':"girls",'J':"jump",'k':"karthika",'p':"python"}

char_list=['a','b','c','E','F','g','p']

print("Valid words:")
for i in char_list:
    if i in d.keys():
        print(d[i])