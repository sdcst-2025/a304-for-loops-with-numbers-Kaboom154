#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""

num = float(input("Enter a  number: "))
if num > 10 and int(num) == num:
    print("Your box size is too big. Boxes should be no larger than a size of 10.")
    num = float(input("Enter a number: "))
    pass
num = int(num)
for i in range (num):
    print("*" * num)
    