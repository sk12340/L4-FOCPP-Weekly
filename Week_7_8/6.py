class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

r1 = Rectangle(5, 3)
r2 = Rectangle(7, 2)

print("Rectangle 1:")
print(f"Area: {r1.area()}, Perimeter: {r1.perimeter()}")
print("Rectangle 2:")
print(f"Area: {r2.area()}, Perimeter: {r2.perimeter()}")