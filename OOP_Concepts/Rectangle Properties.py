class Rectangle():
    def __init__(self,width,height):
        if (width <= 0) or (height <= 0):
            raise ValueError("Lengths can not be negative")
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
    def query_points(self,x,y):
        if (0<x<self.width) and (0<y<self.height):
            return "Inside"
        if (
            (x==0 and 0<=y<=self.height) or
            (x==self.width and 0<=y<=self.height) or
            (y == 0 and 0 <= x <= self.width) or
            (y==self.height and 0<=x<=self.width)):
            return "On edge"
        return "Outside"

if __name__ == "__main__":
    try:
        width = int(input("Width:"))
        height = int(input("Height:"))
        rect = Rectangle(width, height)
    except ValueError as e:
        print("İnvalid values:",e)
    else:
        print("Area:",rect.area())
        print("Perimeter:",rect.perimeter())
        x = int(input("x:"))
        y = int(input("y:"))
        result = rect.query_points(x,y)
        print("{},{} point is in {}.".format(x,y,result))

