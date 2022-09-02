# getting all student weights as input string using input()
print("Input all student weights(lbs) as string:")
student_weights = str(input())

# getting the indiviual weights of the students by using split() on an empty string
weights_lbs = student_weights.split(" ")
print("All student weights(lbs): " + str(weights_lbs)[1:-1])

# converting the lbs weights to kgs by multiplying with 0.45359237
weights_kg = []
for x in weights_lbs:
    weights_kg.append(float(x) * 0.45359237)
print("All student weights(kgs): " + str(weights_kg)[1:-1])

