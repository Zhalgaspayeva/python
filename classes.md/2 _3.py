class Shape():
    x = 0
    y = 0
    cnt = 0
    def area(self):
        return self.x * self.y

    def printt(self):
        return self.cnt

    

class Square(Shape):
    def __init__(self,length):
        Shape.x = length
        Shape.y = self.x
        Shape.cnt +=1

class Rectangle(Shape):
    def __init__(self,length,width):
        Shape.x = length
        Shape.y = width
        Shape.cnt+=1


sq = Square(int(input()))
s = Shape()
print(s.area())

rc = Rectangle(int(input()),int(input()))
print(s.area())

s.area()
print(s.printt())