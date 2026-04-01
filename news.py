from bs4 import BeautifulSoup
from operator import attrgetter
import requests

class Article:
    def __init__(self, title, link, upvotes):
        self.title = title
        self.link = link
        self.upvotes = upvotes

# Scrape site for desired data
response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all(class_="storylink")
article_upvotes = soup.find_all(class_="score")

# Create list of refined article data
refined_articles = []
for i, article in enumerate(articles):
    title = article.get_text()
    link = article["href"]
    # Convert upvote strings to usable ints
    upvotes = int(article_upvotes[i].get_text().split(" ")[0])

    refined_article = Article(title, link, upvotes)

    refined_articles.append(refined_article)

most_upvoted_article = max(refined_articles, key=attrgetter("upvotes"))
print(most_upvoted_article.title)
print(most_upvoted_article.link)
