# Creating two tuples containing names of my sisters and brothers
sisters = ("reshma", "pooja")
brothers = ("vijay", "sai")
print("Sisters: " + str(sisters)[1:-1])
print("Brothers: " + str(brothers)[1:-1])

# using + to join brothers and sisters tuples and assigned it to siblings
siblings = sisters + brothers
print("Siblings: " + str(siblings)[1:-1])

# using len() fucntion to get the number of siblings
print("Number of siblings: " + str(len(siblings)))

# as tuples are immutable we cannot add other elements.
# hence converting the tuple to list and adding to add parents name and converting it back to tuple
familyList = list(siblings)
# modifying existing siblings
familyList[2] = "shonu"
# adding parents to the list
familyList.append("PBK")
familyList.append("lakshmi")
siblings = tuple(familyList)
print("Modified Siblings: " + str(siblings)[1:-1])

# creating an empty family_members tuple
family_members = tuple()
family_members += siblings;
print("Family members: " + str(family_members)[1:-1])
