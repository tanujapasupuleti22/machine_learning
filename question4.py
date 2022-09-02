it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# using len() function to get the length of the set it_companies
print("IT Companies length: " + str(len(it_companies)))
print("IT Companies: " + str(it_companies)[1:-1])

# Added 'Twitter' to it_companies using add()
it_companies.add("Twitter")
print("after adding twitter: " + str(it_companies)[1:-1])

# inserted multiple IT companies at once to the set it_companies by using update()
multiple_companies = ["BMW", "Tesla", "Audi"]
it_companies.update(multiple_companies)
print("after adding multiple IT Companies: " + str(it_companies)[1:-1])

# Removing one of the companies from the set it_companies using remove()
it_companies.remove("IBM")
print("After removeing IBM: " + str(it_companies)[1:-1])

# The remove() function removes the element from the set only if the element is present in the set,
# however when we use discard() method and if the element is not present in the set, an error or exception is raised.

# joining A and B using union()
join_AB = A.union(B)
print("A and B union: " + str(join_AB)[1:-1])

# getting intersection of A and B using intersection()
inter_AB = A.intersection(B)
print("A and B intersection: " + str(inter_AB)[1:-1])

# using issubset() to check if A is subset of B
print("Is A subset of B: " + str(A.issubset(B)))

# using isdisjoint() to check if A and B are disjoint
print("Are A and B disjoint sets: " + str(A.isdisjoint(B)))

# Joining A with B and B with A using union() and using symmetric_difference() to get the symmetric difference b/w two
aWithb = A.union(B)
bWitha = B.union(A)
print("A with B union: " + str(aWithb)[1:-1])
print("B with A union: " + str(bWitha)[1:-1])
print("Symmetric difference: " + str(A.symmetric_difference(B))[1:-1])

# deleting the sets using clear()
A.clear()
B.clear()
print("after deleting A: " +str(A)[1:-1])
print("after deleting B: " +str(B)[1:-1])

# Converting the age to a set using set() function and comparing the length of the list and the set.
print("Length of age as list: " + str(len(age)))
print("Length of age as set: " + str(len(set(age))))

# The set length is less than list length as duplicates are eliminated in set.
