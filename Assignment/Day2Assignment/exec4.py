n=input("Enter Scores:")
l=list(n.split())
l.sort(reverse=True)
max=l[0]
for i in l:
 if max> i:
     print("Runner-up score:",i)
     break
else:
    print("no runner-up")