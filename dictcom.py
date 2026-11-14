# Dictionary Comprehension

# creating a dictionary of squares

numbers = [1,2,3,4,5]
squres = {num : num**2 for num in numbers}
print(squres)

# convert names into uppercase

names = ["Kavita","Lalita","Shivaraj","Puttaraj"]
upper_names = {name : name.upper() for name in names}
print(upper_names)

# convert names into uppercase with condition

names = ["Kavita","Lalita","Shivaraj","Puttaraj"]
upper_names = {name : name.upper() for name in names if name == "Lalita"}
print(upper_names)

# converting a list of numbers to a dictionary of name lengths

names = ["Anand","Geeta","Laxmi","Puneeth"]
name_len = {name:len(name) for name in names}
print(name_len)

# Filtering cities with population above 100

city_population = {"Gadag" : 200,
                   "Koppal":99,
                   "Haveri":103,
                   "Kodagu":87
                   }
highest_population = {city : pop for city,pop in city_population.items() if pop > 100}
print(highest_population)

# printing age which is above 18

name_ages = {"Basu" : 10,"Saraswati": 21,"Avinash": 34,"Pallavi": 16}
highest_age = {name : age for name,age in name_ages.items() if age>18}
print(highest_age)

# convert Celsius into Fahrenheit

celsius = [0, 10, 20, 30, 40]
fahrenheit = {temp : (temp * 9/5) + 32  for temp in celsius}
print(fahrenheit)

# Create a dictionary of students and marks

students = ["Rahule","Priya","Amit"]
marks = [85, 90, 75]

result = {students[i] : marks [i] for i in range (len(students))}
print(result)




