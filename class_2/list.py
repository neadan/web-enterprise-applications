# Initializing the list of car accessories
# car_accessories is an object of type list
# list -- 3rd letter = s, so square brackets
car_accessories = ["car charger", "speaker", "window", "dashboard", "seats"]

# Get the length
print(len(car_accessories))

# Print 'window'
print(car_accessories[2])

# Starting from the end
print(car_accessories[-1])
print(car_accessories[-2])

mixed_list = ["string_1", 5, 5.5, True]
print(mixed_list)

# Get class of car_accessories
print(type(car_accessories))

# Slicing
# listname[start_index : end_index]
car_accessories_short = car_accessories[1:4]
print(car_accessories)
print(car_accessories_short)

# Add items to the list
car_accessories.append("wheels")
print(car_accessories)

# Sorting
car_accessories.sort()
print(car_accessories)
car_accessories.sort(reverse=True)
print(car_accessories)

# Iteration
grades = [50, 60, 40, 34]
print(grades)
for grade in grades:
    print(grade)

for i in range(0, len(grades)):
    print(grades[i])

for i in range(0, len(grades)):
    grades[i] = grades[i] + 5

print(grades)




