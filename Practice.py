class cat:
    def speak(self):
        print("meow")
        return ""

class dog:
    def speak(self):
        print("woof")

d = dog()
c = cat()
# d.speak()

animal = [c, d]
for pets in animal:
    # print(pets.speak())
    pets.speak()


# Checking codes for solution

# class Cat:
#     def speak(self):
#         print("Meow")

# c = Cat()
# c.speak()

# def speak():
#     print("meow")

# speak()

# 2nd way
class cat:
    def speak(self):
        print("meow")
        return ""

class dog:
    def speak(self):
        print("woof")
        return ""

d = dog()
c = cat()
# d.speak()

animal = [c, d]
for pets in animal:
    print(pets.speak(), end="")


# Challange Question 1
class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

class Cow:
    def speak(self):
        print("Humba")

animal = [Dog(), Cat(), Cow()]
for pet in animal:
    pet.speak()

# Challange Question 2

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        print(f"the area of circle is: {3.14 * self.radius * self.radius}")

class Square:
    def __init__(self, square):
            self.square = square
    def area(self):
        print(f"the side of square is: {self.square * self.square}")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(f"the area of rectange is: {self.length * self.width}")

cir = Circle(3)
sq = Square(2)
rc = Rectangle(2, 5)

ar = [cir, sq, rc]
for x in ar:
    x.area()