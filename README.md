## Web scraping:

Description:-
Web scraping (or data scraping) is a technique used to collect content and data from the internet.This data is usually saved in a local file so that it can be manipulated and analyzed as needed. If
youve ever copied and pasted content from a website into an Excel spreadsheet, this is essentially what web scraping is, but on a very small scale.

|Sr.No| Topic | Overview | 
|-|-|-|

# Abstract:-
Web scraping, also known as data Mining, is the process of collecting large amounts of data from the web and then placing it in database for future analysis and later use.
It offers insight into price data, market dynamics, prevailing trends, practises employed by competitors and the challenges they face.
In this article, We will explain the advantages of Web scraping technique.
This research is based on web based python scrapping tool and the main focus is on BeautifulSoup to scrap the data.

# Why we scrape:-
Web pages contain wealth of information (in text form), designed mostly for human consumption.
Static websites (legacy systems)
Interfacing with 3rd party with no API access
Websites are more important than API’s 
The data is already available (in the form of web pages)
No rate limiting 
Anonymous access 

# Fetching the data:-
Involves finding the endpoint – URL or URL’s
Sending HTTP requests to the server
Using requests library:

       import requests
       data = requests.get(‘http://python.org.com/’)
       html = data.content

# Use BeautifulSoup for parsing:-
Python library for pulling data from HTML and XML files.
Provides simple methods to- 
         * search
         * navigate
         * select
# Deals with broken web-pages really well
Auto-detects encoding
You may use this tool to not only scrape data, but also to clean it up.
A number of python parsers, including lxml and hml5lib, are supported by BeautifulSoup , in addition to the HTML parser included in Python’s standard library.

# Live Demo:-
![image](https://github.com/NiteshNamdev/Web-scraping/assets/154548242/605cc6aa-ac3e-402e-88d3-58f2b2fe37d4)
![image](https://github.com/NiteshNamdev/Web-scraping/assets/154548242/0af4f3be-cdaf-4e74-87f4-00d5c544a42e)
![image](https://github.com/NiteshNamdev/Web-scraping/assets/154548242/f04d6222-6ded-4cff-a86f-faed06cdabd9)







