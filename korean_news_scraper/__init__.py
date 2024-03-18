from os.path import dirname
from sys import path

path.insert(0, dirname(__file__))

from save_article_links import save_article_links
from extract_article_content import extract_article_content