from dotenv import load_dotenv
import os

load_dotenv()

name = os.getenv("MY_NAME")
age = os.getenv("MY_AGE")

print(f"Name: {name}")
print(f"Age: {age}")

