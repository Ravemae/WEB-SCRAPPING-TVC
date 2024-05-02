import requests
from bs4 import BeautifulSoup
import sqlite3
import asyncio

# Function to scrape and store data
def async scrape_and_store():
    # Connect to SQLite database
    conn = sqlite3.connect('tvc_news.db')
    c = conn.cursor()

    # Create table to store news data
    c.execute('''CREATE TABLE IF NOT EXISTS news (
                category TEXT,
                heading TEXT,
                image_url TEXT,
                link TEXT)''')

    # Base URL of TVC News website
    base_url = 'https://www.tvcnews.tv/category/'
    n = range(1, 60)

    # List of news categories
    categories = ['nigeria-news', 'world-news', 'politics', 'business', 'sport', 'entertainment', 'health', 'education']

    # Iterate over each category
    for category in categories:
        for num in n:
            url = f'{base_url}{category}/page/{num}/'

            # Fetch the webpage
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Extracting headings, images, and links
                news_items = soup.find_all('article', class_='td_module_10')

                for news_item in news_items:
                    heading = news_item.find('h3', class_='entry-title').text.strip()
                    image_url = news_item.find('img')['src']
                    link = news_item.find('a')['href']

                    # Store data in the database
                    c.execute("INSERT INTO news (category, heading, image_url, link) VALUES (?, ?, ?, ?)",
                            (category, heading, image_url, link))

    conn.commit()
    conn.close()

