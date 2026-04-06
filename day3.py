import json

"""student = {
    "name": "Saurabh",
    "age": 26,
    "city": "Gorakhpur",
    "skills": ["Python", "AI", "Freelancing"]
}

json_string = json.dumps(student)

print(json_string)
print(type(json_string))"""

"""
json_string = '{"name":"Saurabh", "age": 24, "city":"Gorakhpur"}'

student = json.loads(json_string)

print(student["name"])
print(student["age"])
print(student)
print(type(student))

for key,value in student.items():
 print(f"{key} : {value}")
"""
"""
student = {
    "name": "Saurabh",
    "age": 26,
    "city": "Gorakhpur",
    "skills": ["Python", "AI", "Freelancing"]
}

# File mein save karo
with open("student.json", "w") as file:
    json.dump(student, file)

print("File save ho gayi!")"""

"""student = {
    "name": "Saurabh",
    "age": 26,
    "city": "Gorakhpur",
    "skills": ["Python", "AI", "Freelancing"]
}

# File mein save karo
with open("student.json", "w") as file:
    json.dump(student, file)

print("File save ho gayi!")"""

"""
with open("student.json", "r") as file:
  student = json.load(file)

print(student["name"])
print(student["skills"])
print(type(student))"""

my_chatbot = {
  "name": "Ramlal",
  "version": "1.0",
  "creator": "Shyamlal",
  "features": ["Automation", "Fast", "Accuracy"] ,
  "is_active": True
}

json_string = json.dumps(my_chatbot)
print(json_string)

hello = json.loads(json_string)

with open("chatbot.json", "w") as file:
    json.dump(hello, file)

with open("chatbot.json", "r") as file:
  my_chatbot = json.load(file)

print(my_chatbot["features"])
print(my_chatbot["name"])