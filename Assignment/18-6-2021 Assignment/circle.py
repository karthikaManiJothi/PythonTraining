class circle:
    def __init__(self,radius):
        self.radius =radius

    def __eq__(self, other):
        if self.radius==other.radius:
            return  True
        else:
            return False

n =int(input("enter radius for circle-1:"))
m=int(input("enter radius for circle-2:"))

obj1 =circle(n)
obj2 =circle(m)
print(obj1==obj2)

