# strings = words letters string
# ints = whole numbers
# floats = 20.5
# Booleans = true/false
import math

# strings
# print("hello world")
# print("welcome")
#
# first_name = "bro"
# last_name = "code"
#
# full_name = first_name + " " + last_name
# print (full_name)


# int
# age = 21
# age += 1
# print ("your age is " + str(age))
# print(type(age))


# floats
# height = 250.5
# print("your height is " + str(height))
# print(type(height))

# Booleans
# human = False
#
# print("are you a human or alien?" + str(human))
# print (type(human))


# MULTIPLE ASSIGNMENTS
# name = "bro"
# age = 21
# attractive = true

# name, age, attractive = "bro", 21, True
# print(name,age,attractive)


# bob = ryan = kim = danny = 30
# print(bob, ryan, kim, danny)


#
# CONCAT AND .UPPER
# name = "lorenzo"

# print(len(name))
# print(name.find("z"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())

# is only numbers
# print(name.isdigit())

# is only letters
# print(name.isalpha())

# count how many
# print(name.count("o"))
#
# print(name.replace("o", "A"))
# print(name*3)

# INPUT!!!!
# name = input("what is your name?: ")
# print("hello " + name)
#
# # CAST INPUT
# age = int(input("how old are you"))
# age = age + 1
# height = float(input("how tall are you?: "))
# print(age)
# # CAST INT/float TO STR
# print ("you are " + str(age) + "years old" )
# print("you are " + str(height) + "tall:")



# # IMPORT MATH

# pi = -3.14
#
# # print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
#
# # ABSOLUTE SQUARE
# print(abs(pi))
#
# # POWER
# print(pow(pi,2))
#
# # SQUARE ROOT
# print(math.sqrt(420))
#
# x = 1
# y = 2
# z = 3
# print(max(x,y,z))
# print(min(x,y,z))

# STRING SLICING create a sub string or extract elements from string
#   indexing []  or slicing()
#   [start:stop:step]

# name = "lorenzo smith"
#
# first_name = name[0:7]
# # or first_name = name[:7]
# print(first_name)
#
# last_name = name[8:13]
# # or last_name = name[8:]
# print(last_name)
#
# random_name = name[:13:2]
# print(random_name)


# SLICING
# website = "http://google.com"
#
# website_name = slice(7, -4)
#
# print(website[website_name])


# # IF STATMENTS
# age = int(input("what is your age?:"))
#
# if age >= 18:
#     print("you are a ADULT!")
# elif age < 0:
#     print("you havent been born yet")
# elif age == 100:
#     print("you are century year old")
# else:
#     print("you are a child!")

# # LOGICAL OPERATORS and or not (used to check two or more conditional statments)
# temp = int(input("what temperature outside"))
#
# if temp >= 0 and temp <= 30:
#     print("the temperature is just right for outside play")
#
# elif temp < 0 or temp >30:
#     print("the weather is bad today")
#
# not flips from true to false


# WHILE LOOPS
# name = ""
#
# while len(name) == 0:
#     name = input("what is your name")
#
# print("hello " + name)


# FOR-LOOPS     LOOP execute block code
#         limited amount of times
#
#         while = unlimited
#         for loops = limited
# for i in range(10):
#     print(i+1)

# for i in range(50,100,2):
#     print(i+1)

# for i in "lorenzo smith":
#     print(i)


# import time
#
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(2)
# print("happy new year")

# NESTED LOOPS = the "inner loop" will finish all its iterations before
#                                 finishing one itteration of the "outer loop"
#
# rows = int(input("how many rows"))
# columns = int(input("how many columns"))
# symbol = input("enter a symbol to use")
#
# for i in range (rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()


# LOOP CONTROL STATMENTS !!!! change a loops execution from its normal sequence
#
# BREAK =       used to terminate the loop entirely
# CONTINUE =    skips to next iteration of the loop
# PASS =        does nothing acts as placeholder

# while True:
#     name = input("you must enter you name please")
#     if name != "":
#         break

# phone_number = "123-456-789"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1,21):
#     if i == 13:
#         pass
#     else: print(i)


# LIST
# # turn variable into list with ELEMENTS
# food = ["pizza", "pasta", "grapes", "apples", ]
#
# # food[2] = "sushi"
# #
# # print(food[2])
# #
# # for x in food:
# #     print(x)
#
# food2 = "chicken", "steak", "tacos", "pancakes", "mac & cheese"
#
# food.insert(0,"cake")
# food.append("ice cream")
#
# food2.sort()
# food2.remove("chicken")
# food2.pop()
#

# # 2D list list = list of list
#
# drinks = ["soda", "coffee", "juice"]
# dinner = ["steak", "pasta" "chicken", "fish"]
# desserts = ['cake', 'ice cream', 'pastery' ]
#
# food = [drinks, dinner, desserts]
#
# print(food[2][1])




# # TUPLE =    collection which is unchangeable
# #             used to group related data
#
# student = ("bro", 21, "male")
#
# print(student.count("bro"))
# print(student.index("bro"))
#
# for x in student:
#     print(x)
#
# if 21 in student:
#     print("you can drink")


# SET = {} collection which is unordered and unindexed no duplicates allowed

utensile = {"fork", "spoon", "knife"}
china = {"bowls", "plates", "cups", "knife"}


# utensile.add("napkin")
# utensile.remove ("spoon")
# utensile.clear()

# china.update(utensile)

# dinner_table = utensile.union(china)

# for x in dinner_table:
#     print(x)

# print(utensile.difference(china))
# print(china.difference(utensile))
#
# print(china.intersection(utensile))


# DICTIONARYS =  changeable unordered pair unique value pairs
#                 key:value allows for hashing and access to value pairs quickley

# capitals = {"USA": "Washington DC",
#             "India": "New Delhi",
#             "China": "Bejing",
#             "Russia": "Moscow"}
#
# capitals.update({"Germany":"Berlin"})
#
# capitals.update({"USA": "Las Vegas"})
#
# capitals.pop("China")


# print(capitals['Russia'])

# print(capitals.get('Germany'))
#
# print(capitals.keys())
# print(capitals.values())
#
# print(capitals.items())

# for key,value in capitals.items():
#     print(key, value)
# CHANGE DICTIONARY'S WHILE PROGRAM IS RUNNING



# # INDEX OPERATORS [] = gives acces to sequence of elements
# #                      (str,list,tuples)
#
#
# name = "lorenzo Smith"
#
# # if(name[0].islower()):
# #     name = name.capitalize()
#
# first_name = name[:7].upper()
# last_name = name [8:].upper()
#
#
# print(first_name)
# print(last_name)
















