restaurant = {
  "name": "Saurabh",
  "city": "Varanasi",
  "rating": 5,
  "menu": ["Chhola-Bhatura", "Dosa", "Idli", "Namkeen"],
  "is_open": True
}

for key,value in restaurant.items():
   print(f"{key} : {value}")

restaurant["menu"].append("Sambhar")

restaurant["rating"] = 4

restaurant["is_open"] = False

for key,value in restaurant.items():
   print(f"{key} : {value}")
   