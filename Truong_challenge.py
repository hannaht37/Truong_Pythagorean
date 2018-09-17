"""
Write a program that will determine if the user's input is a triangle and what type of triangle
"""
print("Hi there! Today we will be determining if the three lengths you will enter are triangles and what type of triangle it is. ")
greeting = input("What is your name? ")
print("Nice to meet you, " + greeting + ". Let's get started.")
a = float(input("First, please enter a length for leg a : "))
b = float(input("Now please enter a length for leg b : "))
c = float(input("Finally, please enter a length for leg c : "))
if(a+b<c):
    print("Oh No! It looks like the lengths you entered is not a triangle.")
else:
    if(a**2 + b**2 == c**2):
        print("Congrats! The values you entered are equal to a right triangle!")
    if(a**2 + b**2 > c**2):
        print("Yay, the lengths you entered are equal to an acute angle!")
    elif(a**2 + b**2 < c**2):
        print("The lengths you entered are equal to an obtuse angle!")  