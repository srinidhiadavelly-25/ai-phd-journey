#Question 1 – Target universities list
universities = ["UCL", "Bristol", "Birmingham", "Nephier", "Oxford"]
for i in universities:
    print("My target universities are: ", i)

#Question 2 – Numbers: max, min, average
numbers = []
total = 0
for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)
    total = total+n
Average = total/len(n)
print("Max: ", max(numbers))
print("Min: ", min(numbers))
print("Average: ", Average)

#Question 3 – Reverse a list without using reverse()
fruits = ["apple", "kiwi", "cherry", "guava"]
reversed_list = fruits[::-1]
print(reversed_list)

#Question 4 – Tuple with basic info
my_info = ("Srinidhi", 24, "Data Science" )
print(my_info[0])
print(my_info[1])
print(my_info[2])