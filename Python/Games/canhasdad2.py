# import requests
# import random
# search = input("What would you like to hear a joke about? ")
# url_root = "https://icanhazdadjoke.com/search?term="
# url = url_root + search

# # if topic - return "I've got # of jokes about topic. Here's one: #"

# print(url)

# response = requests.get(url)
# print(response.text)

import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKEATRON V2.1.4")
header = colored(header, color="blue")
print(header)

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term":user_input}
    ).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about '{user_input}'. Here's one: ")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"I found {num_jokes} joke about '{user_input}'. Here's one: ")
    print(results[0]['joke'])
else:
    print(f"SORRY, THERE ARE NO JOKES CONTAINING {user_input}")