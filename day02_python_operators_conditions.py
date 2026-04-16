#Day 2 conditions
"""
#Program to check if a number is positive, negative, or zero.
num = float(input("Enter a num: "))
if num > 0:
    print("the number is positive")
elif num < 0:
    print("the number is negative")
else:
    print("it is a zero")

#Program to check if a year is leap year.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0):
    print("It is leap year")
else:
    print("It is not a leap year")

#Program to compute grade from marks (A/B/C/F).
Marks = int(input("Enter your marks: "))
if Marks >= 95:
    print("A grade")
elif Marks >= 75:
    print("B grade")
elif Marks >= 50:
    print("C grade")
else:
    print("F grade")

#Simple login simulation: ask for username/password; if matches hardcoded values, print “Login success”.
correct_username = "Sri25"
correct_password = "Sri@250518"
username = input("Enter your username: ")
password = input("Enter your password: ")
if correct_username == username:
    print("Logic success")
else:
    print("Incorrect password/username")
"""
