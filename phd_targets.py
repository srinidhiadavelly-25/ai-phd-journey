#phd target ares
research_areas = ["AI","ML", "DS", "CS"]
for area in research_areas:
    print(area)
n = int(input("How many research areas you want to add: "))
for i in range(n):
    new_area =  input("Enter research area: ")
    research_areas.append(new_area)
print("Final list of research areas: ")
for area in research_areas:
    print(area)