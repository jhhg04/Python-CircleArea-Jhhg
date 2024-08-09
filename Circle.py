import math

class Circle:
  # Initialize-Constructor
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    #return math.pi * (self.radius ** 2)
    return round(math.pi * (self.radius ** 2), 2)

circle = Circle(3)

print(f"The area of the circle is: {circle.area()}")