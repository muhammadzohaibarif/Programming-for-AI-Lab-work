#class rectangle

class Rectangle:
     def __init__(self, width, height):
        self.width = width
        self.height = height

     def area(self):
      return self.height*self.width

     def perimeter(self):
      return 2*(self.height+self.width)

     def is__squareof(self):
      return self.width == self.height
    
    

R1 = Rectangle (4,6)
R2 = Rectangle (5,5)
print(R1 , R1.area(), R1.perimeter(), R1.is__squareof())
print (R2, R2.area(), R2.perimeter(), R2.is__squareof())
