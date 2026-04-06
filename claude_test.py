'''messages = []
print(messages)

messages.append({"role": "user", "content": "Mera naam Saurabh hai"})
print(messages)'''

'''messages = []
messages.append({"role": "user", "content": "Mera naam Saurabh hai"})
messages.append({"role": "assistant", "content": "Namaste Saurabh!"})
messages.append({"role": "user", "content": "Mera naam kya hai?"})
print(messages)'''

'''messages= []
messages.append({"role":"user", "content":"Mera naam Saurabh hai"})
messages.append({"role":"assistant", "content": "Namaste Saurabh!"})
messages.append({"role":"user", "content":"Mera naam kya hai?"})
messages.append({"role":"user", "content":"Acha, aur mera city?"})
print(messages)'''

'''import anthropic

client = anthropic.Anthropic(api_key="fake-key-for-now")

messages = []

messages.append({"role": "user", "content": "Mera naam Saurabh hai"})
messages.append({"role": "assistant", "content": "Namaste Saurabh!"})
messages.append({"role": "user", "content": "Mera naam kya hai?"})

print(messages)'''

'''import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

messages = [
    {"role": "user", "content": "Mera naam Saurabh hai!"}
]

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=messages
)

print(response.content)

print(response.content[0].text)
'''

import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

system = "Always Talk in English and use Jim Carrey jokes in every conversation"

messages = []

while True:
    user_input = input("Tu: ")
    messages.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model = "claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=system,
        messages=messages
    )

    reply = response.content[0].text
    messages.append({"role": "assistant", "content": reply})

    print(f"Claude: {reply}\n")