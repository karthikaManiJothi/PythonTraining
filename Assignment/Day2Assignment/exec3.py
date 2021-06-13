y = int(input("Enter a  year:"));
if y>=1900:
    if y%4 ==0:
        print("True")
    elif y%400==0:
        print("True")
    else:
      print("False")
else:
    print("enter a year more than 1900")