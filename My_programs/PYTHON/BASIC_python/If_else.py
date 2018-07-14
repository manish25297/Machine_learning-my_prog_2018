
" if else, """

a=int(raw_input("enter the first side of the triangle"))
b=int(raw_input("enter the second side of the triangle"))
c=int(raw_input("enter the third side of the triangle"))



if a==b and b==c:
    print" equilateral triangle"
elif a!=b and b!=c:
    print " scalene triangle"
else :
    print" isoceles triangle"



