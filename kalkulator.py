import math
figuresnumber=float(input())
figureslist = []
class Round:
 sum1=0
 def __init__(self,radius):
  self.radius=radius
 def roundfield(self):
  field1=round(math.pi*self.radius**2,2)
  self.sum1=self.sum1+field1
class Rectangle:
 sum2=0
 def __init__(self,length,width):
  self.length=length
  self.width=width
 def rectanglefield(self):
  field2=round(self.length*self.width,2)
  self.sum2=self.sum2+field2
class Triangle:
 sum3=0
 def __init__(self,side1,side2,side3):
  self.side1=side1
  self.side2=side2
  self.side3=side3
 def trianglefield(self):
  p=(self.side1+self.side2+self.side3)/2
  field3=round(math.sqrt((p*(p-self.side1)*(p-self.side2)*(p-self.side3))),2)
  self.sum3=self.sum3+field3
x=0
y=0
z=0
for i in range(int(figuresnumber)):
 figure = input().split()
 if len(figure)is 1:
  value1=Round(float(figure[0]))
  value1.roundfield()
  x=round(x+value1.sum1,2)
 elif len(figure)is 2:
  value2=Rectangle(float(figure[0]),float(figure[1]))
  value2.rectanglefield()
  y=round(y+value2.sum2,2)
 elif len(figure) is 3:
  value3=Triangle(float(figure[0]),float(figure[1]),float(figure[2]))
  value3.trianglefield()
  z=round(z+value3.sum3,2)
sum=round((x+y+z),2)
print(sum)