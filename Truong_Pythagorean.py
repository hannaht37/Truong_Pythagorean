"""
Write a program that will compute the hypotenuse of a right triangle
"""

name = input("Hello! Please Enter Your Name Here: ")
print("Hi " + name + "! It is nice to meet you. Today I will find the hypotenuse of a right triangle you will create.")
a = int(input("Let's get started. Please enter a length for our right triangle, leg a : "))
b = int(input("Now please enter a length for leg b : "))
print("The hypotenuse of a right triangle with the leg length, " + str(a) + ", and another leg length, " + str(b) + ", is equal to " + str(float(a**2 + b**2)**(1/2)) + ".") 