#area of calculator
a=int(input("enter the choice value= "))
if(a==1):
     print("area of rectangle calulator")
     
     l=int(input("enter the value l"))
     w=int(input("enter the value w"))
     area=l*w
     print("area of rectangle calculator",area)

elif(a==2):
     print("area of square calculator")
     side=int(input("enter the value of square side"))
     area=side*side
     print("area of square",area)
elif(a==3):
     print("area of circle")
     radius=int(input("enter the value of radius"))
     area=(22/7)*radius
     print("area of circle", area)
elif(a==4):
     print("area of triangle")
     b=int(input("enter the off breath"))
     h=int(input("enter the value of height"))
     area=0.5*b/h
     print("area of triangle",area)

     