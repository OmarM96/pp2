import math as m
n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))
a = s/2*m.tan(m.pi/n)
area = round(n*s*a/2)
print("The area of the polygon is: ", area)