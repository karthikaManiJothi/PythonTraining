import math
class circle:
    def __init__(self,r):
        self.r=r

    def circumference(self):
         print("circumference:{:.2f}".format(2*math.pi*self.r))

    def area(self):
           print("Area :{:.2f}".format(math.pi*self.r*self.r))

    def __add__(self, other):
        return self.r+other.r

    def __ge__(self, other):
        if self.r > other.r:
            return "circle 1 is greater than circle 2"
        elif self.r==other.r:
            return "both circles are equal"
        else:
            return "circle 2 is greater than circle 1"

    """def __eq__(self, other):
        if self.r ==other.r:
            return "both circles are equal"
        else:
            return "circles are not equal" """

n=int(input("Enter radius of Circle 1:"))
m=int(input("Enter radius of Circle 1:"))

c1=circle(n)
c2=circle(m)
c1.circumference()
c2.circumference()
c1.area()
c2.area()
print("additon of 2 circle:",c1+c2)
print(c1>=c2)
