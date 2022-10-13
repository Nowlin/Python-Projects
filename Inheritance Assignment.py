class User: #creation of class 'User'
    name = '' #variable 'name' to store User's name
    email = '' #variable 'email' to store User's email
    password = '' #variable 'password' to store User's password

class Student(User): #variable 'Student' inherits from User, with additional variables unique to 'Student'
    ID = 0
    GPA = 3.2

class Teacher(User):
    userName = ''
    base_pay = 30.00
