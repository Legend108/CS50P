students = []

with open("file.csv") as line:
    for row in line:
        name, house = row.rstrip().split(",")
        student = {"name": name, "house": house}
        # Make a list with dicts to sort later using keys
        students.append(student)
        # append the dict

# Function that takes the student object/dict and just returns the name key from it
# We can change it to house too
def get_name(student):
    return student["name"]
# the key parameter takes this function above and provides the students array with a particular dictionary due to the for statement
# it then uses the function and provides the particular dictionary as the argument
# sorts based on those names and returns back the arranged array with dictionaries, something like that
for student in sorted(students, key=get_name, reverse=True):
    print(f"Hello {student['name']} of house {student['house']}")

"""
or we can use this
for student in sorted(students, key=lambda student: student["name"]):
    print(f"Hello {student['name']} of house {student['house']}")
"""
# Reduces the need for defining another function get_name, lambda is a function which we only need once
# student is the argument passed into it and then we use student["name"] to provide the sorted function with a list of strings to sort
# It then sorts those strings and then assigns the dictionaries positions based on the order of strings