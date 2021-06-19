class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

n=int(input("length:"))
m=int(input("breadth:"))
r =rectangle(n,m)
print("area of a triangle:",r.area())