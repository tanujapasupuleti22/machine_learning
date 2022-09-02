#question--1

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()#sort() is an inbuilt function used to sort.
min_a,min_b=ages[0],ages[len(ages)-1] #mininmum age and maximum age in list.
print("max and min elements are",min_a,min_b)
ages.append(min_a) # appending the min and max ages to the list
ages.append(min_b)
print("After adding the min and max elements to the list",ages)
if len(ages)%2 == 0:#finding the median age.
    median_a= (ages[len(ages)//2]+ ages[(len(ages)//2)-1])/2
else:
    median_a= ages[len(ages)//2]
print("Median age is",median_a)
average_a=sum(ages)/len(ages) #TO FIND AVERAGE AGE
print("Avearge age is",average_a)
range_a=ages[-1]-ages[0] #RANGE
print("Range of the ages is",range_a)



#question----2


dog={}#Creating empty dictionary called dog.
dog.update({'name':""})
dog.update({'color':""})
dog.update({'breed':""})
dog.update({'legs':""})
dog.update({'age':""})
print("Dog dictionary is: ",dog)
student={}#Initializing dictionary.
student['first_name']=""
student['last_name']=""
student['gender']=""
student['age']=0
student['martial status']=""
student['skills']=[]
student['country']=""
student['city']=""
student['address']=""
print("Student dictionary : ",student)
print("length of the student dictionary",len(student))
print("value of the skills",student['skills'])
print("Type of the skills",type(student['skills']))
student['skills']+=['sleeping','vacation planning']#Modifying the skill values by adding some skills.
print("Student dictionary keys are:",student.keys())
print("Student dictionary values are:",student.values())

#question-----3

brothers_t=('j','a','c','k')
siblings_t=()
print("Brothers tuple",brothers_t)
sisters_t=('a','m','m','a')
print("Sisters tuple: ",sisters_t)
siblings_t=sisters_t+brothers_t#adding two tuples into one.
print("Siblings are: ",siblings_t)
print("I got 8 siblings")
modify_list=list(siblings_t)#As tuples are immutable we cannot add other elements.If you still want to add then you have to convert the tuple to list and convert it back to tuple.
print("Modified list: ",modify_list)
modify_list.append("mom")
modify_list.append("dad")
family_members=tuple(modify_list)
print("Family members are: ",family_members)


#question------4


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

length_it=len(it_companies)#length of it_companies
print("length of the it_companies: ",length_it)

it_companies.add("Twitter")#Adding "Twitter" using add() method.
print("After Adding 'Twitter' to it_companies. ",it_companies)

it_companies.update(["Tcs","Tech Mahindra"])#Adding multiple companies using update() method.
print("After Adding  multiple companies to it_companies. ",it_companies)

it_companies.remove("Apple")#Deleting "Apple" using remove() method.
print("After Deleting 'Apple' : ",it_companies)
#it_companies.discard("Apple")#Deleting "Apple" using remove() method.
'''
The discard() method removes the specified item from the set.
This method is different from the remove() method, because the remove() method will raise an error
if the specified item does not exist, and the discard() method will not.
'''
join_ab=A.union(B)
print("After joining A and B: ",join_ab)
inter_ab=A.intersection(B)
print("A intersection B: ",inter_ab)
print("Is A  subset of B: ",A.issubset(B))# to test whether a is subset of b or not.
print("Is A disjoint of B: ",A.isdisjoint(B))# To test whether A isdisjoint of B.
A,B=A.union(B),B.union(A)
print("The symmetric difference of A and B:",A.symmetric_difference(B))#To find symmetric difference.
A.clear()#To clear the whole set.
B.clear()#To clear the whole set.
age_set=set(age)#To convert it into set.
len_age_set,len_age=len(age_set),len(age)
print("Length of the list and set are: ",len_age,len_age_set)#lentgh of age is reduced by "3" after converting it into set as age has 3 duplicate elements.


#question----5

radius_of_circle=30
_area_of_circle_=3.14*radius_of_circle*radius_of_circle#area of circle=pi*r*r and pi=3.14
print("Area of circle with a fixed radius : ",_area_of_circle_)
_circum_of_circle_=2*3.14*radius_of_circle
print("Circumference of a circle with a fixed radius : ",_circum_of_circle_)
r=int(input())#Reading input from user.
area_of_circle=3.14*r*r#area of circle=pi*r*r and pi=3.14
print("Area of circle with user input radius : ",area_of_circle)



#question----6

s="I am a teacher and I love to inspire and teach people"
s=s.split()
s=set(s)
print("Unique words used in the sentece are and the count is: ",s,len(s))

#question----7

print("Name\t\tAge\t\tCountry\t\tCity")
print("Asabeneh\t250\t\tFinland\t\tHelsinki")

#question----8

radius=10
area = int(3.14 * radius ** 2)
print("The area of a circle with radius {} is {} meters square".format(radius,area))#using string formatting method to get output.

#question----9

from math import trunc
N=int(input())#reading input from the user
l=[]
n = 2
for i in range(N):
    temp_var=int(input())/2.2046
    temp_var=int(temp_var*10**n)/10 ** n
    l.append(temp_var)
print("After converting into kilograms: ",l)










