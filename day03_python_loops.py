# Day 03 - loops practice
# #Print numbers 1 to 50
for x in range(1, 51):
    print(x)

#Sum of numbers 1 to N
n = int(input("Enter a number:"))
total = 0
for i in range(1, n+1):
    total = total + i
print("sum of the numbers:", total)

#Multiplication table
n = int(input("Enter a number: "))
Table = 0
for i in range(1, 11):
    print(n, "*", i, "=", n * i)

#Guess the number (while loop)
secret_number = 18
guess = int(input("Enter your number:"))
while guess != secret_number:
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    guess = int(input("Try again: "))
print("Yeah! you guessed right")


