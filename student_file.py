"""import json

student = {
  "Name": "Saurabh",
  "Age": 24,
  "City": "Varanasi",
  "Skills": ["Automation", "Anthropic", "Claude"]
}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    json.read()"""

"""import requests

response = requests.get(
  "https://api.open-meteo.com/v1/forecast?latitude=25.4358&longitude=81.8463&current=temperature_2m"
)

data = response.json()

print(data["current"]["temperature_2m"])"""

import json

"""
student = {
    "Name": "Saurabh",
  "Age": 24,
  "City": "Varanasi",
  "Skills": ["Automation", "Anthropic", "Claude"]
}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    student = json.load(file)

print(student["Skills"])

student["Skills"].append("File Handling")

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    student = json.load(file)
    print(student)

for key, value in student.items():
    print(f"{key} is {value}")"""

"""
try:
    with open("Hey_File", "r") as file:
        content = file.read(file)
        print(content)

except FileNotFoundError:
    print("File nahi mili - check karo!")
"""
"""
try:
    with open("student.json", "r") as file:
        content = json.read(file)
        print(content)

except FileNotFoundError:
    print("File nahi mili - check karo!")
"""
"""
import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")

data = response.json()

print(data["setup"])
print(data["punchline"])"""

"""import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

headers = {
    "X-RapidAPI-Key": "d5984d4405mshc5a2921592a43a4p1a6cd6jsncc7f316bc19c",
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

data = response.json()

print(data)"""

"""import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

headers = {
  "X-RapidAPI-Key": "d5984d4405mshc5a2921592a43a4p1a6cd6jsncc7f316bc19c",
  "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

for match_type in data["typeMatches"]:
    for series in match_type["seriesMatches"]:
        if "seriesAdWrapper" in series:
            for match in series["seriesAdWrapper"]["matches"]:
                info = match["matchInfo"]
                if info["state"] == "In Progress":
                 print(f"🏏 {info['team1']['teamName']} vs {info['team2']['teamName']}")
                 print(f"Status: {info['status']}")
                 print()"""

"""import requests

response = requests.get("https://official-joke-api.appspot.com/jokes/ten")
data = response.json()

for joke in data:
    print(joke["setup"])
    print(joke["punchline"])"""

"""print(data[0])"""

'''counts = {}

for joke in data:
    t = joke["type"]
    if t in counts:
        counts[t] = counts[t] + 1
    else:
        counts[t] = 1

for type_name, count in counts.items():
    print(f"{type_name}: {count}")'''

"""
import requests

choice = input("Choose (1/2/3/4): ")

if choice == "1":
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()

    print("\n😂 Random Joke:\n")
    print(data["setup"])
    print(data["punchline"])

elif choice == "2":
    response = requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
    data = response.json()
    print("\n💻 Programming Joke:\n")
    for joke in data:
        if joke["type"] == "programming":
         print(joke["setup"])
         print(joke["punchline"])

elif choice == "3":
    response = requests.get("https://official-joke-api.appspot.com/jokes/types")
    data = response.json()

    print("\n📊 Joke Types Count:\n")
    print("Total types:", len(data))
    print("Types:", ", ".join(data))

elif choice == "4":
    print("Bye!")

else:
    print("Invalid choice ❌") """
"""
import requests

def get_random_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    print(data["setup"])
    print(data["punchline"])


def get_programming_joke():
    response = requests.get("https://official-joke-api.appspot.com/jokes/ten")
    data = response.json()
    for joke in data:
        if joke["type"] == "programming":
            print(joke["setup"])
            print(joke["punchline"])

def get_joke_types():
    response = requests.get("https://official-joke-api.appspot.com/jokes/ten")
    data = response.json()

    counts = {}
    for joke in data:
        t = joke["type"]
        if t in counts:
            counts[t] = counts[t] + 1
        else:
            counts[t] = 1

    for type_name,count in counts.items():
        print(f"{type_name}: {count}")

get_random_joke()
get_programming_joke()
get_joke_types()"""

import requests

choice = input("Choose (1/2/3/4): ")

def get_random_joke():
  
  response = requests.get("https://official-joke-api.appspot.com/random_joke")
  data = response.json()
  print(data["setup"])
  print(data["punchline"])

def get_programming_joke():
 response = requests.get("https://official-joke-api.appspot.com/jokes/ten")
 data = response.json()
 for joke in data:
        if joke["type"] == "programming":
            print(joke["setup"])
            print(joke["punchline"])

def get_joke_types():
  response = requests.get("https://official-joke-api.appspot.com/jokes/ten")
  data = response.json()
  counts = {}
  for joke in data:
     t = joke["type"]
     if t in counts:
            counts[t] = counts[t] + 1
     else:
            counts[t] = 1
     
  for type_name, count in counts.items():
        print(f"{type_name}: {count}")   

if choice == "1":
    get_random_joke()
elif choice == "2":
    get_programming_joke()
elif choice == "3":
    get_joke_types()
elif choice == "4":
    print("Bye!")

    