# http://quotes.toscrape.com
import requests # makes a request to URL
from bs4 import BeautifulSoup # allows you to use Beautiful Soup for scraping
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com"

def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

def start_game(quotes):

    quote = choice(quotes)
    rem_guesses = 4
    print("Here's a quote: ")
    print(quote["text"])
    guess = ''
    while guess.lower() != quote["author"].lower() and rem_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining: {rem_guesses}\n")
        if guess.lower() == quote["author"].lower():
            print("CORRECT!")
            break
        rem_guesses -= 1
        if rem_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here'a a hint: The author was born on {birth_date}  {birth_place}")
        elif rem_guesses == 2:
            print(f"Here'a a hint: The author's first name starts with: {quote['author'][0]}")
        elif rem_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here'a a hint: The author's last name starts with: {last_initial}")
        else:
            print(f"Sorry you ran out of guesses. The answer was {quote['author']}")



    again = ''
    while again not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)?")
    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print("Fine! Bye Then!")
quotes = read_quotes("quotes.csv")
start_game(quotes)

# with open("blog_data.csv", "w") as csv_file:
#     csv_writer = writer(csv_file)
#     csv_writer.writerow(["title", "link", "date"])

#     for article in articles:
#         a_tag = article.find("a")
#         title = a_tag.get_text()
#         url = a_tag['href']
#         date = article.find("time")["datetime"]
#         csv_writer.writerow([title, url, date])
