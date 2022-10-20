# Parent Class
class Person:
    name = "Unknown"
    email = "Unknown"

    def getInfo(self): # parent class method
        New_name = input("Your name?")
        New_email = input("Email?")

# Child Class
class Human(Person):
    age = "Unknown" 
    gender = "Unknown" 

    def getInfo(self): # polymorphism from parent class method
        New_name = input("Name?")
        New_email = input("And your email?")

# 2nd Child Class
class Robot(Person):
    year_built = "Unknown"
    function = "Unknown"

    def getInfo(self): # 2nd polymorphism from parent class method
        New_name = input("What is your serial number?")
        New_email = input("Where are your commands sent to?")
