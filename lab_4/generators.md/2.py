class Squares():
    def __init__(self,end):
        self.current = 2
        self.end_point = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end_point:
            raise StopIteration()
        self.current += 1 + (self.current % 2 == 0)
        return (self.current)
n = int(input())
print(*Squares(n), sep=', ')

# print(*Squares(n), sep = ', ')