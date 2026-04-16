#with list
hours_list = []
days = int(input("Enter how many days you  study: "))
for i in range(days):
    hours = int(input("Enter how many hours did you study: "))
    hours_list.append(hours)
total = sum(hours_list)
average = total/days
print("Average= ", average)
print("Total= ", total)

#without list
days = int(input("How many days did you study? "))
total = 0
for i in range(days):
    hours = float(input("Enter study hours: "))
    total = total + hours
average = total / days
print("Total:", total)
print("Average:", average)