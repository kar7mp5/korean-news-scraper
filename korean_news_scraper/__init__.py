from os.path import dirname
from sys import path

path.insert( 0 , dirname( __file__ ) )
from google_news_scraper import googleNewsScraper