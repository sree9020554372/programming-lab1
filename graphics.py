r=int(input("Enter the radius of circle:"))

l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
l1=int(input("Enter the length of cuboid:"))
b1=int(input("Enter the breadth of cuboid:"))
h1=int(input("Enter the height of cuboid:"))

r1=int(input("Enter the radius of sphere:"))
def areac(r):
    a=3.14*r*r
    print("Area of Circle is:",a)
def peric(r):
    p=2*3.14*r
    print("Perimeter of Circle is:",p)

def arear(l,b):
    a=l*b
    print("Area of Rectangle is:",a)
def perir(l,b):
    p=2*(l+b)
    print("Area of Rectangle is:",p)

def areas(r):
    a = 4*3.14*r*r
    print("Area of Sphere is:", a)
def peris(r):
    p = 6.2832*r
    print("Perimeter of Sphere is:", p)

def areacub(l,b,h):
    a = 2*((l*b) + (b*h) + (h*l))
    print("Area of Cuboid is:", a)
def pericub(l,b,h):
    p = 4*(l+b+h)
    print("Perimeter of Cuboid is:", p)
