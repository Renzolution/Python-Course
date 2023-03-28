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

student = ("bro", 21, "male")

print(student.count("bro"))
print(student.index("bro"))
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


# # arrays vs tuples

# # array of tuples
# coords1 = [(0, 0), (1, 1), (2, 2)]

# # array of arrays
# coords2 = [[0, 0], [1, 1], [2, 2]]

# print(coords1)
# print(coords2)
# print(coords1 + coords2)


# # Dictionaries
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])


# # assign new key value pairs
# pie = {'flavor'}


# tuples can have tuples, list/array, or floats
# # tuples are un modifiable
# dimension = (200, 50)
# # class type
# print(type(dimension))
# # can not change
# # dimension[0] = 100

# # Adding/Assign to tuple
# alien = {}
# alien['color'] = 'green'
# alien['points'] = 5
# print(alien)


# # nesting tuples
# tuple1 = (1, 3, 6, 7, 9)
# tuple2 = (2, 'python', 'jave')
# tuple3 = (tuple1, tuple2)
# print(tuple3)

# # slicing nested tuples

# print(tuple1[2:])
# print(tuple2[-2:])

# # turn tuple into list
# tuple1 = (1, 3, 6, 7, 9)
# list1 = list(tuple1)
# print(list1)

# list2 = [1,6,8,9]
# print(list2)


# # loop through tuple
# for i in dimension:
#     print(i)


# alien_0 = {'color': 'grenn', 'height': '7feet'}
# print("the alien color is " + alien_0['color'] + "!")

# alien_0['color'] = 'Purple'
# print("the alien has morphed into a " + alien_0['color'] + " alien!")

# # del tuple information
# del alien_0['color']

# print(alien_0)

# # task 1/////////////////////
# list = []
# tuple = ()
# # using **arbituary will allow for many data set:


# def build_profile(first, last, **user_info):

#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile


# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# # print(user_profile)

# # print specific dictionary
# # KEY:Value
# user_0 = {
#     'username': 'renzo',
#     'first_name': 'lorenzo',
#     'last_name': 'smith',
# }

# # print the key or the value
# for key, value in user_0.items():
#     print("key   ---" + key)
#     print("value   ---" + value)

# # task 2//////////////////
# author = {}

# author['first_name-1'] = ' lorenzo'
# author['first_name-2'] = ' bob'
# author['first_name-3'] = ' jamie'
# author['first_name-4'] = ' john'
# author['first_name-5'] = ' susan'
# author['first_name-6'] = ' mary'

# for name, author in author.items():
#     print(author)


# author['username'] = ('lorenzo', 'bob', 'jamie', 'john', 'susan', 'mary')
# for name, value in author.items():
#     print(name)
#     print(value)
#     # print(author)


# # 2-1
# message = "Hello World!"
# print(message)

# # 2-2
# message1 = "Hello World!"
# message1 = "i am a replace string"
# print(message1)


# # 2-3
# name = 'PersonName'

# print("hello there " + name + "very nice to meet you")

# # 2-4
# print(name.lower())
# print(name.upper())
# print(name.title())

# # 2-5
# quote = '-Nikola Tesla \"If you want to find the secrets of the universe, think in terms of energy, frequency and vibration.\"'
# print(quote)
# # 2-6

# famous_person = 'Nikola Tesla'
# Famous_quote = famous_person + \
#     ' \"If you want to find the secrets of the universe, think in terms of energy, frequency and vibration.\"'
# print(Famous_quote)

# # 2-7
# WName = "   Elon   Musk   "
# Wname2 = "   Elon  \t Musk \n is a astronaut"
# print(Wname2)
# print(WName)
# print(WName.strip())
# print(WName.lstrip())
# print(WName.rstrip())

# # 2-8 being able to manipulate numbers is a very crucial part of programming
# print(4+4)
# print(12-4)
# print(4*2)
# print(72/9)

# # 2-9 this is a comment this program is a variable int that is transformed into a string
# secret_number = 96
# print("my secret number is " + str(secret_number))

# # 2-10


# # DNA Exercise

# DNA = "ATAACTG"
# RNA = DNA.replace("T", "U")

# print(RNA)


# # workbook
# 1 lines up perfectly
# mailing = "Lorenzo Smith \nrenzolutionn@gmail.com \nThaddesus Stevens College"
# print(mailing.strip())
# 2
# ask1 = input("what is your name")
# print("hello " + ask1)
# 3 area
# Width = int(input("What is the width "))
# length = int(input("what is the length "))
# Area = Width * length
# Result = "the area of the room is " + \
#     str(length) + "*" + str(Width) + "=" + str(Area)
# print(Result)
# 4 Farmer filed are
# convert1 = int(input("How many Feet wide is your farm"))
# Result2 = convert1/43560
# print(Result2)
# 5 Bottle Deposits
# liter1 = int(input("how many 1 liter bottles of water do you have?"))
# liter2 = int(input("how many 2 liter or more bottles of water do you have?"))
# liter1Return1 = liter1*0.10
# liter2Return2 = liter2*0.25
# print(str(liter1Return1) + " 1 liter bottles of water bonus")
# print(str(liter2Return2) + " 2 liter bottles of water bonus")
# 6 Tax and Tip
# cost = int(input("food item cost__"))
# tax = 0.06
# taxReturn = cost*tax
# tip = 1.18
# tipReturn = cost*tip
# print("your food item cost" + str(cost) +
#       " tax is " + str(round(taxReturn, 2)) +
#       " and tip amount is " + str(round(tipReturn, 2)))

# 7 wrong
# math1 = int(input("lets find the sum of all numbers from 1 and your number"))
# base = 0
# number = 1
# while base < math1:
#     base += 1 * math1 / 2
# print(base)

# 8 Widgets and Gizmos
# Widget = 75
# gizmo = 112
# WI = int(input("Widget count"))
# GI = int(input("Gizmo count"))
# Wamount = Widget * WI
# Gamount = gizmo * GI

# result = Wamount + Gamount
# total = str(result) + " is your total order weight"
# print(total)

# 9 Compund interest


# 10 finish Arithmetic
# input1 = int(input("Enter a number"))
# input2 = int(input("Enter another number"))
# return1 = input1 + input2
# return2 = input2 - input1
# return3 = input1 * input2
# return4 = input1 / input2
# return5 = input1 % input2
# return6 =
# return7 =
# print(return1)
# print(return2)
# print(return3)
#
# 11 Fuel MPG to kL

# input1 = int(input("Enter a MPG number"))
# convert = 235.214583/input1
# print(convert)

# import math
# 12distance between two points on earth


# def distance_on_unit_sphere(lat1, long1, lat2, long2):

#     # Convert latitude and longitude to radians
#     degrees_to_radians = math.pi/180.0
#     phi1 = (90.0 - lat1)*degrees_to_radians
#     phi2 = (90.0 - lat2)*degrees_to_radians
#     theta1 = long1*degrees_to_radians
#     theta2 = long2*degrees_to_radians

#     # Calculate spherical distance from spherical coordinates
#     cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
#            math.cos(phi1)*math.cos(phi2))
#     arc = math.acos(cos)

#     # Radius of Earth in kilometers
#     radius = 6371.0

#     # Return distance in kilometers
#     return arc * radius


# # Get latitude and longitude of the first point
# lat1 = float(input("Enter latitude of point 1 in degrees: "))
# long1 = float(input("Enter longitude of point 1 in degrees: "))

# # Get latitude and longitude of the second point
# lat2 = float(input("Enter latitude of point 2 in degrees: "))
# long2 = float(input("Enter longitude of point 2 in degrees: "))

# # Calculate distance between the two points in kilometers
# distance = distance_on_unit_sphere(lat1, long1, lat2, long2)

# # Display the distance between the two points
# print(
#     "The distance between the two points is {:.2f} kilometers.".format(distance))

# # 13 change machince program
# # q1 = int(input("input change amount in cents"))


# # def compute_change(change):
# #     toonies = change // 200
# #     change %= 200
# #     loonies = change // 100
# #     change %= 100
# #     quarters = change // 25
# #     change %= 25
# #     dimes = change // 10
# #     change %= 10
# #     nickels = change // 5
# #     change %= 5
# #     pennies = change
# #     return (toonies, loonies, quarters, dimes, nickels, pennies)

# # # Get input from user
# # change = int(input("Enter the amount of change in cents: "))

# # # Compute the minimum number of coins required to make the change
# # coins = compute_change(change)

# # # Display the result
# # print("Toonies: ", coins[0])
# # print("Loonies: ", coins[1])
# # print("Quarters: ", coins[2])
# # print("Dimes: ", coins[3])
# # print("Nickels: ", coins[4])
# # print("Pennies: ", coins[5])

# # 14 feet and inch to centimeter conversion
# # user1 = int(input("Enter feet "))
# # user2 = int(input("Enter inches "))

# # user1Return = user1 * 30.48
# # user2Return = user2 * 2.54
# # print(str(user1Return) + "this is how many centimetres you have for feet")
# # print(str(user2Return) + "this is how many centimeter you have for inches")

# # 15 feet to inches yards and miles conversion
# user1 = int(input("Enter feet "))

# inches = user1 * 0.0254
# yards =
# miles = user1 * 0.3048
# 16area and volume
# import math
# r = float(input("Enter Radius "))
# area = math.pi * r ** 2
# volume = 4/3 - math.pi * r ** 3
# print(f"Area of circle with radius {r}: {area:.2f}")
# print(f"Volume of sphere with radius {r}: {volume:.2f}")
# # 17 heat capacity
# # read input from user
# m = float(input("Enter the mass of water in grams: "))
# delta_T = float(input("Enter the change in temperature in degrees Celsius: "))

# # specific heat capacity of water in J/g·°C
# C = 4.186

# # calculate the amount of energy required
# q = m * C * delta_T

# # display the result
# print(f"The amount of energy required is {q:.2f} joules.")
# 18 volume of a cylinder
# base = int(input("Enter the base of the cylinder: "))
# height = int(input("Enter the height of the cylinder: "))
# volume = base * height
# print(f"The volume of the cylinder is {volume:.2f}")

# 19
# import math

# # read input from user
# h = float(input("Enter the height from which the object is dropped (in meters): "))

# # acceleration due to gravity in m/s^2
# a = 9.8

# # initial speed is 0 m/s
# vi = 0

# # distance fallen (d) is the same as the height from which the object is dropped
# d = h

# # calculate the final speed (vf) using the formula vf^2 = vi^2 + 2ad
# vf = math.sqrt(vi ** 2 + 2 * a * d)

# # display the result
# print(f"The final speed of the object when it hits the ground is {vf:.2f} m/s.")
# 20 ideal gas constant
# R = 8.314 # J/(mol*K)

# # read input from user
# p = float(input("Enter the pressure (in Pascals): "))
# v = float(input("Enter the volume (in liters): "))
# t = float(input("Enter the temperature (in degrees Celsius): "))

# # convert temperature from Celsius to Kelvin
# t += 273.15

# # calculate the number of moles using the ideal gas law
# n = (p * v) / (R * t)

# # display the result
# print(f"The amount of gas in moles is {n:.2f} moles.")
# 21 area of a triangle
# b = int(input("Enter the base of the triangle: "))
# h = int(input("Enter the height of the triangle: "))
# area = (b * h) / 2
# print(f"The area of the triangle is {area:.2f}")
# # 22
# import math

# # read input from user
# a = float(input("Enter the length of side a: "))
# b = float(input("Enter the length of side b: "))
# c = float(input("Enter the length of side c: "))

# # calculate the semi-perimeter
# s = (a + b + c) / 2

# # calculate the area using Heron's formula
# area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# # display the result
# print(f"The area of the triangle is {area:.2f} square units.")
# 23 area of a regular polygon
# import math

# # read input from user
# s = float(input("Enter the length of a side of the polygon: "))
# n = int(input("Enter the number of sides of the polygon: "))

# # calculate the area of the polygon
# area = (n * s**2) / (4 * math.tan(math.pi / n))

# # display the result
# print(f"The area of the polygon is {area:.2f} square units.")
# # 24
# # Read the duration from the user
# days = int(input('Enter number of days: '))
# hours = int(input('Enter number of hours: '))
# minutes = int(input('Enter number of minutes: '))
# seconds = int(input('Enter number of seconds: '))

# # Compute the total number of seconds
# total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds

# # Display the result
# print('The total number of seconds is:', total_seconds)
# 25
# Read the number of seconds from the user
# total_seconds = int(input("Enter the number of seconds: "))

# # Compute the days, hours, minutes and seconds
# days = total_seconds // (24 * 3600)
# remaining_seconds = total_seconds % (24 * 3600)
# hours = remaining_seconds // 3600
# remaining_seconds %= 3600
# minutes = remaining_seconds // 60
# seconds = remaining_seconds % 60

# # Format the output string
# output_string = "{:02d}:{:02d}:{:02d}:{:02d}".format(days, hours, minutes, seconds)

# # Display the output
# print(output_string)
# # 26 current time
# import time

# # Get the current time and date
# current_time = time.asctime()

# # Display the current time and date
# print("The current time and date is:", current_time)

# # 27 body mass index
# # read the height in inches from the user
# height = float(input("Enter your height in inches: "))

# # read the weight in pounds from the user
# weight = float(input("Enter your weight in pounds: "))

# # calculate the BMI using the formula
# bmi = (weight / (height ** 2)) * 703

# # display the result
# print("Your BMI is: {:.2f}".format(bmi))
# 28
# import math

# # read input values from the user
# t = float(input("Enter the air temperature in degrees Fahrenheit: "))
# v = float(input("Enter the wind speed in miles per hour: "))

# # compute the wind chill index
# wci = 35.74 + 0.6215*t - 35.75*math.pow(v, 0.16) + 0.4275*t*math.pow(v, 0.16)

# # round the result to the nearest integer
# wci = round(wci)

# # display the result
# print("The wind chill index is:", wci)

# 29celsius to fahrenheit
# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = (celsius * 1.8) + 32
# kelvin = celsius + 273.15

# print("Temperature in Fahrenheit: {:.2f}".format(fahrenheit))
# print("Temperature in Kelvin: {:.2f}".format(kelvin))
# # 30 units of pressure
# pressure_kpa = float(input("Enter the pressure in kilopascals: "))

# # Convert to pounds per square inch
# pressure_psi = pressure_kpa * 0.145038

# # Convert to millimeters of mercury
# pressure_mmhg = pressure_kpa * 7.50062

# # Convert to atmospheres
# pressure_atm = pressure_kpa / 101.325

# # Display the results
# print("Pressure in pounds per square inch:", round(pressure_psi, 2))
# print("Pressure in millimeters of mercury:", round(pressure_mmhg, 2))
# print("Pressure in atmospheres:", round(pressure_atm, 2))
# 31 sum of digits seperated by index []
# num = input("Enter a four-digit integer: ")

# # Convert the string to individual digits and add them together
# sum_of_digits = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])

# # Display the sum of the digits
# print("The sum of the digits is:", sum_of_digits)

# 32
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# minimum = min(num1, num2, num3)
# maximum = max(num1, num2, num3)
# middle = (num1 + num2 + num3) - minimum - maximum

# print("The sorted numbers are:", minimum, middle, maximum)

# # 33 day ols bread
# num_loaves = int(input("Enter the number of loaves: "))

# regular_price = num_loaves * 3.49
# discount_price = regular_price * 0.6
# total_price = regular_price - discount_price

# print(f"Discount Price: ${discount_price:6.2f}")
# print(f"regular price: ${regular_price:6.2f}")
# print(f"total price: ${total_price:6.2f}")


# # 2-1
# message = "Hello World!"
# print(message)

# # 2-2
# message1 = "Hello World!"
# message1 = "i am a replace string"
# print(message1)


# # 2-3
# name = 'PersonName'

# print("hello there " + name + "very nice to meet you")

# # 2-4
# print(name.lower())
# print(name.upper())
# print(name.title())

# # 2-5
# quote = '-Nikola Tesla \"If you want to find the secrets of the universe, think in terms of energy, frequency and vibration.\"'
# print(quote)
# # 2-6

# famous_person = 'Nikola Tesla'
# Famous_quote = famous_person + \
#     ' \"If you want to find the secrets of the universe, think in terms of energy, frequency and vibration.\"'
# print(Famous_quote)

# # 2-7
# WName = "   Elon   Musk   "
# Wname2 = "   Elon  \t Musk \n is a astronaut"
# print(Wname2)
# print(WName)
# print(WName.strip())
# print(WName.lstrip())
# print(WName.rstrip())

# # 2-8 being able to manipulate numbers is a very crucial part of programming
# print(4+4)
# print(12-4)
# print(4*2)
# print(72/9)

# # 2-9 this is a comment this program is a variable int that is transformed into a string
# secret_number = 96
# print("my secret number is " + str(secret_number))

# # 2-10


# # DNA Exercise

# DNA = "ATAACTG"
# RNA = DNA.replace("T", "U")

# print(RNA)


# # workbook
# 1 lines up perfectly
# mailing = "Lorenzo Smith \nrenzolutionn@gmail.com \nThaddesus Stevens College"
# print(mailing.strip())
# 2
# ask1 = input("what is your name")
# print("hello " + ask1)
# 3 area
# Width = int(input("What is the width "))
# length = int(input("what is the length "))
# Area = Width * length
# Result = "the area of the room is " + \
#     str(length) + "*" + str(Width) + "=" + str(Area)
# print(Result)
# 4 Farmer filed are
# convert1 = int(input("How many Feet wide is your farm"))
# Result2 = convert1/43560
# print(Result2)
# 5 Bottle Deposits
# liter1 = int(input("how many 1 liter bottles of water do you have?"))
# liter2 = int(input("how many 2 liter or more bottles of water do you have?"))
# liter1Return1 = liter1*0.10
# liter2Return2 = liter2*0.25
# print(str(liter1Return1) + " 1 liter bottles of water bonus")
# print(str(liter2Return2) + " 2 liter bottles of water bonus")
# 6 Tax and Tip
# cost = int(input("food item cost__"))
# tax = 0.06
# taxReturn = cost*tax
# tip = 1.18
# tipReturn = cost*tip
# print("your food item cost" + str(cost) +
#       " tax is " + str(round(taxReturn, 2)) +
#       " and tip amount is " + str(round(tipReturn, 2)))

# 7 wrong
# math1 = int(input("lets find the sum of all numbers from 1 and your number"))
# base = 0
# number = 1
# while base < math1:
#     base += 1 * math1 / 2
# print(base)

# 8 Widgets and Gizmos
# Widget = 75
# gizmo = 112
# WI = int(input("Widget count"))
# GI = int(input("Gizmo count"))
# Wamount = Widget * WI
# Gamount = gizmo * GI

# result = Wamount + Gamount
# total = str(result) + " is your total order weight"
# print(total)

# 9 Compund interest


# 10 finish Arithmetic
# input1 = int(input("Enter a number"))
# input2 = int(input("Enter another number"))
# return1 = input1 + input2
# return2 = input2 - input1
# return3 = input1 * input2
# return4 = input1 / input2
# return5 = input1 % input2
# return6 =
# return7 =
# print(return1)
# print(return2)
# print(return3)
#
# 11 Fuel MPG to kL

# input1 = int(input("Enter a MPG number"))
# convert = 235.214583/input1
# print(convert)

# import math
# 12distance between two points on earth


# def distance_on_unit_sphere(lat1, long1, lat2, long2):

#     # Convert latitude and longitude to radians
#     degrees_to_radians = math.pi/180.0
#     phi1 = (90.0 - lat1)*degrees_to_radians
#     phi2 = (90.0 - lat2)*degrees_to_radians
#     theta1 = long1*degrees_to_radians
#     theta2 = long2*degrees_to_radians

#     # Calculate spherical distance from spherical coordinates
#     cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
#            math.cos(phi1)*math.cos(phi2))
#     arc = math.acos(cos)

#     # Radius of Earth in kilometers
#     radius = 6371.0

#     # Return distance in kilometers
#     return arc * radius


# # Get latitude and longitude of the first point
# lat1 = float(input("Enter latitude of point 1 in degrees: "))
# long1 = float(input("Enter longitude of point 1 in degrees: "))

# # Get latitude and longitude of the second point
# lat2 = float(input("Enter latitude of point 2 in degrees: "))
# long2 = float(input("Enter longitude of point 2 in degrees: "))

# # Calculate distance between the two points in kilometers
# distance = distance_on_unit_sphere(lat1, long1, lat2, long2)

# # Display the distance between the two points
# print(
#     "The distance between the two points is {:.2f} kilometers.".format(distance))

# # 13 change machince program
# # q1 = int(input("input change amount in cents"))


# # def compute_change(change):
# #     toonies = change // 200
# #     change %= 200
# #     loonies = change // 100
# #     change %= 100
# #     quarters = change // 25
# #     change %= 25
# #     dimes = change // 10
# #     change %= 10
# #     nickels = change // 5
# #     change %= 5
# #     pennies = change
# #     return (toonies, loonies, quarters, dimes, nickels, pennies)

# # # Get input from user
# # change = int(input("Enter the amount of change in cents: "))

# # # Compute the minimum number of coins required to make the change
# # coins = compute_change(change)

# # # Display the result
# # print("Toonies: ", coins[0])
# # print("Loonies: ", coins[1])
# # print("Quarters: ", coins[2])
# # print("Dimes: ", coins[3])
# # print("Nickels: ", coins[4])
# # print("Pennies: ", coins[5])

# # 14 feet and inch to centimeter conversion
# # user1 = int(input("Enter feet "))
# # user2 = int(input("Enter inches "))

# # user1Return = user1 * 30.48
# # user2Return = user2 * 2.54
# # print(str(user1Return) + "this is how many centimetres you have for feet")
# # print(str(user2Return) + "this is how many centimeter you have for inches")

# # 15 feet to inches yards and miles conversion
# user1 = int(input("Enter feet "))

# inches = user1 * 0.0254
# yards =
# miles = user1 * 0.3048
# 16area and volume
# import math
# r = float(input("Enter Radius "))
# area = math.pi * r ** 2
# volume = 4/3 - math.pi * r ** 3
# print(f"Area of circle with radius {r}: {area:.2f}")
# print(f"Volume of sphere with radius {r}: {volume:.2f}")
# # 17 heat capacity
# # read input from user
# m = float(input("Enter the mass of water in grams: "))
# delta_T = float(input("Enter the change in temperature in degrees Celsius: "))

# # specific heat capacity of water in J/g·°C
# C = 4.186

# # calculate the amount of energy required
# q = m * C * delta_T

# # display the result
# print(f"The amount of energy required is {q:.2f} joules.")
# 18 volume of a cylinder
# base = int(input("Enter the base of the cylinder: "))
# height = int(input("Enter the height of the cylinder: "))
# volume = base * height
# print(f"The volume of the cylinder is {volume:.2f}")

# 19
# import math

# # read input from user
# h = float(input("Enter the height from which the object is dropped (in meters): "))

# # acceleration due to gravity in m/s^2
# a = 9.8

# # initial speed is 0 m/s
# vi = 0

# # distance fallen (d) is the same as the height from which the object is dropped
# d = h

# # calculate the final speed (vf) using the formula vf^2 = vi^2 + 2ad
# vf = math.sqrt(vi ** 2 + 2 * a * d)

# # display the result
# print(f"The final speed of the object when it hits the ground is {vf:.2f} m/s.")
# 20 ideal gas constant
# R = 8.314 # J/(mol*K)

# # read input from user
# p = float(input("Enter the pressure (in Pascals): "))
# v = float(input("Enter the volume (in liters): "))
# t = float(input("Enter the temperature (in degrees Celsius): "))

# # convert temperature from Celsius to Kelvin
# t += 273.15

# # calculate the number of moles using the ideal gas law
# n = (p * v) / (R * t)

# # display the result
# print(f"The amount of gas in moles is {n:.2f} moles.")
# 21 area of a triangle
# b = int(input("Enter the base of the triangle: "))
# h = int(input("Enter the height of the triangle: "))
# area = (b * h) / 2
# print(f"The area of the triangle is {area:.2f}")
# # 22
# import math

# # read input from user
# a = float(input("Enter the length of side a: "))
# b = float(input("Enter the length of side b: "))
# c = float(input("Enter the length of side c: "))

# # calculate the semi-perimeter
# s = (a + b + c) / 2

# # calculate the area using Heron's formula
# area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# # display the result
# print(f"The area of the triangle is {area:.2f} square units.")
# 23 area of a regular polygon
# import math

# # read input from user
# s = float(input("Enter the length of a side of the polygon: "))
# n = int(input("Enter the number of sides of the polygon: "))

# # calculate the area of the polygon
# area = (n * s**2) / (4 * math.tan(math.pi / n))

# # display the result
# print(f"The area of the polygon is {area:.2f} square units.")
# # 24
# # Read the duration from the user
# days = int(input('Enter number of days: '))
# hours = int(input('Enter number of hours: '))
# minutes = int(input('Enter number of minutes: '))
# seconds = int(input('Enter number of seconds: '))

# # Compute the total number of seconds
# total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds

# # Display the result
# print('The total number of seconds is:', total_seconds)
# 25
# Read the number of seconds from the user
# total_seconds = int(input("Enter the number of seconds: "))

# # Compute the days, hours, minutes and seconds
# days = total_seconds // (24 * 3600)
# remaining_seconds = total_seconds % (24 * 3600)
# hours = remaining_seconds // 3600
# remaining_seconds %= 3600
# minutes = remaining_seconds // 60
# seconds = remaining_seconds % 60

# # Format the output string
# output_string = "{:02d}:{:02d}:{:02d}:{:02d}".format(days, hours, minutes, seconds)

# # Display the output
# print(output_string)
# # 26 current time
# import time

# # Get the current time and date
# current_time = time.asctime()

# # Display the current time and date
# print("The current time and date is:", current_time)

# # 27 body mass index
# # read the height in inches from the user
# height = float(input("Enter your height in inches: "))

# # read the weight in pounds from the user
# weight = float(input("Enter your weight in pounds: "))

# # calculate the BMI using the formula
# bmi = (weight / (height ** 2)) * 703

# # display the result
# print("Your BMI is: {:.2f}".format(bmi))
# 28
# import math

# # read input values from the user
# t = float(input("Enter the air temperature in degrees Fahrenheit: "))
# v = float(input("Enter the wind speed in miles per hour: "))

# # compute the wind chill index
# wci = 35.74 + 0.6215*t - 35.75*math.pow(v, 0.16) + 0.4275*t*math.pow(v, 0.16)

# # round the result to the nearest integer
# wci = round(wci)

# # display the result
# print("The wind chill index is:", wci)

# 29celsius to fahrenheit
# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = (celsius * 1.8) + 32
# kelvin = celsius + 273.15

# print("Temperature in Fahrenheit: {:.2f}".format(fahrenheit))
# print("Temperature in Kelvin: {:.2f}".format(kelvin))
# # 30 units of pressure
# pressure_kpa = float(input("Enter the pressure in kilopascals: "))

# # Convert to pounds per square inch
# pressure_psi = pressure_kpa * 0.145038

# # Convert to millimeters of mercury
# pressure_mmhg = pressure_kpa * 7.50062

# # Convert to atmospheres
# pressure_atm = pressure_kpa / 101.325

# # Display the results
# print("Pressure in pounds per square inch:", round(pressure_psi, 2))
# print("Pressure in millimeters of mercury:", round(pressure_mmhg, 2))
# print("Pressure in atmospheres:", round(pressure_atm, 2))
# 31 sum of digits seperated by index []
# num = input("Enter a four-digit integer: ")

# # Convert the string to individual digits and add them together
# sum_of_digits = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])

# # Display the sum of the digits
# print("The sum of the digits is:", sum_of_digits)

# 32
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# minimum = min(num1, num2, num3)
# maximum = max(num1, num2, num3)
# middle = (num1 + num2 + num3) - minimum - maximum

# print("The sorted numbers are:", minimum, middle, maximum)

# # 33 day ols bread
# num_loaves = int(input("Enter the number of loaves: "))

# regular_price = num_loaves * 3.49
# discount_price = regular_price * 0.6
# total_price = regular_price - discount_price

# print(f"Discount Price: ${discount_price:6.2f}")
# print(f"regular price: ${regular_price:6.2f}")
# print(f"total price: ${total_price:6.2f}")

# DNA = "ACGTGCGTTAC"

# print(DNA.count("A"))
# print(DNA.count("C"))
# print(DNA.count("G"))
# print(DNA.count("T"))

# # 3-1
# names = ["John", "Mary", "Jane"]
# for name in names:
#     print(name)

# # 3-2
# for name in names:
#     print('hello ' + name + ' we are the beings of light')

# # 3-3
# transportation = ["car", "plane", "bus", "train"]
# print('i like to take the ' + transportation[0])
# print('i like to take the ' + transportation[1])
# print('i like to take the ' + transportation[2])
# print('i like to take the ' + transportation[3])


# 3-4
# guest_list = ['nikola tesla', 'elon musk', 'juice wrld']
# for guest_name in guest_list:
#     print('Hello ' + guest_name.upper() + ' youve been invited to the world meeting with lorenzo ')


# 3-5
# guest_list1 = ['tom', 'jerry', 'jimmy', 'jane', 'jess', 'amandra']

# print(guest_list1[0] + ' invited')
# guest_list1[1] = guest_list1[0]
# print(guest_list1[1] + ' not invited')

# guest_list1[2] = guest_list1[0]
# print(guest_list1[2] + ' not invited')
# print(guest_list1[3] + ' invited')

# guest_list1[4] = guest_list1[0]
# print(guest_list1[4] + ' not invited')
# print(guest_list1[5] + ' invited')

# APPENDS THANK YOU MILES!!!!!!!@@@@@@AA@@@ USE Arrays
# THEN USE FOR LOOP
# guest_list_finale = []
# guest_list_finale.append(guest_list1[0])
# guest_list_finale.append(guest_list1[3])
# guest_list_finale.append(guest_list1[5])


# for guest_list_fl in guest_list_finale:
#     print(guest_list_fl +
#           ' ---- Congrats you have been invited to the world meeting with lorenzo ')


# 3-6
# guest_list1 = ['jearad', 'jimmy', 'sarah', 'katy', 'jess', 'amandra']

# for guest_name in guest_list1:
#     print(guest_name + ' Open Tables for world meeting')

# guest_list1.insert(2, 'sam')
# print(guest_list1)

# guest_list1.insert(4, "Hailey")
# print(guest_list1)


# guest_list1.append('stephanie')
# print(guest_list1)

# for guest_name in guest_list1:
#     print(guest_name + ' Open Tables for world meeting please email for +plus ones')


# 3-7

# guest_list1 = ['jearad', 'jimmy', 'sarah', 'katy', 'jess', 'amandra']

# # for guest_name in guest_list1:
# #     print(guest_name + ' sorry we only have room for TWO people on this list')


# removed_list = []
# removed_list.append(guest_list1[0:4])

# print(removed_list)

# Finale_inv = guest_list1[4:6]
# for x in Finale_inv:
#     print(x + ' has been invited to the world meeting with lorenzo')
# print(Finale_inv)


# del Finale_inv
# Finally_inv = None

# print(Finale_inv)


# 3-8


# Vaca_location = ['Vaca', 'São Paulo', 'Rio de Janeiro', 'Brazil', 'Italy']

# print(Vaca_location)
# print(sorted(Vaca_location))
# print(Vaca_location)


# print(sorted(Vaca_location, reverse=True))


# 3-9
# guest_list1 = ['jearad', 'jimmy', 'sarah', 'katy', 'jess', 'amandra']
# inv_list = guest_list1[4:6]
# print(inv_list)
# print(len(inv_list))

# list_index = str(inv_list)
# print('you are inviting ' + list_index +
#       ' people to the world meeting with lorenzo')


# 3-10
# every function


# 3-11
# index error


# 4-1
# pizzas = ['pepperoni', 'bacon', 'cbr']

# for pizza in pizzas:
#     print(pizza + ' is a great pizza')
#     print('i like pizza my guy')

# 4-2

# birds = ['eagle', 'flamingo', 'owl']

# for bird in birds:
#     print('A ' + bird + ' would make a great trained hunting bird')


# 4-3
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in x:
#     print(i)


# For x in Range Loop
# for x in range(0, 21):
#     print(x)


# 4-4 / 4-5 create a LIST Element And find the values of that element
# numbers = list(range(1000001))

# max_mili = max(numbers)
# min_mili = min(numbers)

# print(str(max_mili) + ' max value')
# print('min value ' + str(min_mili))

# 4-6 count to twenty by 3
# third = 20
# for i in range(0, third, 3):
#     print(i)


# 4-7 How do i print to a list

# X = 30

# for num in range(0, X, 3):
#     print(num)

# how to count by 3 and print in a list
# x = list(range(0, 21, 3))
# print(x)


# 4-8 range to the third power
# x = 20
# for i in range(0, x):
#     print(i**3)


# 4-9 Array with a for loop for every number raised to the third
# Numbers = [i**3 for i in range(1, 11)]
# print(Numbers)


# 4-10
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# F_three = x[0:3]
# M_three = x[4:6]
# L_three = x[8:10]

# print(F_three)
# print(M_three)
# print(L_three)


# 4-11
# pizzas = ['pepperoni', 'bacon', 'cbr']
# friends_pizzas = ['pepperoni', 'cheese', 'chichen alfredo', 'bbq chicken']

# pizzas.insert(0, 'cheese')
# friends_pizzas.insert(0, 'upside down')

# for x in pizzas:
#     print(x + 'are my favorite')

# for L in friends_pizzas:
#     print(L + ' are your favorite')


# 4-12
# done

# 5-8
# check if word has admin in it
# users = ['admin-john', 'janet', 'Bill', 'admin-hailey', 'julia', 'admin-renzo']

# for x in users:
#     if x.startswith('admin'):
#         print(x)

# for x in users:
#     if 'admin' in x:
#         print(x)


# 5-9
# empty = []
# if empty == [] or empty:
#     print('empty we need employees')


# 5-10
# current_user = ['renzo', 'katie', 'john', 'stephanie', 'frendrick', 'amy']
# new_user = ['renzo', 'john', 'sam', 'susan', 'julia']

# for x in current_user:
#     if x in new_user:
#         print(x+'name is not availabe')
#     else:
#         print(x+'name is availabe')

# 5-11


# num = range(10)


# for x in num:
#     if x >= 4:
#         print(str(x)+'th')
#     elif x >= 3:
#         print(str(x) + 'rd')
#     elif x >= 2:
#         print(str(x) + 'nd')
#     else:
#         print(str(x)+'stttt lol')

# exercise 104 - 108
# exercise 54 - 60
# exercise 71 - 75
# # workbook 104 - 108

# order_list = []
# order = int(input("Please enter a number: "))
# order_list.append(order)
# while order != 0:
#     order = int(input("Please enter another number (ends when 0 is entered): "))
#     if order != 0:
#         order_list.append(order)
# order_list.sort()
# print(order_list)

# reverse_order_list = []
# reverse_order = int(input("Please enter a number: "))
# reverse_order_list.append(reverse_order)
# while reverse_order != 0:
#     reverse_order = int(input("Please enter another number (ends when 0 is entered): "))
#     if reverse_order != 0:
#         reverse_order_list.append(reverse_order)
# reverse_order_list.sort(reverse=True)
# print(reverse_order_list)

# def outlier(array, n):
#     new_list = array
#     del new_list[len(new_list)-n:len(new_list)]
#     del new_list[0:n]
#     return new_list

# outlier_list = []
# outliers = int(input("Enter a number: "))
# outlier_list.append(outliers)
# while outliers != 0:
#     outliers = int(input("Enter another number(Ends when 0 is entered): "))
#     outlier_list.append(outliers)

# if len(outlier_list) < 4:
#     print("Please enter 4 or more values")
# else:
#     print(outlier(outlier_list, 2))

# words = []
# word = input("Please enter any word: ")
# words.append(word)
# repeat_word = []
# while len(word) != 0:
#     word = input("Please enter another word(ends when line is blank: ")
#     if len(word) != 0:
#         words.append(word)

# for i in words:
#     if i not in repeat_word:
#         print(i)
#         repeat_word.append(i)

# integers = []
# ints = input("Enter any integer: ")
# integers.append(int(ints))
# while len(ints) != 0:
#     ints = input("Enter any integer(ends when nothing entered: ")
#     if len(ints) != 0:
#         integers.append(int(ints))
# for i in integers:
#     if i < 0:
#         print(i)
# for i in integers:
#     if i == 0:
#         print(i)
# for i in integers:
#     if i > 0:
#         print(i)


# # workbook 54 - 60
# wavelength = float(input("Enter a wavelength: "))
# if 380 <= wavelength < 450:
#     print(f'{wavelength} is violet')
# elif 450 <= wavelength < 495:
#     print(f'{wavelength} is blue')
# elif 495 <= wavelength < 570:
#     print(f'{wavelength} is green')
# elif 570 <= wavelength < 590:
#     print(f'{wavelength} is yellow')
# elif 590 <= wavelength < 620:
#     print(f'{wavelength} is orange')
# elif 620 <= wavelength <= 750:
#     print(f'{wavelength} is yellow')
# else:
#     print(f'{wavelength} is outside visible spectrum')

# rad_freq= float(input("Enter a radiation frequency: "))
# if rad_freq < 3 * (10**9):
#     print(f'{rad_freq} is radio waves')
# elif 3 * (10**9) <= rad_freq < 3 * (10**12):
#     print(f'{rad_freq} is microwaves')
# elif 3 * (10**12) <= rad_freq < 4.3 * (10**14):
#     print(f'{rad_freq} is infrared light')
# elif 4.3 * (10**14) <= rad_freq < 7.5 * (10**14):
#     print(f'{rad_freq} is visible light')
# elif 7.5 * (10**14) <= rad_freq < 3 * (10**17):
#     print(f'{rad_freq} is ultraviolet light')
# elif 3 * (10**17) <= rad_freq <= 3 * (10**19):
#     print(f'{rad_freq} is x-rays')
# else:
#     print(f'{rad_freq} is gamma rays')

# total_minutes = int(input("Enter total number of call minutes: "))
# total_messages = int(input("Enter total number of messages: "))
# extra_minutes = 0
# extra_messages = 0
# print('Base Charge: $15.00')
# if total_minutes > 50:
#     extra_minutes = (total_minutes-50) * .25
#     print(f'Extra Minutes: ${extra_minutes}')
# if total_messages > 50:
#     extra_messages = (total_messages - 50) * .15
#     print(f'Extra Messages: ${extra_messages}')
# print("911 Fee: $.44")
# subtotal = 15 + extra_minutes + extra_messages + .44
# tax = round((subtotal * .05),2)
# print(f'Tax: ${tax}')
# print(f'Total: ${subtotal + tax}')

# year = int(input("Enter a year: "))
# if year % 400 == 0:
#     print(f'{year} is a leap year')
# elif year % 100 == 0:
#     print(f'{year} is not a leap year')
# elif year % 4 == 0:
#     print(f'{year} is a leap year')
# else:
#     print(f'{year} is not a leap year')

# plate = input("Enter a licence plate: ")
# if len(plate) == 6:
#     if type(plate[0:3]) is str:
#         if plate[0:3] == plate[0:3].upper() and type(plate[3:7] is int):
#             print(f'{plate} is a valid style of licence plate')
#         else:
#             print(f'{plate} is not a valid style of licence plate')
# elif len(plate) == 6:
#     if type(plate[0:4]) is int:
#         if plate[4:8] == plate[4:8].upper():
#             print(f'{plate} is a valid style of licence plate')
#         else:
#             print(f'{plate} is not a valid style of licence plate')
# else:
#     print(f'{plate} is not a valid style of licence plate')

# import random
# randnum = str(random.randint(0, 36))
# red = ['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36']
# if randnum == "0":
#     split = random.randint(1, 2)
#     if split == 1:
#         randnum = "0"
#     else:
#         randnum = "00"
# print(f'The spin resulted in {randnum}')
# if randnum == "0" or randnum == "00":
#      print(f'pay {randnum}')
# else:
#     print(f'pay {randnum}')
#     if randnum in red:
#         print(f'pay red')
#     else:
#         print(f'pay black')

#     if int(randnum) % 2 == 0:
#         print(f'pay even')
#     else:
#         print(f'pay odd')

#     if int(randnum) < 19:
#         print('pay 1 - 18')
#     else:
#         print('pay 19 - 36')

# x = int(input("Enter a number"))
# guess = x/2
# while abs(guess) <= 10**-12:
#     guess = x/guess
# print(f'approximate sqrt of {x} is {guess}')

# pali = input("Enter a word")
# if pali == pali[::-1]:
#     print(f'{pali} is a palindrome')

# multi_pali = input("Enter a word")
# space_pali = multi_pali.replace(" ", "")
# if space_pali == space_pali[::-1]:
#     print(f'{multi_pali} is a multi-palindrome')

# table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("", end='  ')
# for i in table:
#     if i != 10:
#         print(i, end=' ')
#     else:
#         print(i)
# for i in table:
#     print(i, end=' ')
#     for j in table:
#         if j != 10:
#             print(i * j, end=' ')
#         else:
#             print(i * j)

# m = int(input("enter a number"))
# n = int(input("enter a number"))
# d = min(m, n)
# while m % d != 0 or n % d != 0:
#     d -= 1
# print(f'{d} is the greatest common factor of {m} and {n}')

# lorenzo smith
# # 8-1
# def display_message():
#     print('!in lecture 4 we learned about passing list and importing function!')


# display_message()


# # 8-2
# def favorite_book(Title):
#     print('my favorite book is ' + Title + 'too!!!')


# favorite_book(Title=input('Favorite Book'))


# # 8-3

# cust_message = input("what message do you want on your shirt:?")
# size = input("what size do you want")


# def make_shirt():
#     print('the message on the shirt is ' + '"'+cust_message+'"')
#     print('the size is ' + size)


# make_shirt()

# # --positional
# def make_shirt(cust_message, size):
#     print('the message on the shirt is ' + '"'+cust_message+'"')
#     print('the size is ' + size)

#

# make_shirt("i like cake", "XL")

# -- keyword
# def make_shirt(cust_message, size):
#     print('the message on the shirt is ' + '"'+cust_message+'"')
#     print('the size is ' + size)


# make_shirt(cust_message="party like a rock star", size="small")


# def greet(name, message="Hello"):
#     print(f"{message}, {name}!")

# # Calling the greet() function without specifying the 'message' argument
# greet("Alice")  # prints "Hello, Alice!"

# # Calling the greet() function with a different 'message' argument
# greet("Bob", message="Hi")  # prints "Hi, Bob!"


# # 8-4
# def making_shirt(message="i love python", size="large"):
#     if size == "small":
#         print("your message is " + '"' + message + '"' + "skinny banana")
#     elif size == "large":
#         print("your message is " + '"' + message +
#               '"' + " your size is " + size)
#     elif size == "medium":
#         print("your message is " + '"' + message +
#               '"' + " your size is " + size)


# making_shirt()


# # 8-4.2
# def making_shirt(message, size="large"):
#     if size == "small":
#         print("your message is " + '"' + message + '"' + size + "skinny banana")
#     elif size == "large":
#         print("your message is " + '"' + message +
#               '"' + " your size is " + size)
#     elif size == "medium":
#         print("your message is " + '"' + message +
#               '"' + " your size is " + size)


# making_shirt("i love python", size="small")


# # 8-5 Cant set default

# city = input("name of you city please:")
# country = input("country name please:")


# def describe_city(city, country):

#     print("you in live in " + city + " city " +
#           " which is in the country " + country)


# describe_city(city, country)


# # 8-6
# def city_country(city_name, country):
#     print('"' + city_name + ',' + country + '"')


# city_country("Santiago", " Chile")
# city_country("Paris", " France")
# city_country("Tokyo", " Japan")


# # # 8-9


# # magician = ["John", "mary", "jose", "catrina"]

# def call_magician():
#     for artist in magician:
#         print(artist)


# call_magician()

# # ex2


# def show_magicians(magicians):
#     """
#     This function takes a list of magician names and prints each name.
#     """
#     for magician in magicians:
#         print(magician)


# magicians = ['Harry Houdini', 'David Blaine', 'Criss Angel', 'Penn & Teller']
# show_magicians(magicians)


# # 8-10 repeats itself
# def show_magicians(magicians):
#     """
#     This function takes a list of magician names and prints each name.
#     """
#     for magician in magicians:
#         print(magician)


# def make_great(magicians):
#     """
#     This function modifies the list of magicians by adding "the Great" to each name.
#     """
#     for i in range(len(magicians)):
#         magicians[i] = "the Great " + magicians[i]


# magicians = ['Harry Houdini', 'David Blaine', 'Criss Angel', 'Penn & Teller']
# make_great(magicians)
# show_magicians(magicians)


# # 8-11  wow

# def show_magicians(magicians):
#     """
#     This function takes a list of magician names and prints each name.
#     """
#     for magician in magicians:
#         print(magician)

# def make_great(magicians):
#     """
#     This function modifies the list of magicians by adding "the Great" to each name.
#     """
#     for i in range(len(magicians)):
#         magicians[i] = "the Great " + magicians[i]
#     return magicians

# magicians = ['Harry Houdini', 'David Blaine', 'Criss Angel', 'Penn & Teller']

# # Make a copy of the list of magicians and pass it to make_great()
# great_magicians = make_great(magicians[:])

# # Print the original list and the modified list
# print("Original Magicians:")
# show_magicians(magicians)

# print("\nGreat Magicians:")
# show_magicians(great_magicians)


# # 8-12


# def make_sandwitch(toppings):
#     print("your sandwitch ingrediants are ")

#     for topping in toppings:

#         print(topping)


# make_sandwitch(toppings=['bread', 'lettuce', 'mustard'])
# make_sandwitch(toppings=['cheese', 'mayo', 'ham'])
# make_sandwitch(toppings=['turkey', 'ketchup', 'tomato'])


# 8-15 & 8-16 returns butts ive kicked twice why?
# from exercise_4_import_function_file import kicking_butt

# kicking_butt("miami", "PA", "dubai")

# 8-16


# book exercise

# # 81.
# A = float(input("Enter first side of a triangle:"))
# B = float(input("Enter second side of a triangle"))


# def find_hypotenuse(A,B):
#     C = (A**2 + B**2)/2

#     print(C)


# find_hypotenuse(A, B)


# # 82.
# def calculate_taxi_fare(distance_in_km):
#     base_fare = 4.00
#     distance_in_meters = distance_in_km * 1000
#     additional_fare_per_meter = 0.25 / 140
#     additional_fare = distance_in_meters * additional_fare_per_meter
#     total_fare = base_fare + additional_fare
#     return total_fare
# # 83.
# # def calc_shipping(number_shipped):
# #     first_buy = 10.95
# #     next_buy = 2.95


# def calculate_shipping_charge(num_items):
#     if num_items == 1:
#         return 10.95
#     else:
#         return 10.95 + (num_items - 1) * 2.95


# num_items = int(input("Enter the number of items in your order: "))
# shipping_charge = calculate_shipping_charge(num_items)
# print("Your shipping charge is: $%.2f" % shipping_charge)

# # 84.
# number1 = int(input("Enter the number "))
# number2 = int(input("Enter the number"))
# number3 = int(input("Enter the number"))


# def finding_median(number1, number2, number3):
#     nums = [number1, number2, number3]
#     nums.sort()
#     return nums[1]


# find_median_action = finding_median(number1, number2, number3)
# print('your median of those three numbers is', str(find_median_action))

# # 85.
# def ordinal_number(num):
#     if num == 1:
#         return "1st"
#     elif num == 2:
#         return "2nd"
#     elif num == 3:
#         return "3rd"
#     elif 4 <= num <= 12:
#         return str(num) + "th"
#     else:
#         return ""


# if __name__ == "__main__":
#     for i in range(1, 13):
#         print(f"{i}: {ordinal_number(i)}")

# # 86.
# def print_verse(verse_num):
#     gifts = [
#         "A partridge in a pear tree.",
#         "Two turtle doves,",
#         "Three French hens,",
#         "Four calling birds,",
#         "Five golden rings,",
#         "Six geese a-laying,",
#         "Seven swans a-swimming,",
#         "Eight maids a-milking,",
#         "Nine ladies dancing,",
#         "Ten lords a-leaping,",
#         "Eleven pipers piping,",
#         "Twelve drummers drumming,"
#     ]
#     days = [
#         "first", "second", "third", "fourth", "fifth", "sixth",
#         "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
#     ]
#     print(f"On the {days[verse_num-1]} day of Christmas")
#     print("my true love sent to me:")
#     for i in range(verse_num-1, -1, -1):
#         if i == 0 and verse_num != 1:
#             print("and", end=" ")
#         print(gifts[i])
#     print()


# for i in range(1, 13):
#     print_verse(i)


# 87.
# def center_text(text, width):
#     if len(text) >= width:
#         return text
#     else:
#         num_spaces = (width - len(text)) // 2
#         return ' ' * num_spaces + text

# if __name__ == '__main__':
#     text = 'Hello, world!'
#     width = 30
#     centered_text = center_text(text, width)
#     print(centered_text)

# # 88.
# def is_triangle(a, b, c):
#     """
#     Determine if three lengths can form a triangle.

#     Return True if they can form a triangle, and False otherwise.
#     """
#     if a >= b + c or b >= a + c or c >= a + b:
#         return False
#     else:
#         return True


# # Read the input lengths from the user
# a = float(input("Enter the length of the first side: "))
# b = float(input("Enter the length of the second side: "))
# c = float(input("Enter the length of the third side: "))

# # Determine if they can form a triangle
# if is_triangle(a, b, c):
#     print("These lengths can form a triangle.")
# else:
#     print("These lengths cannot form a triangle.")

# # 89.
# def capitalize_string(s):
#     # Capitalize first letter of string
#     s = s.capitalize()

#     # Capitalize 'i' when preceded and followed by a space
#     s = s.replace(' i ', ' I ')

#     # Capitalize first non-space character after ., ! or ?
#     for p in '.!?':
#         s = s.replace(p + ' ' + s[s.index(p)+2], p +
#                       ' ' + s[s.index(p)+2].upper())

#     return s


# # Test the function with user input
# user_input = input("Enter a string: ")
# capitalized = capitalize_string(user_input)
# print(capitalized)
# # This function capitalize_string takes a string s as input and returns a


# # 90.
# def isInteger(s):
#     """Returns True if s represents an integer, False otherwise."""
#     s = s.strip()  # Remove leading and trailing white space
#     if len(s) == 0:
#         return False  # Empty string is not an integer
#     if s[0] in '+-':
#         return s[1:].isdigit()  # Check if remaining characters are digits
#     else:
#         return s.isdigit()  # Check if all characters are digits

# def main():
#     s = input("Enter a string: ")
#     if isInteger(s):
#         print("The string represents an integer.")
#     else:
#         print("The string does not represent an integer.")

# if __name__ == '__main__':
#     main()
# # 91.
# def precedence(operator):
#     if operator in ['+', '-']:
#         return 1
#     elif operator in ['*', '/']:
#         return 2
#     elif operator == '^':
#         return 3
#     else:
#         return -1

# if __name__ == '__main__':
#     operator = input('Enter an operator (+, -, *, /, ^): ')
#     p = precedence(operator)
#     if p == -1:
#         print('Error: Not a valid operator')
#     else:
#         print(f'The precedence of {operator} is {p}')

# # 92.
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# if __name__ == '__main__':
#     n = int(input("Enter a number: "))
#     if is_prime(n):
#         print(f"{n} is a prime number.")
#     else:
#         print(f"{n} is not a prime number.")

# # 93.
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def next_prime(n):
#     next_num = n + 1
#     while True:
#         if is_prime(next_num):
#             return next_num
#         next_num += 1

# if __name__ == '__main__':
#     n = int(input("Enter a number: "))
#     next_p = next_prime(n)
#     print(f"The next prime number after {n} is {next_p}.")

# # 94.
# import random

# def generate_password():
#     length = random.randint(7, 10)
#     password = ''
#     for i in range(length):
#         password += chr(random.randint(33, 126))
#     return password

# if __name__ == '__main__':
#     password = generate_password()
#     print(f"Your random password is: {password}")

# # 95.
# import random

# def generate_license_plate():
#     if random.random() < 0.5:  # 50/50 chance of old or new license plate format
#         letters = ''.join([chr(random.randint(65, 90)) for i in range(3)])
#         numbers = ''.join([str(random.randint(0, 9)) for i in range(3)])
#         return f"{letters}{numbers}"
#     else:
#         numbers = ''.join([str(random.randint(0, 9)) for i in range(4)])
#         letters = ''.join([chr(random.randint(65, 90)) for i in range(3)])
#         return f"{numbers}{letters}"

# if __name__ == '__main__':
#     license_plate = generate_license_plate()
#     print(f"Your random license plate is: {license_plate}")

# # 96.
# def is_good_password(password):
#     has_digit = False
#     has_lowercase = False
#     has_uppercase = False

#     if len(password) < 8:
#         return False

#     for char in password:
#         if char.isdigit():
#             has_digit = True
#         elif char.islower():
#             has_lowercase = True
#         elif char.isupper():
#             has_uppercase = True

#     return has_digit and has_lowercase and has_uppercase

# def main():
#     password = input("Enter a password: ")
#     if is_good_password(password):
#         print("Good password")
#     else:
#         print("Bad password")

# if __name__ == '__main__':
#     main()


# # 97.

# import random
# import string
# from exercise_94 import has_digit, has_lowercase, has_uppercase
# from exercise_96 import is_long_enough

# def generate_password():
#     while True:
#         password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
#         if has_digit(password) and has_lowercase(password) and has_uppercase(password) and is_long_enough(password):
#             return password

# def main():
#     attempts = 0
#     while True:
#         password = generate_password()
#         attempts += 1
#         if password:
#             print(f"Generated password: {password}")
#             print(f"Number of attempts: {attempts}")
#             break

# if __name__ == '__main__':
#     main()

# #  98.
# def hex2int(hex_digit):
#     """Converts a hexadecimal digit to a base 10 integer"""
#     if hex_digit.isdigit():
#         return int(hex_digit)
#     elif hex_digit.upper() in 'ABCDEF':
#         return ord(hex_digit.upper()) - 55
#     else:
#         print('Error: Invalid hexadecimal digit')
#         exit()

# def int2hex(integer):
#     """Converts an integer between 0 and 15 to a single hexadecimal digit"""
#     if 0 <= integer <= 9:
#         return str(integer)
#     elif 10 <= integer <= 15:
#         return chr(integer + 55)
#     else:
#         print('Error: Invalid integer')
#         exit()

# 99.
# def convert_to_base_10(number, base):
#     decimal = 0
#     power = 0
#     digits = "0123456789ABCDEF"
#     for digit in reversed(number):
#         value = digits.index(digit.upper())
#         decimal += value * base ** power
#         power += 1
#     return decimal


# def convert_from_base_10(decimal, base):
#     if decimal == 0:
#         return "0"
#     digits = []
#     digits_str = "0123456789ABCDEF"
#     while decimal > 0:
#         remainder = decimal % base
#         digits.append(digits_str[remainder])
#         decimal //= base
#     digits.reverse()
#     return "".join(digits)


# def base_conversion():
#     input_base = int(input("Enter the input base (2-16): "))
#     if input_base < 2 or input_base > 16:
#         print("Error: Input base must be between 2 and 16.")
#         return
#     output_base = int(input("Enter the output base (2-16): "))
#     if output_base < 2 or output_base > 16:
#         print("Error: Output base must be between 2 and 16.")
#         return
#     number = input(f"Enter the number in base {input_base}: ")
#     decimal = convert_to_base_10(number, input_base)
#     result = convert_from_base_10(decimal, output_base)
#     print(f"{number} in base {input_base} is {result} in base {output_base}.")


# base_conversion()

# Enter the number: 1011
# Enter the base of the input number: 2
# Enter the base of the result number: 16
# 1011 in base 2 is B in base 16

# 100


# # 101
# def reduce_fraction(numerator, denominator):
#     # Find the greatest common divisor of numerator and denominator
#     # using Euclid's algorithm
#     a = numerator
#     b = denominator
#     while b != 0:
#         t = b
#         b = a % b
#         a = t

#     # a now contains the greatest common divisor
#     # Divide both numerator and denominator by the gcd to get the reduced fraction
#     reduced_num = numerator // a
#     reduced_denom = denominator // a

#     return reduced_num, reduced_denom


# # Main program
# num = int(input("Enter the numerator: "))
# denom = int(input("Enter the denominator: "))

# reduced_num, reduced_denom = reduce_fraction(num, denom)

# print(
#     f"The reduced fraction of {num}/{denom} is: {reduced_num}/{reduced_denom}")


# 102
# def convert_volume(num, unit):
#     if unit == 'teaspoon':
#         if num >= 3 * 4 * 4:
#             cups = num // (3 * 4 * 4)
#             num %= 3 * 4 * 4
#             return f'{cups} cup' + ('s' if cups > 1 else '') + (f' {num} teaspoon' + ('s' if num > 1 else '') if num > 0 else '')
#         elif num >= 3 * 4:
#             tablespoons = num // (3 * 4)
#             num %= 3 * 4
#             return f'{tablespoons} tablespoon' + ('s' if tablespoons > 1 else '') + (f' {num} teaspoon' + ('s' if num > 1 else '') if num > 0 else '')
#         else:
#             return f'{num} teaspoon' + ('s' if num > 1 else '')
#     elif unit == 'tablespoon':
#         if num >= 16:
#             cups = num // 16
#             num %= 16
#             return f'{cups} cup' + ('s' if cups > 1 else '') + (f' {num} tablespoon' + ('s' if num > 1 else '') if num > 0 else '')
#         else:
#             return f'{num} tablespoon' + ('s' if num > 1 else '')
#     else:
#         return f'{num} cup' + ('s' if num > 1 else '')
# # 103
# def is_magic_date(day, month, year):
#     two_digit_year = year % 100
#     return day * month == two_digit_year


# if __name__ == '__main__':
#     for year in range(1900, 2000):
#         for month in range(1, 13):
#             for day in range(1, 32):
#                 if is_magic_date(day, month, year):
#                     print(f'{month}/{day}/{year:02}')
