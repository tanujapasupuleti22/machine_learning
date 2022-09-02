# creating an empty dictionary called dog
dog = {}
# Adding name, color, breed, legs, age to the dog dictionary
dog["name"] = "cookie"
dog["color"] = "mustard"
dog["breed"] = "labrador"
dog["legs"] = 4
dog["age"] = 1
print("Dog: " + str(dog)[1:-1])

# creating a student dictionary with first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
student = {
    "first_name": "tanuja",
    "last_name": "pasupuleti",
    "gender": "female",
    "age": "10",
    "marital_status": "single",
    "skills": ["java"],
    "country": "usa",
    "city": "kansas",
    "address": "white house"
         }
print("Student: " + str(student)[1:-1])

# using len() function, getting the length of the student dictionary.
print("Length of student: " + str(len(student)))

# using type() function to check if the skills data type is a list
print("Type of skills: " + str(type(student["skills"])))

# using append() function to modify the skills values by adding two new skills
print("Skills: " + str(student["skills"])[1:-1])
student["skills"].append("hadoop")
student["skills"].append("python")
print("New Skills: " + str(student["skills"])[1:-1])

# using keys() function to get the dictionary keys as a list
print("Student Keys: " + str(student.keys())[1:-1])

# using values() function to get the dictionary values as a list
print("Student Values: " + str(student.values())[1:-1])
