#Module Operators

# Declare your age as integer variable
age = 25

# Declare your height as float variable
height = 12.4

# Declare a variable that store a complex number
complex_num = (9 + 2j)

# Write a script that prompts the user to enter base and 
# height of the triangle and calculate an area of this 
# triangle (area = 0.5 x b x h
base = int(input("Enter base: "))
height = int(input("Enter height: "))

area = 0.5 * base * height

print("The area of the triangle is ", area)

#Write a script that prompts the user to enter side a, 
# side b, and side c of the triangle. Calculate the 
# perimeter of the triangle (perimeter = a + b + c).

side_a = int(input("Enter side a: "))  
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))

perimeter = side_a + side_b + side_c

print("The perimeter of the triangle is ", perimeter)

# Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and 
# perimeter (perimeter = 2 x (length + width))
length = int(input("Enter length: "))
width = int(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print("The area of the rectangle is ", area)
print("The perimeter of the rectangle is ", perimeter)

# Get the radius of a circle using prompt. Calculate 
# the area (area = pi x r x r) and circumference 
# (c = 2 x pi x r) where pi = 3.14.
radius = int(input("Enter radius: "))
pi = 3.14

area = pi * radius ** 2
circumference = 2 * pi * radius

print("The area of the circle is ", area)
print("The circumference of the circle is ", circumference)

# Calculate the slope, x-intercept and y-intercept 
# of y = 2x - 2 (y = mx + c)
slope = 2
x_intercept = -2
y_intercept = 2

print("The slope is ", slope)
print("The x-intercept is ", x_intercept)
print("The y-intercept is ", y_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and 
# Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
x2 = 6
y1 = 2
y2 = 10

slope_m = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("The slope is ", slope_m)
print("The Euclidean distance is ", euclidean_distance)

# Compare the slopes in tasks 8 and 9.
print("The slope in task 8 is greater than the slope in task 9 ", slope > slope_m)
print("The slope in task 8 is less than the slope in task 9 ", slope < slope_m)
print("The slope in task 8 is equal to the slope in task 9 ", slope == slope_m)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values 
# and figure out at what x value y is going to be 0
x = int(input("Enter x: ")) 
y = x ** 2 + 6 * x + 9

print("The value of y is ", y)

# Find the length of 'python' and 'dragon' and make a 
# falsy comparison statement
pylen = len('python')
drlen = len('dragon')

print("The length of python is ", pylen)   
print("The length of dragon is ", drlen)
print("The falsy comparison statement is ", pylen != drlen)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
compare = 'on' in 'python' and 'on' in 'dragon'

print("Does the word 'on' found in both 'python' and 'dragon'? ", compare)

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
jargon = 'jargon' in 'I hope this course is not full of jargon.'

print("Is the word 'jargon' in the sentence? ", jargon)

# There is no 'on' in both dragon and python
compare = 'on' not in 'python' and 'on' not in 'dragon'

print("Does the word 'on' not found in both 'python' and 'dragon'? ", compare)

# Find the length of the text python and convert the value 
# to float and convert it to string
pylen = len('python')
pylen = float(pylen)
pylen = str(pylen)

print("The length of python is ", pylen)

# Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is not even")

# Check if the floor division of 7 by 3 is equal to the 
#  int converted value of 2.7
print("The floor division of 7 by 3 is ", 7 // 3)
print("The integer division of 7 by 3 is ", 7 / 3)
print("is Floor division and interger division is equal? ", 7//3 == 2.7)

# Check if type of '10' is equal to type of 10
print(type('10') is type(10))

# Check if int('9.8') is equal to 10
print(int('9.8') == 10)

# Write a script that prompts the user to enter hours 
# and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))

pay = hours * rate

print("Your weekly earning is ", pay)

# Write a script that prompts the user to enter number 
# of years. Calculate the number of seconds a person 
# can live. Assume a person can live hundred years
years = int(input("Enter number of years: "))

seconds = years * 31536000

print(f"You lived {seconds} seconds.")

# Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")