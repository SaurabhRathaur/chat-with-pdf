"""movie = {
    "title": "Inception",
    "rating": 8.7,
    "genre": ["Action", "Thriller", "Horror"],
    "available_seats": 25,
    "is_housefull": False
}

for key,value in movie.items():
    print(f"{key} : {value}")
    
seats_needed = int(input("How many seats do you need: "))

if seats_needed > movie["available_seats"]:
   print("Itni seats available nahi!")
else:
   print("Booking confirmed!")
   movie["available_seats"] = movie["available_seats"] - seats_needed

if movie["available_seats"] == 0:
    movie["is_housefull"] = True
    movie["genre"].append("Blockbuster")
    
for key,value in movie.items():
    print(f"{key} : {value}")"""

"""with open("notes.txt", "w") as file:
    file.write("My name is Saurabh\n")
    file.write("I am learning AI\n")
    file.write("I belong to Varanasi\n")

print("I have written the file")"""

"""
with open("notes.txt", "r") as file:
  content = file.read()

print(content)"""

with open("notes.txt", "a") as file: 
  
  file.write("And There is more about me\n")
  file.write("I am here to stay\n")

print("File is final now")

with open("notes.txt", "r") as file:
  
  content = file.read()

  print(content)

 