class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def move(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print(str(self.x) + ' ' + str(self.y))

    def dist(self):
        print(abs(self.y-self.x))

p = Point(1, 5)

p.show()
p.move(1,2)
p.show()
p.dist()
p.move(10,5)
p.dist()