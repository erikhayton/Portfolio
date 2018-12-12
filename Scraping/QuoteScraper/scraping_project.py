# http://quotes.toscrape.com
import requests # makes a request to URL
from csv import writer # allows you to write to a file using csv
from bs4 import BeautifulSoup # allows you to use Beautiful Soup for scraping
from time import sleep

all_quotes = []
base_url = "http://quotes.toscrape.com"
url = "/page/1"

while url:
    response = requests.get(f"{base_url}{url}")
    print(f"Now Scraping {base_url}{url}.....")
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all(class_="quote")
    # print(quotes) # run this to see if it's working (always run print for each step)

    for quote in quotes: # loop through quotes
        all_quotes.append({
            "text":quote.find(class_="text").get_text(),
            "author":quote.find(class_="author").get_text(),
            "bio-link":quote.find("a")["href"]
        })

    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None
    # sleep(2)

print(all_quotes)

# with open("blog_data.csv", "w") as csv_file:
#     csv_writer = writer(csv_file)
#     csv_writer.writerow(["title", "link", "date"])

#     for article in articles:
#         a_tag = article.find("a")
#         title = a_tag.get_text()
#         url = a_tag['href']
#         date = article.find("time")["datetime"]
#         csv_writer.writerow([title, url, date])
