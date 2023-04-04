

# # Class can be used to create real world items virtuly using Attributes/Characteristics and Methods/Action
# class Car:

#     # constructor

#     def __init__(self, make, model, year, color, odm_reading):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.odm_reading = odm_reading

#     def driver(self):
#         print('this ' + self.make + ' is driving')
# #       print('this' + self.make + 'is driving)

#     def stop(self):
#         print('this car is stopping')

#     def read_odm(self):
#         print('this car mileage is ' + str(self.odm_reading) + ' miles')

#     def update_odm(self, odm_mileage):
#         if odm_mileage >= self.odm_reading:
#             self.odm_reading = odm_mileage
#         else:
#             print("you cant roll back odometer")


# # create cars or objects need matching pair of objects
# car_1 = Car('Mclaren', 'Super Sport', '2021', 'purple', 50000)

# # Update or Modify value using a function inside of class
# # why wont it print the message?????????????
# car_1.update_odm(4000)
# car_1.read_odm()

# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)
# print('this ' + car_1.make + ' car is driving')

# car_1.driver()
# car_1.stop()


# car_2 = Car('Ferrari', 'Super Sport', '2020', 'green', 0)

# car_2.driver()
# car_2.read_odm()


# create IF statement inside function for restrictions


# inheritance
# 1.create parent class and attributes that all classes will have
# 2.create child class with new atrributes and parent attributes as well

class Animal:

    alive = True

    def eat(self):
        print("this animal is eating ")

    def sleep(self):
        print("this animal is sleeping")


class Rabbit(Animal):
    def run(self):
        print("this Rabbit is running ")


class Fish(Animal):
    def swim(self):
        print('this fish is swimming')


class Hawk(Animal):
    def fly(self):
        print('this hawk is flying')


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()


rabbit.run()
fish.swim()
hawk.fly()


# print(rabbit.alive)
# print(hawk.eat)
# print(fish.sleep)
