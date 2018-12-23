# Python program practice of class and inheritance from codesdope
class Rectangle():
	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth
	def getArea(self):
		print self.length*self.breadth," is area of rectangle"
class Square(Rectangle):
	def __init__(self,side):
		self.side = side
		Rectangle.__init__(self,side,side)
	def getArea(self):
		print self.side*self.side," is area of square"
square = Square(6)
rect = Rectangle(5,2)
square.getArea()
rect.getArea()
