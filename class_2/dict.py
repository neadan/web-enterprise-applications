
# dict (third letter is c)
grades = {"Joe": 80,
          "Sarah": 75,
          "Mark": 99}
print(grades)

# get length of dict
print(len(grades))

# get value for a key
print(grades['Sarah'])

# add 'Mike' to our dictionary, with a grade of 50
grades['Mike'] = 50
print(grades)

# update in the same way as above
grades['Sarah'] = 80
print(grades)

# tuples (third letter is p)
my_tuple = (1, 2, 3)

# values can be anything
grocery_items = {"Oscar": ["apples", "bananas", "cherries"],
                 "Daniel": ['Peppers', 'Steak'],
                 "Arezoo": ['Bananas', 'Fries']}

print(grocery_items)

# get class of grocery_items
print(type(grocery_items))
