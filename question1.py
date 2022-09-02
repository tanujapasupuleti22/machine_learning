ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("The original list : " + str(ages)[1:-1])

# using sort() function to sort a list
ages.sort()
print("The Sorted list: " + str(ages)[1:-1])

# using min() and max() functions to get min and max from a list
_min_age = min(ages)
_max_age = max(ages)
print("Minimum age: " + str(_min_age));
print("Maximum age: " + str(_max_age));

# using append() function to add values to a list
ages.append(_min_age)
ages.append(_max_age)
print("The New list: " + str(ages)[1:-1])

# if the length of list is even, then the median is average of middle two items.
# if the length of list is odd, then the median is the middle item.
_median_age = 0
if(len(ages)%2==0):
    index = len(ages)/2
    _median_age = (ages[index] + ages[index+1])/2;
else:
    _median_age = ages[(len(ages)+1)/2]
print("Median age: " + str(_median_age))

# using sum() to get the sum of all items in a list and diving it with length of items to get the average.
print("Average age: " + str(sum(ages)/len(ages)))

# using min() and max() functions to get the range. The range is obtained by subtracting max value by min
print ("Range of age: " + str(max(ages) - min(ages)))
