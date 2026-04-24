#Day 5 – Practice Questions

#Question 1 – Student Dictionary
student_dict = {
    "name" : "A.Srinidhi",
    "branch" : "Data Science",
    "CGPA" : "3.8",
    "target country" : "UK"
}
for x, y in student_dict.items():
   print(x, ":", y)
# this is to print the whole dict if we need only keys then we write(for x in student_dict.values() and same for key,value and items)
# for x in student_dict.values():
   # print(x)

#Question 2 – Subject Marks
subject_marks = { }
for x in range(3):
    subject = input("Enter subjects names: ")
    score = int(input("Enter your marks: "))
    # adding data to dictionary eg: {subject:score}
    subject_marks[subject] = score
total = sum(subject_marks.values())
average = total/len(subject_marks)
print("Total: ", total)
print("Average: ", average)

#Question 3 – Phonebook
phone_book = {}
n = int(input("How many contacts do you need: "))
for x in range(n):
    name = input("Enter the contact name: ")
    number = int(input("Enter the number: "))
    phone_book[name] = number
search = input("Enter the name to search: ")
if search in phone_book:
#Dictionary is a fast lookup system: give key → get value
    print("Number: ", phone_book[search])
else:
    print("Contact not found")

#Question 4 - Set Operations
set1 = {"Python", "ML", "SQL"}
set2 = {"ML", "DL", "Python"}
set3 = set1.union(set2)
set4 = set1.intersection(set2)
print(set3, set4)