import math
s_area = lambda a : a**2
r_area = lambda len, ht : len*ht
t_area= lambda b,h:1/2  *b*h

print("area of square (10) is:", s_area(10))
print("Area of Rectangle (30,20) is:", r_area(30,20))
print("area of triangle (8,4) is:", t_area(8,4))