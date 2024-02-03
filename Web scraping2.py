import requests
from bs4 import BeautifulSoup


source = requests.get('https://www.python.org/')
source.raise_for_status()

soup = BeautifulSoup(source.text, 'html.parser')

articles = soup.find('div', class_='shrubbery').find_all('li')

print("new news in the python.org section")

for article in articles:
    latest_news = article.a.text.strip()
    print(latest_news)
    
    
