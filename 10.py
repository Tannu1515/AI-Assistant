#write a program to check if a number is a single digit number , 2 digit number and so on up to 5 digit
number=int(input("enter the no up to 5 digit"))
if(number<10):
    print("one digit no")
elif(number>10):
    print("2 digit no")
elif(number>100):
    print("3 digit no")
elif(number>1000):
    print(" 4 digit no")
else:
    print("5 digit no")
