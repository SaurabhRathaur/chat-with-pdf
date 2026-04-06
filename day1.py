"""
age = int(input("Come on handsome, tell me your age: "))

if age>18:
  print("You are really mature handsome")
elif age<=2:
  print("Baby, where is your dada")
else:
  print("Go and study")
  """

"""
numbers = [1,2,3,4,5]

for number in numbers:
  print(f"The cube of {number} is {number*number*number}")"""

"""def calculate_cube(number):
    print(f"Cube of the {number} is {number*number*number}")

calculate_cube(5)
calculate_cube(15)
calculate_cube(25)"""


"""def check_age(name, age):
    if age < 18:
        print(f"{name}, you are too young!")
    else:
        print(f"{name}, you can vote!")

for i in range(3):
    name = input("What is your name: ")
    age = int(input("What is your age: "))
    check_age(name, age)"""

def movie_entry():
    name = input("Tell me your name my Buoy: ")
    age = int(input("Tell me your age my Buoy "))

    if age<12:
        print(f"{name}, go home kid")
    elif 13<=age<=17:
        print(f"{name}, only with parents")
    else:
        print(f"{name}, you can watch!")

for i in range(4):
    movie_entry()    