#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

num = float(input("Enter a number: "))
strNum = "1"
total = 0

if num >= 10 or num.is_integer() == False: 
    print("Invalid number. Ensure your input is an integer that is smaller than 10")
    num = float(input("Enter a number: "))

num = int(num)

for i in range (1,num+1):
    abcd = int(strNum * i)
    total += abcd
print(f"The sum of the series is {total}")