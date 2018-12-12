# https://www.rithmschool.com/blog
import requests # makes a request to URL
from csv import writer # allows you to write to a file using csv
from bs4 import BeautifulSoup # allows you to use Beautiful Soup for scraping

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
#print(articles) # run this to see if it's working (always run print for each step)

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])

    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])
