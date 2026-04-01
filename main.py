import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Scrape movie ranking data
response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

# Handle/organise movie ranking data
movie_synopses = soup.find_all(class_="article-title-description__text")

best_100_movies = [movie_synopsis.find(class_="title").get_text() for movie_synopsis in movie_synopses]

# The site ranks the movies from 100 down to 1; we want it from 1 to 100
best_100_movies.reverse()

# Save ranking to text file
with open("./movies.txt", "w", encoding='utf-8') as movie_file:
    for movie in best_100_movies:
        movie_file.write(f"{movie}\n")